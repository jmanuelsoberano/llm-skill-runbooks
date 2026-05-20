# Cómo agregar una nueva skill

## Paso 1: Definir propósito

Responde:

- ¿Qué problema resuelve?
- ¿Qué entrada recibe?
- ¿Qué salida produce?
- ¿Quién la usará?
- ¿Cómo sabremos que funcionó?

## Paso 2: Crear carpeta

```bash
mkdir skills/nombre-de-la-skill
```

## Paso 3: Copiar plantilla

Usa:

```text
templates/skill-template.md
templates/prompt-template.md
templates/eval-template.md
```

## Paso 4: Crear archivos mínimos

```text
skill.md
prompt.full.md
input.schema.md
output.schema.md
evals/checklist.md
changelog.md
```

## Paso 5: Agregar ejemplos

```text
examples/sample-input.md
examples/sample-output.md
```

## Paso 6: Registrar la skill

Edita `registry.yaml`.

## Paso 7: Validar

```bash
python scripts/validate_repo.py
```

## Paso 8: Probar con LLM

Ejecuta al menos un caso real y evalúa con checklist.
