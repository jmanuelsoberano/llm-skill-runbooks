# Input schema

## Tipos de entrada aceptados

La skill acepta:

1. Transcript pegado como texto.
2. Archivo adjunto con transcript.
3. Varias partes de un transcript largo.
4. Varios transcripts de reuniones relacionadas.

## Formatos sugeridos

- `.txt`
- `.docx`
- `.pdf`
- `.vtt`
- `.csv`
- texto pegado directamente
- exportación de Microsoft Teams

## Contexto opcional

El usuario puede proporcionar:

| Campo | Obligatorio | Descripción |
|---|---:|---|
| `meeting_date` | No | Fecha de la reunión. |
| `project` | No | Proyecto relacionado. |
| `client` | No | Cliente o área. |
| `repo_url` | No | Repositorio asociado. |
| `objective` | No | Objetivo esperado de la reunión. |
| `participants_expected` | No | Participantes esperados. |
| `desired_depth` | No | rápido, normal, profundo. |
| `output_language` | No | Idioma de salida. |

## Reglas de entrada

- Si el archivo no puede leerse, la salida debe indicarlo.
- Si el transcript parece incompleto, se debe marcar.
- Si faltan nombres o roles, usar `No especificado`.
- Si hay timestamps, usarlos como evidencia cuando ayuden.
- Si el transcript tiene ruido de transcripción automática, se debe limpiar mentalmente sin inventar.
