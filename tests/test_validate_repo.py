"""Behavioral regression tests for catalog validation, using isolated repositories."""

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import yaml

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_repo", REPO / "scripts/validate_repo.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        shutil.copytree(REPO / "schemas", self.root / "schemas")
        self.skill = self.root / "skills" / "sample-skill"
        (self.skill / "evals").mkdir(parents=True)
        for relative in VALIDATOR.REQUIRED_FILES:
            (self.skill / relative).write_text(
                "# Procedure\n\nUse the supplied document as evidence, preserve uncertainty, "
                "and return the requested analysis. Confirm the relevant contracts and distinguish "
                "known facts from proposals. Review the result for omissions before delivering it.\n",
                encoding="utf-8",
            )
        self.frontmatter = {
            "name": "sample-skill",
            "description": "Analiza documentos cuando el usuario solicita requisitos.",
            "metadata": {"id": "sample.skill", "version": "1.0.0", "status": "draft"},
        }
        self.body = (
            "# Sample skill\n\n"
            "Read [the procedure](prompt.full.md), [input](input.schema.md), "
            "and [output](output.schema.md).\n"
        )
        self.entry = {
            "id": "sample.skill", "name": "Sample skill", "path": "skills/sample-skill",
            "version": "1.0.0", "status": "draft", "category": "general",
            "tags": ["sample"], "input_types": ["text"], "output_formats": ["markdown"],
        }
        self.write_entrypoint()
        self.write_registry([self.entry])

    def write_entrypoint(self):
        (self.skill / "SKILL.md").write_text(
            "---\n" + yaml.safe_dump(self.frontmatter, allow_unicode=True) + "---\n\n" + self.body,
            encoding="utf-8",
        )

    def write_registry(self, entries):
        (self.root / "registry.yaml").write_text(yaml.safe_dump({"skills": entries}), encoding="utf-8")

    def assert_invalid(self, message):
        errors = VALIDATOR.validate_repo(self.root)
        self.assertTrue(any(message in error for error in errors), errors)

    def test_valid_portable_skill_passes(self):
        self.assertEqual([], VALIDATOR.validate_repo(self.root))

    def test_missing_or_blank_description_fails(self):
        for value in (None, "", "   ", 42):
            with self.subTest(value=value):
                self.frontmatter["description"] = value
                self.write_entrypoint()
                self.assert_invalid("description")
        del self.frontmatter["description"]
        self.write_entrypoint()
        self.assert_invalid("description")

    def test_invalid_name_or_folder_mismatch_fails(self):
        for value in ("Other-Skill", "sample--skill", "another-skill", "x" * 65):
            with self.subTest(value=value):
                self.frontmatter["name"] = value
                self.write_entrypoint()
                self.assert_invalid("name")

    def test_custom_metadata_must_use_strings(self):
        self.frontmatter["metadata"]["revision"] = 1
        self.write_entrypoint()
        self.assert_invalid("metadata.revision")

    def test_legacy_top_level_fields_fail(self):
        self.frontmatter["id"] = "sample.skill"
        self.write_entrypoint()
        self.assert_invalid("Additional properties")

    def test_malformed_or_unclosed_frontmatter_fails(self):
        for content in ("---\nname: [\n---\nBody", "---\nname: sample-skill\nBody", "---\n- item\n---\nBody"):
            with self.subTest(content=content):
                (self.skill / "SKILL.md").write_text(content, encoding="utf-8")
                self.assert_invalid("SKILL.md")

    def test_duplicate_yaml_keys_fail_instead_of_silent_overwrite(self):
        path = self.skill / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "name: sample-skill", "name: another-skill\nname: sample-skill"
        ), encoding="utf-8")
        self.assert_invalid("Duplicate YAML key")

    def test_lowercase_entrypoint_fails_on_windows_too(self):
        temporary = self.skill / "entry.tmp"
        (self.skill / "SKILL.md").rename(temporary)
        temporary.rename(self.skill / "skill.md")
        self.assert_invalid("exactly one entrypoint")

    def test_duplicate_entrypoints_fail_on_case_sensitive_filesystems(self):
        # The path cannot exist separately on case-insensitive filesystems.
        if (self.skill / "skill.md").exists():
            self.skipTest("Filesystem does not support distinct case-only filenames")
        (self.skill / "skill.md").write_text("Legacy entry", encoding="utf-8")
        self.assert_invalid("exactly one entrypoint")

    def test_broken_or_case_mismatched_links_fail(self):
        for target in ("missing.md", "Input.schema.md"):
            with self.subTest(target=target):
                self.body += f"\n[Read this]({target})\n"
                self.write_entrypoint()
                self.assert_invalid(f"invalid reference {target}")

    def test_link_cannot_escape_installable_package(self):
        (self.skill.parent / "shared.md").write_text("Outside the package", encoding="utf-8")
        self.body += "\n[Shared procedure](../shared.md)\n"
        self.write_entrypoint()
        self.assert_invalid("without traversal")

    def test_linked_directory_is_supported(self):
        self.body += "\n[Evaluation resources](evals/)\n"
        self.write_entrypoint()
        self.assertEqual([], VALIDATOR.validate_repo(self.root))

    def test_fenced_examples_and_web_links_do_not_require_local_files(self):
        self.body += (
            "\n```markdown\n[Example](does-not-exist.md)\n```\n"
            "\n[Specification](https://agentskills.io/specification)\n"
            "\n[This heading](#sample-skill)\n"
        )
        self.write_entrypoint()
        self.assertEqual([], VALIDATOR.validate_repo(self.root))

    def test_reference_style_links_are_validated(self):
        self.body += "\nSee [guide].\n\n[guide]: missing.md\n"
        self.write_entrypoint()
        self.assert_invalid("invalid reference missing.md")

    def test_unlinked_procedure_or_variant_fails(self):
        self.body = self.body.replace("[the procedure](prompt.full.md)", "the procedure")
        self.write_entrypoint()
        self.assert_invalid("link the required procedure/contract: prompt.full.md")
        (self.skill / "prompt.quick.md").write_text(
            (self.skill / "prompt.full.md").read_text(encoding="utf-8"), encoding="utf-8"
        )
        self.assert_invalid("prompt variant is not linked: prompt.quick.md")

    def test_required_file_cannot_be_replaced_with_a_directory(self):
        path = self.skill / "changelog.md"
        path.unlink()
        path.mkdir()
        self.assert_invalid("required file is not a file")

    def test_empty_required_file_fails(self):
        (self.skill / "evals/checklist.md").write_text("  \n", encoding="utf-8")
        self.assert_invalid("required file is empty")

    def test_registry_metadata_drift_fails(self):
        for field, replacement in (("id", "different.id"), ("version", "2.0.0"), ("status", "stable")):
            with self.subTest(field=field):
                entry = {**self.entry, field: replacement}
                self.write_registry([entry])
                self.assert_invalid(f"metadata.{field} disagrees")

    def test_duplicate_registry_entries_fail(self):
        self.write_registry([self.entry, self.entry])
        self.assert_invalid("duplicate id")
        self.assert_invalid("duplicate path")

    def test_nonexistent_registry_path_fails(self):
        self.write_registry([{**self.entry, "path": "skills/absent-skill"}])
        self.assert_invalid("missing path or incorrect case")
        self.assert_invalid("missing registry entry")

    def test_malformed_registry_fails_cleanly(self):
        for text in ("skills: [", "skills: string", "skills:\n  - not-a-mapping", "skills: []\nskills: []"):
            with self.subTest(text=text):
                (self.root / "registry.yaml").write_text(text, encoding="utf-8")
                self.assertTrue(VALIDATOR.validate_repo(self.root))

    def test_invalid_schema_is_a_failure(self):
        (self.root / "schemas/agent-skill.schema.json").write_text(
            json.dumps({"type": "unknown-type"}), encoding="utf-8"
        )
        self.assert_invalid("invalid validation schema")


if __name__ == "__main__":
    unittest.main()
