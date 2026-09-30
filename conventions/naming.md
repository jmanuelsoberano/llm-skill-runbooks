# Convenciones de nombres

## Entrada nativa

Cada carpeta dentro de `skills/` tiene exactamente un archivo `SKILL.md`. No mantengas una segunda entrada `skill.md`: los nombres colisionan en sistemas sin distinción de mayúsculas.

El frontmatter incluye `name` en kebab-case, idéntico al nombre de la carpeta, y `description` que explica qué hace y cuándo aplica. Los campos de catálogo van bajo `metadata`:

```yaml
---
name: meeting-transcript-analysis
description: Analiza transcripts y notas de reuniones para extraer decisiones y compromisos.
metadata:
  id: "meeting.transcript.analysis"
  version: "1.1.0"
  status: "stable"
---
```

Los IDs con puntos son identificadores del catálogo. El nombre visible en español, categoría, etiquetas y formatos permanecen en `registry.yaml`. `metadata` contiene valores de texto; entrecomilla versiones y otros valores que YAML pueda interpretar como números.

## Archivos del catálogo

```text
SKILL.md
prompt.full.md
input.schema.md
output.schema.md
evals/checklist.md
changelog.md
```

Estos archivos adicionales son convenciones de Skillbook; el estándar Agent Skills solo exige la entrada nativa. Añade ejemplos y casos de evaluación útiles para verificar la tarea.

Mantén los nombres de variantes explícitos: `prompt.quick.md`, `prompt.file-input.md`, `prompt.multi-transcript.md` o `prompt.chunked-long-transcript.md`.

## Referencias portables

Desde `SKILL.md`, enlaza el procedimiento, los contratos y cada variante, explicando cuándo leerlos. Usa enlaces Markdown convencionales relativos a la raíz de la skill:

```markdown
Lee [el procedimiento](prompt.full.md).
Para cambios de datos, consulta [la referencia](references/data-changes.md).
```

Respeta las mayúsculas exactas, usa barras `/` y conserva los recursos dentro de la carpeta de la skill. No dependas de archivos vecinos al paquete instalado.

El validador revisa enlaces inline y definiciones de enlaces de referencia fuera de bloques de código; no es un parser completo de Markdown. Para recursos operativos usa el formato sencillo mostrado arriba, sin rutas absolutas, `..` ni paréntesis en el nombre del archivo. No valida anclas, enlaces externos ni rutas escritas solo como texto.

## Estados

| Estado | Significado |
|---|---|
| draft | En diseño; puede cambiar. |
| experimental | Disponible para probar; requiere evaluación. |
| stable | Contrato estable; cambios incompatibles requieren versión mayor. |
| deprecated | Ya no se recomienda. |
