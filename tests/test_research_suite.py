"""Behavioral regression tests for portable installation; synthetic packages only."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

spec = importlib.util.spec_from_file_location("suite", Path(__file__).resolve().parents[1] / "scripts/manage_research_suite.py")
suite = importlib.util.module_from_spec(spec)
spec.loader.exec_module(suite)

class SuiteInstallationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="skillbook-test-")
        self.base = Path(self.tmp.name).resolve()
        self.root = self.base / "source"
        self.dest = self.base / "installed"
        self.backup = self.base / "backups"
        self.root.mkdir()
        (self.root / "references").mkdir()
        (self.root / "references/evidence-contract.md").write_text("contract v1", encoding="utf-8")
        (self.root / "research-suite.json").write_text(json.dumps({"version":"0.1.0", "skills":["alpha","beta"]}),encoding="utf-8")
        for name in ("alpha","beta"):
            folder = self.root / "skills" / name
            for rel in suite.REQUIRED:
                p = folder / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text("fixture",encoding="utf-8")
            (folder / "SKILL.md").write_text(f"---\nname: {name}\n---\nInstructions",encoding="utf-8")
        suite.sync(self.root)

    def tearDown(self):
        # TemporaryDirectory created this exact resolved test boundary.
        assert self.base.name.startswith("skillbook-test-")
        self.tmp.cleanup()

    def test_fresh_install_and_repeat_are_identical(self):
        first = suite.install(self.root,self.dest,self.backup)
        self.assertEqual(["alpha","beta"],first["changes"])
        self.assertEqual(suite.hashes(self.root/"skills/alpha"),suite.hashes(self.dest/"alpha"))
        second = suite.install(self.root,self.dest,self.backup)
        self.assertEqual([],second["changes"])
        self.assertEqual(2,second["unchanged"])

    def test_conflict_preflight_makes_no_partial_install(self):
        (self.dest/"beta").mkdir(parents=True)
        (self.dest/"beta/custom.txt").write_text("keep")
        with self.assertRaisesRegex(ValueError,"Existing skill differs"):
            suite.install(self.root,self.dest,self.backup)
        self.assertFalse((self.dest/"alpha").exists())
        self.assertFalse(self.backup.exists())
        self.assertEqual("keep",(self.dest/"beta/custom.txt").read_text())

    def test_explicit_replace_keeps_previous_files(self):
        (self.dest/"alpha").mkdir(parents=True)
        (self.dest/"alpha/custom.txt").write_text("keep")
        result = suite.install(self.root,self.dest,self.backup,replace=["alpha"])
        self.assertEqual("keep",(Path(result["backup"])/"alpha/custom.txt").read_text())
        self.assertFalse((self.dest/"alpha/custom.txt").exists())

    def test_second_move_failure_restores_previous_state(self):
        (self.dest/"alpha").mkdir(parents=True)
        (self.dest/"alpha/custom.txt").write_text("keep")
        original = Path.rename
        def fail_beta(path,target):
            if path.parent.name == "stage" and path.name == "beta":
                raise OSError("simulated destination failure")
            return original(path,target)
        with patch.object(Path,"rename",fail_beta):
            with self.assertRaisesRegex(OSError,"simulated"):
                suite.install(self.root,self.dest,self.backup,replace=["alpha"])
        self.assertEqual({"custom.txt": suite.hashes(self.dest/"alpha")["custom.txt"]},suite.hashes(self.dest/"alpha"))
        self.assertEqual("keep",(self.dest/"alpha/custom.txt").read_text())
        self.assertFalse((self.dest/"beta").exists())

    def test_dry_run_does_not_create_directories(self):
        result = suite.install(self.root,self.dest,self.backup,dry_run=True)
        self.assertEqual(2,len(result["changes"]))
        self.assertFalse(self.dest.exists())
        self.assertFalse(self.backup.exists())

    def test_traversal_rejected(self):
        (self.root/"research-suite.json").write_text(json.dumps({"version":"0.1.0","skills":["../outside"]}))
        with self.assertRaisesRegex(ValueError,"Invalid skill name"):
            suite.check(self.root)

    def test_stale_contract_rejected(self):
        (self.root/"skills/alpha/references/evidence-contract.md").write_text("stale")
        with self.assertRaisesRegex(ValueError,"Outdated evidence contract"):
            suite.install(self.root,self.dest,self.backup)
        self.assertFalse(self.dest.exists())

    def test_backup_inside_source_rejected_without_writes(self):
        backup = self.root/"skills/alpha/backup"
        with self.assertRaisesRegex(ValueError,"Backups must be outside source"):
            suite.install(self.root,self.dest,backup)
        self.assertFalse(backup.exists())
        self.assertFalse(self.dest.exists())

    def test_missing_version_rejected_before_install(self):
        (self.root/"research-suite.json").write_text(json.dumps({"skills":["alpha","beta"]}))
        with self.assertRaisesRegex(ValueError,"semantic version"):
            suite.install(self.root,self.dest,self.backup)
        self.assertFalse(self.dest.exists())

    def test_new_collision_is_not_moved_during_rollback(self):
        original = Path.rename
        def create_collision(path,target):
            if path.parent.name == "stage" and path.name == "beta":
                target.mkdir()
                (target/"concurrent.txt").write_text("belongs to another writer")
                raise OSError("simulated concurrent writer")
            return original(path,target)
        with patch.object(Path,"rename",create_collision):
            with self.assertRaisesRegex(OSError,"concurrent writer"):
                suite.install(self.root,self.dest,self.backup)
        self.assertFalse((self.dest/"alpha").exists())
        self.assertEqual("belongs to another writer",(self.dest/"beta/concurrent.txt").read_text())

    def test_receipt_failure_restores_packages(self):
        original = Path.write_text
        def fail_receipt(path,*args,**kwargs):
            if path.name == "receipt.json":
                raise OSError("simulated receipt failure")
            return original(path,*args,**kwargs)
        with patch.object(Path,"write_text",fail_receipt):
            with self.assertRaisesRegex(OSError,"receipt failure"):
                suite.install(self.root,self.dest,self.backup)
        self.assertFalse((self.dest/"alpha").exists())
        self.assertFalse((self.dest/"beta").exists())

    def test_rollback_failure_does_not_skip_other_packages(self):
        original_rename = Path.rename
        original_write = Path.write_text
        def fail_receipt(path,*args,**kwargs):
            if path.name == "receipt.json":
                raise OSError("original failure")
            return original_write(path,*args,**kwargs)
        def fail_beta_recovery(path,target):
            if path.parent == self.dest and path.name == "beta":
                raise OSError("locked beta")
            return original_rename(path,target)
        with patch.object(Path,"rename",fail_beta_recovery), patch.object(Path,"write_text",fail_receipt):
            with self.assertRaisesRegex(RuntimeError,"original failure.*locked beta"):
                suite.install(self.root,self.dest,self.backup)
        self.assertFalse((self.dest/"alpha").exists())
        self.assertTrue((self.dest/"beta").exists())

    def test_package_normalizes_parent_traversal_before_writing(self):
        (self.root/"work").mkdir()
        output = self.root/"work/../skills/alpha/bundle.zip"
        with self.assertRaisesRegex(ValueError,"outside skills"):
            suite.package(self.root,output)
        self.assertFalse(output.exists())

    def test_invalid_path_during_recovery_does_not_skip_others(self):
        original_write, original_child = Path.write_text, suite.child
        rollback = False
        def fail_receipt(path,*args,**kwargs):
            nonlocal rollback
            if path.name == "receipt.json":
                rollback = True
                raise OSError("original receipt failure")
            return original_write(path,*args,**kwargs)
        def fail_path(base,name):
            if rollback and Path(base) == self.dest and name == "beta":
                raise ValueError("unexpected linked beta")
            return original_child(base,name)
        with patch.object(suite,"child",fail_path), patch.object(Path,"write_text",fail_receipt):
            with self.assertRaisesRegex(RuntimeError,"receipt failure.*linked beta"):
                suite.install(self.root,self.dest,self.backup)
        self.assertFalse((self.dest/"alpha").exists())
        self.assertTrue((self.dest/"beta").exists())

    def test_source_overlap_rejected(self):
        with self.assertRaisesRegex(ValueError,"separate from source"):
            suite.install(self.root,self.root/"skills",self.backup)

    def test_backup_in_discovery_directory_rejected(self):
        with self.assertRaisesRegex(ValueError,"Backups must be outside"):
            suite.install(self.root,self.dest,self.dest/"backups")

    def test_archive_contains_only_suite_and_checksums(self):
        for rel in ("scripts/manage_research_suite.py","playbooks/research-suite.md","workflows/engineering-research.md","LICENSE.md"):
            p=self.root/rel
            p.parent.mkdir(parents=True,exist_ok=True)
            p.write_text("fixture")
        output=self.base/"suite.zip"
        count=suite.package(self.root,output)
        with zipfile.ZipFile(output) as archive:
            data=json.loads(archive.read("bundle-hashes.json"))
            self.assertEqual(count,len(data))
            for name,digest in data.items():
                self.assertEqual(digest,suite.hashlib.sha256(archive.read(name)).hexdigest())
            self.assertFalse(any(".git/" in n for n in archive.namelist()))

if __name__=="__main__":
    unittest.main()
