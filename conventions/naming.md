# Convenciones de nombres

## IDs de skills

Usa IDs en minúsculas con puntos:

```text
meeting.transcript.analysis
repository.issue.generator
technical.requirements.extractor
```

## Carpetas

Usa kebab-case:

```text
meeting-transcript-analysis
repository-issue-generator
technical-requirements-extractor
```

## Prompts

Usa nombres explícitos:

```text
prompt.full.md
prompt.quick.md
prompt.file-input.md
prompt.multi-transcript.md
prompt.chunked-long-transcript.md
```

## Archivos obligatorios por skill

```text
skill.md
prompt.full.md
input.schema.md
output.schema.md
evals/checklist.md
changelog.md
```

## Estados de skill

| Estado | Significado |
|---|---|
| draft | En diseño. Puede cambiar. |
| experimental | Usable, pero no estable. |
| stable | Contrato estable. Cambios incompatibles requieren versión mayor. |
| deprecated | Ya no se recomienda. |
