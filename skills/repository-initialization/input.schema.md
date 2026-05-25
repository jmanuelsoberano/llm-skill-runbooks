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
| criticidad | No | Nivel de riesgo del repositorio o sistema. | `baja`, `media`, `alta` |
| dependencias_externas | No | DB, APIs, archivos, colas, servicios externos o infraestructura. | `SQL Server, API externa` |
| requiere_ui | No | Indica si hay interfaz de usuario significativa. | `sí, Angular` |
| requiere_api | No | Indica si expone endpoints o contratos consumidos por otros. | `sí, REST API` |
| estrategia_pruebas_deseada | No | Perfil de pruebas esperado si ya se conoce. | `layered-testing` |
| restricciones_pruebas | No | Restricciones para pruebas, mocks, BD, CI o herramientas. | `evitar mocks; usar BD en memoria` |
| quality_gates_deseados | No | Perfil de validaciones automáticas esperado si ya se conoce. | `format-lint-test` |
| herramientas_calidad | No | Herramientas de formato, lint, hooks, CI o análisis ya preferidas. | `pre-commit, ESLint, dotnet format` |
| restricciones_quality_gates | No | Restricciones para hooks, CI, tiempos de ejecución o herramientas. | `no correr E2E en pre-commit` |

## Formatos aceptados

- Texto libre.
- Markdown.
- Lista de requisitos.
- Contexto adjunto.
- Descripción conversacional.
- Árbol de carpetas existente.
- Notas sobre riesgos, dependencias o pruebas esperadas.
- Notas sobre hooks, CI, linters, formato o reglas de arquitectura.

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

## Descubrimiento de pruebas

Cuando no se indique estrategia de pruebas, inferir un perfil inicial usando:

- tipo de repositorio;
- patrón estructural;
- stack tecnológico;
- criticidad;
- presencia de UI;
- presencia de API;
- dependencias externas;
- necesidades de CI/CD;
- restricciones del usuario.

## Descubrimiento de quality gates

Cuando no se indiquen quality gates, inferir un perfil inicial usando:

- stack tecnológico;
- perfil de pruebas;
- patrón estructural;
- criticidad;
- herramientas conocidas del ecosistema;
- necesidad de hooks locales;
- necesidad de validaciones en PR/CI;
- reglas de arquitectura o seguridad esperadas;
- restricciones de tiempo para `pre-commit` y `pre-push`.
