# Cómo agregar una nueva skill

## Definir y reutilizar

Describe el problema, la entrada, la salida y las condiciones que permiten evaluar el resultado. Revisa si una skill existente ya cubre la tarea antes de crear otra.

## Crear la carpeta

Crea `skills/<skill-name>/` usando kebab-case. Adapta [la plantilla de entrada](../templates/skill-template.md) como `SKILL.md`, y la plantilla de prompt como `prompt.full.md`.

El catálogo requiere:

```text
SKILL.md
prompt.full.md
input.schema.md
output.schema.md
evals/checklist.md
changelog.md
```

`SKILL.md` debe enlazar los contratos y el procedimiento. Si hay variantes, explica cómo elegirlas; no cargues todas por defecto. Copiar una estructura sin reemplazar sus instrucciones de plantilla no completa una skill.

## Registrar y evaluar

1. Añade una entrada en `registry.yaml`. Conserva el mismo ID, versión y estado que `metadata` en `SKILL.md`.
2. Añade al menos un caso representativo de entrada y salida, más criterios que detecten errores relevantes. Separa fixtures, instrucciones y resultados de ejecución.
3. Instala las dependencias de validación en un entorno virtual y ejecuta desde la raíz:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

4. Instala la carpeta completa en un entorno de pruebas del cliente y verifica que la detecte.
5. Ejecuta un caso representativo con un LLM y evalúa el resultado con la checklist. Registra cliente/modelo, fecha, entrada, salida y límites de la prueba. Un caso escrito pero no ejecutado es una expectativa, no evidencia de funcionamiento.

Consulta [instalación](use-and-install-agent-skills.md), [evaluaciones](how-to-run-evals.md) y [migración de entradas anteriores](migrate-existing-skills.md).
