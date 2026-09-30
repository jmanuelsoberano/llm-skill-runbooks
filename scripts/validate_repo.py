#!/usr/bin/env python3
"""Validate Skillbook metadata, portable entrypoints and local entrypoint links."""

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError as error:
    raise SystemExit(
        "Missing validation dependency. Run: python -m pip install -r requirements-dev.txt"
    ) from error

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "prompt.full.md", "input.schema.md", "output.schema.md",
    "evals/checklist.md", "changelog.md",
)
REQUIRED_LINKS = ("prompt.full.md", "input.schema.md", "output.schema.md")
INLINE_LINK = re.compile(
    r"\[[^\]\n]+\]\((?:<([^>\n]+)>|([^\s)]+))(?:\s+\"[^\"]*\")?\)"
)
REFERENCE_LINK = re.compile(r"^ {0,3}\[[^\]\n]+\]:\s*(?:<([^>\n]+)>|(\S+))", re.M)


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject silent overwrites and non-string mapping keys in metadata."""

    def construct_mapping(self, node, deep=False):
        mapping = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str):
                raise yaml.constructor.ConstructorError(
                    None, None, "Metadata keys must be strings", key_node.start_mark
                )
            if key in mapping:
                raise yaml.constructor.ConstructorError(
                    None, None, f"Duplicate YAML key: {key}", key_node.start_mark
                )
            mapping[key] = self.construct_object(value_node, deep=deep)
        return mapping


def read_text(path, errors):
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        errors.append(f"{path}: cannot read UTF-8 text: {error}")
        return None


def load_yaml(text, label, errors):
    try:
        value = yaml.load(text, Loader=UniqueKeyLoader)
    except yaml.YAMLError as error:
        errors.append(f"{label}: invalid YAML: {error}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{label}: expected a YAML mapping")
        return None
    return value


def load_schema(path, errors):
    text = read_text(path, errors)
    if text is None:
        return None
    try:
        schema = json.loads(text)
        Draft202012Validator.check_schema(schema)
        return Draft202012Validator(schema)
    except (json.JSONDecodeError, SchemaError) as error:
        # Schema errors are configuration failures, not successful validation.
        errors.append(f"{path}: invalid validation schema: {error}")
        return None


def validate_schema(value, validator, label, errors):
    if validator is None:
        return
    for error in validator.iter_errors(value):
        field = ".".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"{label}: {field}: {error.message}")


def exact_local_path(base, relative):
    """Resolve a package-local path, checking case even on Windows."""
    if not relative or "\\" in relative or relative.startswith("/"):
        raise ValueError("use a relative path with forward slashes")
    parts = relative.rstrip("/").split("/")
    if any(part in ("", ".", "..") or ":" in part for part in parts):
        raise ValueError("use a package-local path without traversal")
    current = base
    for part in parts:
        if not current.is_dir() or part not in {entry.name for entry in current.iterdir()}:
            raise ValueError(f"missing path or incorrect case: {relative}")
        current = current / part
    if not current.resolve().is_relative_to(base.resolve()):
        raise ValueError(f"path escapes its package: {relative}")
    return current


def markdown_links(body):
    """Read conventional inline links and reference definitions outside fences."""
    lines = []
    fence_marker = None
    fence_length = 0
    for line in body.splitlines():
        fence = re.match(r"^\s*(\x60{3,}|~{3,})(.*)$", line)
        if fence:
            marker, suffix = fence.groups()
            if fence_marker is None:
                fence_marker, fence_length = marker[0], len(marker)
            elif marker[0] == fence_marker and len(marker) >= fence_length and not suffix.strip():
                fence_marker = None
            continue
        if fence_marker is None:
            # Avoid treating code examples as operational links.
            lines.append(re.sub(r"\x60+[^\x60]*\x60+", "", line))
    text = "\n".join(lines)
    return [match.group(1) or match.group(2)
            for pattern in (INLINE_LINK, REFERENCE_LINK)
            for match in pattern.finditer(text)]


def validate_entrypoint(folder, validator, errors):
    label = f"skills/{folder.name}/SKILL.md"
    candidates = [entry.name for entry in folder.iterdir() if entry.name.lower() == "skill.md"]
    if candidates != ["SKILL.md"]:
        errors.append(f"{label}: exactly one entrypoint named SKILL.md is required; found {candidates}")
        return None
    text = read_text(folder / "SKILL.md", errors)
    if text is None:
        return None
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.S)
    if not match:
        errors.append(f"{label}: missing or unclosed YAML frontmatter")
        return None
    frontmatter = load_yaml(match.group(1), label, errors)
    if frontmatter is None:
        return None
    validate_schema(frontmatter, validator, label, errors)
    if frontmatter.get("name") != folder.name:
        errors.append(f"{label}: name must match folder name {folder.name}")
    body = text[match.end():]
    if not body.strip():
        errors.append(f"{label}: skill instructions are empty")
    local_links = set()
    for target in markdown_links(body):
        try:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            relative = unquote(parsed.path)
            exact_local_path(folder, relative)
            local_links.add(relative)
        except (OSError, ValueError) as error:
            errors.append(f"{label}: invalid reference {target}: {error}")
    for required in REQUIRED_LINKS:
        if required not in local_links:
            errors.append(f"{label}: link the required procedure/contract: {required}")
    for prompt in folder.glob("prompt*.md"):
        if prompt.name not in local_links:
            errors.append(f"{label}: prompt variant is not linked: {prompt.name}")
    return frontmatter


def validate_repo(root=ROOT):
    root = Path(root)
    errors = []
    entry_validator = load_schema(root / "schemas/agent-skill.schema.json", errors)
    registry_validator = load_schema(root / "schemas/skill.schema.json", errors)
    registry_text = read_text(root / "registry.yaml", errors)
    registry = load_yaml(registry_text, "registry.yaml", errors) if registry_text is not None else None
    entries = registry.get("skills") if registry is not None else None
    if not isinstance(entries, list) or not entries:
        errors.append("registry.yaml: skills must be a non-empty list")
        entries = []
    indexed = {}
    seen_ids = set()
    for index, entry in enumerate(entries):
        label = f"registry.yaml: skills[{index}]"
        validate_schema(entry, registry_validator, label, errors)
        if not isinstance(entry, dict):
            continue
        skill_id, path = entry.get("id"), entry.get("path")
        if isinstance(skill_id, str):
            if skill_id in seen_ids:
                errors.append(f"{label}: duplicate id: {skill_id}")
            seen_ids.add(skill_id)
        if not isinstance(path, str):
            continue
        if path in indexed:
            errors.append(f"{label}: duplicate path: {path}")
        indexed[path] = entry
        try:
            if not exact_local_path(root, path).is_dir():
                errors.append(f"{label}: skill path is not a directory: {path}")
        except (OSError, ValueError) as error:
            errors.append(f"{label}: {error}")
    skills_dir = root / "skills"
    folders = sorted(path for path in skills_dir.iterdir() if path.is_dir()) if skills_dir.is_dir() else []
    if not folders:
        errors.append("skills/: no skill directories found")
    for folder in folders:
        label = f"skills/{folder.name}"
        for relative in REQUIRED_FILES:
            try:
                path = exact_local_path(folder, relative)
                if not path.is_file():
                    errors.append(f"{label}/{relative}: required file is not a file")
                    continue
                content = read_text(path, errors)
                if content is not None and not content.strip():
                    errors.append(f"{label}/{relative}: required file is empty")
            except (OSError, ValueError) as error:
                errors.append(f"{label}: {error}")
        for prompt in sorted(folder.glob("prompt*.md")):
            content = read_text(prompt, errors)
            if content is not None and len(content.strip()) < 200:
                errors.append(f"{label}/{prompt.name}: prompt must contain at least 200 characters")
        frontmatter = validate_entrypoint(folder, entry_validator, errors)
        entry = indexed.get(label)
        if entry is None:
            errors.append(f"{label}: missing registry entry")
        elif frontmatter is not None and isinstance(frontmatter.get("metadata"), dict):
            for field in ("id", "version", "status"):
                if frontmatter["metadata"].get(field) != entry.get(field):
                    errors.append(f"{label}: metadata.{field} disagrees with registry.yaml")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root to validate")
    args = parser.parse_args()
    errors = validate_repo(args.root)
    if errors:
        for error in errors:
            print(f"[ERROR] {error}", file=sys.stderr)
        print(f"Validation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1
    print("Validation passed: native entrypoints, metadata, registry, files and entrypoint links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
