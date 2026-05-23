# Input schema

## Entrada mínima

| Campo | Requerido | Descripción |
|---|---:|---|
| tipo_repositorio | Sí | Código, documentación, aplicación, seguimiento, investigación, prompts, skills o mixto. |
| proposito | Sí | Para qué existirá el repositorio. |
| audiencia | No | Quién lo usará o mantendrá. |
| contenido_inicial | No | Archivos, notas o contexto ya disponible. |
| tecnologias | No | Lenguajes, frameworks o herramientas relacionadas. |
| restricciones | No | Límites, reglas o cosas que no deben incluirse. |
| nivel_formalidad | No | Ligero, medio o formal. |

## Formatos aceptados

- Texto libre.
- Markdown.
- Lista de requisitos.
- Contexto adjunto.
- Descripción conversacional.

## Manejo de faltantes

Si falta información crítica, la salida debe marcarla como `Pendiente de definir` o pedir aclaración mínima.
