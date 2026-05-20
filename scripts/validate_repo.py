from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

REQUIRED_SKILL_FILES = [
    "skill.md",
    "prompt.full.md",
    "input.schema.md",
    "output.schema.md",
    "evals/checklist.md",
    "changelog.md",
]

def fail(message: str) -> None:
    print(f"[ERROR] {message}")

def ok(message: str) -> None:
    print(f"[OK] {message}")

def main() -> int:
    errors = 0

    if not SKILLS_DIR.exists():
        fail("No existe la carpeta skills/")
        return 1

    skill_dirs = [p for p in SKILLS_DIR.iterdir() if p.is_dir()]
    if not skill_dirs:
        fail("No hay skills en skills/")
        return 1

    for skill_dir in sorted(skill_dirs):
        print(f"\nValidando skill: {skill_dir.name}")
        for rel in REQUIRED_SKILL_FILES:
            target = skill_dir / rel
            if target.exists():
                ok(rel)
            else:
                fail(f"Falta {rel}")
                errors += 1

        # Revisión simple de prompts vacíos
        prompt_files = list(skill_dir.glob("prompt*.md"))
        if not prompt_files:
            fail("No hay archivos prompt*.md")
            errors += 1
        else:
            for prompt in prompt_files:
                text = prompt.read_text(encoding="utf-8").strip()
                if len(text) < 200:
                    fail(f"{prompt.name} parece demasiado corto")
                    errors += 1
                else:
                    ok(f"{prompt.name} tiene contenido")

    print("\nResumen")
    if errors:
        print(f"Validación terminada con {errors} error(es).")
        return 1

    print("Validación completada sin errores críticos.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
