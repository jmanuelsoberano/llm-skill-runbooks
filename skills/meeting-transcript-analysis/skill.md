---
id: meeting.transcript.analysis
name: Análisis de transcripts de reuniones
version: 1.0.0
status: stable
category: meetings
tags:
  - teams
  - transcript
  - reuniones
  - resumen
  - compromisos
  - requerimientos
  - issues
input_types:
  - text
  - file
  - txt
  - docx
  - pdf
  - vtt
  - csv
output_formats:
  - markdown
llm_compatibility:
  - generic-llm
  - ChatGPT
  - Claude
  - Gemini
  - Copilot
---

# Skill: Análisis de transcripts de reuniones

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

Ver `input.schema.md`.

## Salida esperada

Ver `output.schema.md`.

## Prompts disponibles

| Archivo | Uso |
|---|---|
| `prompt.full.md` | Análisis completo. |
| `prompt.quick.md` | Análisis rápido. |
| `prompt.file-input.md` | Transcript adjunto como archivo. |
| `prompt.multi-transcript.md` | Varios transcripts. |
| `prompt.chunked-long-transcript.md` | Transcript muy largo dividido en partes. |

## Criterios de calidad

Ver `evals/checklist.md`.

## Mantenimiento

- Cambios menores de redacción: patch.
- Nuevas secciones compatibles: minor.
- Cambio en estructura obligatoria: major.
