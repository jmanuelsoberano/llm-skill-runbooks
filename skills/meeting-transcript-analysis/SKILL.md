---
name: meeting-transcript-analysis
description: Analiza transcripts, minutas o notas de reuniones para extraer decisiones,
  compromisos, riesgos y requerimientos con evidencia. Úsala con texto, archivos,
  reuniones relacionadas o transcripts entregados por partes. No transcribe audio.
metadata:
  id: meeting.transcript.analysis
  version: 1.1.0
  status: stable
---

# Skill: Análisis de transcripts de reuniones

## Ejecución como Agent Skill

Lee [input.schema.md](input.schema.md) y selecciona el procedimiento según la entrada y el pedido; las rutas se aplican en este orden:

1. Si el usuario está entregando un transcript por partes, usa [prompt.chunked-long-transcript.md](prompt.chunked-long-transcript.md). Espera `FIN DEL TRANSCRIPT` antes del documento final. Si ya llegó una parte, confirma esa parte sin volver a pedir la primera.
2. Para varias reuniones relacionadas, usa [prompt.multi-transcript.md](prompt.multi-transcript.md); distingue las reuniones antes de consolidarlas.
3. Para un resumen rápido solicitado, usa [prompt.quick.md](prompt.quick.md), también si la fuente es un archivo accesible.
4. Para una reunión en archivo, usa [prompt.file-input.md](prompt.file-input.md).
5. Para el análisis completo de una reunión en texto, usa [prompt.full.md](prompt.full.md).

Lee y aplica la variante elegida. Los marcadores de ejemplo se sustituyen con el material disponible; no vuelvas a pedir una entrada ya proporcionada. Lee el contenido de los archivos con las herramientas disponibles; si no puedes acceder, indica la limitación sin simular una lectura.

[output.schema.md](output.schema.md) define el análisis completo. Conserva las secciones aunque no haya evidencia para llenarlas. Las variantes rápida y consolidada mantienen los formatos específicos que ya definen sus propios prompts; no las mezcles con el formato completo. Usa [evals/checklist.md](evals/checklist.md) para revisar la salida aplicable.

Para mantenimiento, prueba las rutas con [evals/agent-cases.md](evals/agent-cases.md).

## Propósito

Convertir transcripts de reuniones, especialmente de Microsoft Teams, en documentos Markdown estructurados, accionables y reutilizables para seguimiento, documentación, análisis técnico, generación de issues y toma de decisiones.

## Cuándo usarla

Usa esta skill cuando tengas:

- transcript de Microsoft Teams;
- minuta larga y desordenada;
- notas de reunión;
- conversación exportada;
- archivo `.txt`, `.docx`, `.pdf`, `.vtt`, `.csv` o similar;
- varias reuniones que necesitas consolidar.

## Cuándo no usarla

No usar esta skill cuando:

- necesites transcribir audio desde cero;
- solo quieras corregir ortografía;
- la entrada no sea una conversación o minuta;
- necesites análisis legal, médico o financiero especializado sin revisión humana.

## Entradas esperadas

Ver [input.schema.md](input.schema.md).

## Salida esperada

Ver [output.schema.md](output.schema.md).

## Prompts disponibles

| Archivo | Uso |
|---|---|
| [prompt.full.md](prompt.full.md) | Análisis completo. |
| [prompt.quick.md](prompt.quick.md) | Análisis rápido. |
| [prompt.file-input.md](prompt.file-input.md) | Transcript adjunto como archivo. |
| [prompt.multi-transcript.md](prompt.multi-transcript.md) | Varios transcripts. |
| [prompt.chunked-long-transcript.md](prompt.chunked-long-transcript.md) | Transcript muy largo dividido en partes. |

## Criterios de calidad

Ver [evals/checklist.md](evals/checklist.md).

## Mantenimiento

- Cambios menores de redacción: patch.
- Nuevas secciones compatibles: minor.
- Cambio en estructura obligatoria: major.
