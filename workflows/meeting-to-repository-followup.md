# Workflow: De transcript de reunión a seguimiento en repositorio

## Objetivo

Convertir una reunión en acciones rastreables dentro de un repositorio.

## Flujo

```text
Transcript
  → meeting-transcript-analysis
  → repository-issue-generator
  → revisión humana
  → creación de issues
  → seguimiento
```

## Paso 1: Analizar transcript

Usa:

```text
skills/meeting-transcript-analysis/prompt.file-input.md
```

o:

```text
skills/meeting-transcript-analysis/prompt.full.md
```

Resultado esperado:

```text
analysis.md
```

## Paso 2: Generar issues

Pasa `analysis.md` a:

```text
skills/repository-issue-generator/prompt.full.md
```

Resultado esperado:

```text
issues.md
```

## Paso 3: Revisión humana

Antes de crear issues reales, confirmar:

- responsables;
- prioridad;
- alcance;
- dependencias;
- criterios de aceptación;
- etiquetas;
- fechas.

## Paso 4: Crear issues

Puedes copiar manualmente o crear automatización posterior.

## Paso 5: Guardar trazabilidad

Guarda en el repo:

```text
docs/meetings/YYYY-MM-DD-topic.md
docs/decisions/
docs/requirements/
```

## Recomendación

No conviertas todos los comentarios de una reunión en issues. Solo crea issues cuando haya acción clara, valor y posibilidad de verificación.
