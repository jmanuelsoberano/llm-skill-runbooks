#!/usr/bin/env python3
"""Check, synchronize, package and install the engineering research suite (stdlib only)."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import uuid
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("SKILL.md", "prompt.full.md", "input.schema.md", "output.schema.md",
            "evals/checklist.md", "changelog.md", "references/evidence-contract.md")
IGNORED = {"__pycache__", ".git", ".DS_Store"}

def clean_tree(root):
    """Reject junctions/symlinks so copy and move boundaries remain explicit."""
    root = Path(root)
    for path in (root, *root.rglob("*")):
        if path.is_symlink() or getattr(path, "is_junction", lambda: False)():
            raise ValueError(f"Links are not supported in a package: {path}")
    return root

def child(base, name):
    base = Path(base).absolute()
    path = base / name
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError(f"Invalid skill name: {name}")
    if path.resolve().parent != base.resolve() or path.is_symlink() or getattr(path, "is_junction", lambda: False)():
        raise ValueError(f"Path escapes intended directory: {path}")
    return path

def manifest(root):
    data = json.loads((root / "research-suite.json").read_text(encoding="utf-8"))
    if not isinstance(data.get("version"), str) or not re.fullmatch(r"\d+\.\d+\.\d+", data["version"]):
        raise ValueError("Suite version must be a semantic version")
    names = data["skills"]
    if (not isinstance(names, list) or not names or
            not all(isinstance(name, str) for name in names) or len(names) != len(set(names))):
        raise ValueError("Suite must contain unique skill names")
    for name in names:
        child(root / "skills", name)
    return data

def files(root):
    clean_tree(root)
    return sorted(p for p in root.rglob("*") if p.is_file() and
                  not set(p.relative_to(root).parts).intersection(IGNORED) and p.suffix != ".pyc")

def hashes(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in files(root)}

def sync(root):
    source = (root / "references/evidence-contract.md").read_bytes()
    for name in manifest(root)["skills"]:
        folder = child(root / "skills", name)
        clean_tree(folder)
        target = folder / "references/evidence-contract.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source)

def check(root):
    data = manifest(root)
    common = (root / "references/evidence-contract.md").read_bytes()
    for name in data["skills"]:
        folder = clean_tree(child(root / "skills", name))
        for relative in REQUIRED:
            p = folder / relative
            if not p.is_file() or not p.read_text(encoding="utf-8").strip():
                raise ValueError(f"Missing/empty resource: {name}/{relative}")
        if (folder / "references/evidence-contract.md").read_bytes() != common:
            raise ValueError(f"Outdated evidence contract: {name}; run sync")
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        if not re.search(r"^name:\s*[\"']?" + re.escape(name) + r"[\"']?\s*$", text, re.M):
            raise ValueError(f"Entrypoint name mismatch: {name}")
    return data

def package(root, output):
    data = check(root)
    output = Path(output).absolute()
    for p in (output, *output.parents):
        if p.is_symlink() or getattr(p, "is_junction", lambda: False)():
            raise ValueError(f"Linked package output: {p}")
    output = output.resolve()
    # Prevent packaging from adding files to a skill source.
    if output.is_relative_to((root / "skills").resolve()):
        raise ValueError("Package output must be outside skills/")
    entries = {}
    for name in data["skills"]:
        folder = root / "skills" / name
        for p in files(folder):
            entries[p.relative_to(root).as_posix()] = p.read_bytes()
    for rel in ("research-suite.json", "references/evidence-contract.md",
                "scripts/manage_research_suite.py", "playbooks/research-suite.md",
                "workflows/engineering-research.md", "LICENSE.md"):
        entries[rel] = (root / rel).read_bytes()
    digest = {p: hashlib.sha256(content).hexdigest() for p, content in entries.items()}
    entries["bundle-hashes.json"] = (json.dumps(digest, indent=2, ensure_ascii=False) + "\n").encode()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in entries.items():
            archive.writestr(name, content)
    return len(digest)

def install(root, destination, backup_root, replace=(), dry_run=False):
    data = check(root)
    destination = Path(destination).absolute()
    backup_root = Path(backup_root).absolute()
    # Installation must not modify source packages.
    if (destination.resolve().is_relative_to(root.resolve()) or
            root.resolve().is_relative_to(destination.resolve())):
        raise ValueError("Installation destination must be separate from source")
    if backup_root.resolve().is_relative_to(destination.resolve()):
        raise ValueError("Backups must be outside the skills discovery directory")
    if backup_root.resolve().is_relative_to(root.resolve()):
        raise ValueError("Backups must be outside source")
    for base in (destination, backup_root):
        for p in (base, *base.parents):
            if p.is_symlink() or getattr(p, "is_junction", lambda: False)():
                raise ValueError(f"Linked destination ancestor: {p}")
    unknown = set(replace) - set(data["skills"])
    if unknown:
        raise ValueError(f"Unknown replacement names: {sorted(unknown)}")
    plan = []
    # Complete conflict preflight before any mutation.
    for name in data["skills"]:
        src = child(root / "skills", name)
        target = child(destination, name)
        if target.exists() and not target.is_dir():
            raise ValueError(f"Destination is not a directory: {target}")
        if target.exists() and hashes(src) == hashes(target):
            continue
        if target.exists() and name not in replace:
            raise ValueError(f"Existing skill differs: {name}; review and pass --replace {name}")
        if target.exists():
            clean_tree(target)
        plan.append((name, target.exists(), hashes(src), hashes(target) if target.exists() else None))
    if dry_run or not plan:
        return {"dry_run": dry_run, "changes": [n for n, _, _, _ in plan],
                "unchanged": len(data["skills"]) - len(plan)}
    run = backup_root / ("install-" + uuid.uuid4().hex)
    run.mkdir(parents=True, exist_ok=False)
    stage, previous, failed = (run / n for n in ("stage", "previous", "failed"))
    for p in (stage, previous, failed):
        p.mkdir()
    destination.mkdir(parents=True, exist_ok=True)
    for name, existed, expected, before in plan:
        shutil.copytree(child(root / "skills", name), child(stage, name),
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".git", ".DS_Store"))
        if hashes(child(stage, name)) != expected:
            raise ValueError(f"Staged package checksum mismatch: {name}")
    completed = []
    receipt = {"suite_version": data["version"], "destination": str(destination),
               "changes": [name for name, _, _, _ in plan],
               "unchanged": len(data["skills"]) - len(plan),
               "backup": str(previous),
               "hashes": {name: expected for name, _, expected, _ in plan}}
    journal = run / "journal.json"
    def write_journal(status, errors=None):
        journal.write_text(json.dumps({"status": status, "destination": str(destination),
                           "operations": completed, "recovery_errors": errors or []},
                           ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_journal("prepared")
    try:
        for name, existed, expected, before in plan:
            target = child(destination, name)
            old = child(previous, name)
            # Resolved paths checked immediately before each whole-directory move.
            if target.exists() != existed or (existed and hashes(target) != before):
                raise ValueError(f"Destination changed after preflight: {target}")
            operation = {"name": name, "moved_old": False, "installed_new": False}
            completed.append(operation)
            if existed:
                target.rename(old)
                operation["moved_old"] = True
            child(stage, name).rename(target)
            operation["installed_new"] = True
            if hashes(target) != expected:
                raise ValueError(f"Installed package checksum mismatch: {name}")
            write_journal("applying")
        (run / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_journal("complete")
    except Exception as initial_error:
        errors = []
        for operation in reversed(completed):
            name = operation["name"]
            backup_location = previous / name
            try:
                target, old = child(destination, name), child(previous, name)
                if operation["installed_new"] and target.exists():
                    if hashes(target) != receipt["hashes"][name]:
                        raise ValueError(f"Installed files changed; manual recovery required: {target}")
                    target.rename(child(failed, name))
                if operation["moved_old"]:
                    if target.exists():
                        raise ValueError(f"Unexpected destination; previous files remain at {old}")
                    old.rename(target)
            except Exception as recovery_error:
                errors.append(f"{name}: {recovery_error}; backup: {backup_location}")
        try:
            write_journal("recovery-incomplete" if errors else "rolled-back", errors)
        except OSError as journal_error:
            errors.append(f"Could not record recovery: {journal_error}")
        if errors:
            raise RuntimeError(f"Install failed: {initial_error}. Recovery requires attention: " + "; ".join(errors)) from initial_error
        raise
    return receipt

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("sync")
    sub.add_parser("check")
    p = sub.add_parser("package")
    p.add_argument("--output", required=True, type=Path)
    p = sub.add_parser("install")
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    p.add_argument("--dest", type=Path, default=codex_home / "skills")
    p.add_argument("--backup-root", type=Path, default=codex_home / "skill-backups")
    p.add_argument("--replace", action="append", default=[])
    p.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command == "sync":
        sync(root)
        print("Evidence contract synchronized.")
    elif args.command == "check":
        data = check(root)
        print(f"Suite checks passed: {len(data['skills'])} packages.")
    elif args.command == "package":
        count = package(root, args.output)
        print(f"Packaged {count} files with checksums: {args.output}")
    else:
        result = install(root, args.dest, args.backup_root, args.replace, args.dry_run)
        print(json.dumps({k: v for k, v in result.items() if k != "hashes"}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
