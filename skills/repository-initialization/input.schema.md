# Input schema

## Entrada mínima

| Campo | Requerido | Descripción | Ejemplo |
|---|---:|---|---|
| tipo_repositorio | Sí | Código, documentación, aplicación, seguimiento, investigación, prompts, skills o mixto. | `documentación` |
| proposito | Sí | Para qué existirá el repositorio. | `Versionar documentos y prompts reutilizables` |
| audiencia | No | Quién lo usará, mantendrá o revisará. | `yo, equipo, LLMs` |
| contenido_inicial | No | Archivos, notas, carpetas o contexto ya disponible. | `documentos Markdown existentes` |
| tecnologias | No | Lenguajes, frameworks, herramientas o plataformas relacionadas. | `GitHub, Markdown, Python` |
| restricciones | No | Límites, reglas o cosas que no deben incluirse. | `no guardar secretos` |
| nivel_formalidad | No | Ligero, medio o formal. | `medio` |
| visibilidad | No | Público, privado, interno o equipo. | `privado` |
| estrategia_versionado | No | Cómo se espera versionar cambios. | `commits pequeños y changelog` |

## Formatos aceptados

- Texto libre.
- Markdown.
- Lista de requisitos.
- Contexto adjunto.
- Descripción conversacional.
- Árbol de carpetas existente.

## Información sensible

La entrada no debe incluir:

- contraseñas;
- tokens;
- llaves privadas;
- secretos de despliegue;
- datos personales innecesarios.

## Manejo de faltantes

Si falta información crítica, la salida debe:

1. marcarla como `Pendiente de definir`, `Ambiguo` o `Requiere confirmación`;
2. hacer solo las preguntas mínimas necesarias;
3. continuar con una propuesta razonable cuando no bloquee el avance.

## Supuestos permitidos

Solo se permiten supuestos explícitos y etiquetados como `Inferencia`.
