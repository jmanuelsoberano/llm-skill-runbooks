# Ejemplo: estrategia de pruebas por patrón estructural

Este archivo ayuda a conectar el patrón estructural del repositorio con una estrategia inicial de pruebas.

## `docs-only`

Perfil recomendado: `no-code-validation`.

Estrategia:

- Validar estructura documental.
- Validar Markdown y enlaces.
- Revisar ejemplos y checklists.
- No crear carpetas de pruebas de aplicación.

## `code-library`

Perfil recomendado: `unit-only` o `unit-plus-integration`.

Estrategia:

- Unitarias para API pública de la librería.
- Casos borde y errores esperados.
- Integración solo si hay archivos, red, DB o servicios externos.

## `split-frontend-backend`

Perfil recomendado: combinación de `frontend-component-testing` y `unit-plus-integration`.

Estrategia:

- Frontend: componentes, servicios cliente, rutas e interacción.
- Backend: lógica de aplicación, integración con DB/API y endpoints.
- E2E solo para flujos críticos entre frontend y backend.

## `single-src-layered`

Perfil recomendado: `layered-testing`.

Estrategia:

- Dominio: unitarias aisladas.
- Aplicación: casos de uso o servicios.
- Infraestructura: integración con DB, archivos o servicios.
- Presentación/API/UI: escenarios principales.

## `framework-native`

Perfil recomendado: depende del framework.

Estrategia:

- Respetar herramientas del ecosistema.
- Django: tests con `TestCase` o pytest según convención del proyecto.
- Angular/React: componentes, servicios cliente y flujos relevantes.
- .NET: unitarias e integración con herramientas del stack.

## `monorepo-workspace`

Perfil recomendado: `custom` o `full-quality-gate`.

Estrategia:

- Definir pruebas por app, paquete o librería.
- Agregar validaciones transversales de workspace.
- Evitar que todas las apps ejecuten pruebas innecesarias.
- Documentar ownership y límites entre módulos.

## `prompt-skill-repo`

Perfil recomendado: `no-code-validation`.

Estrategia:

- Validar prompts contra ejemplos.
- Validar contratos de entrada/salida.
- Validar checklist de calidad.
- Validar estructura de carpetas y registro de skills.

## `mixed`

Perfil recomendado: `custom`.

Estrategia:

- Separar qué aplica a cada parte del repositorio.
- Documentar explícitamente qué pruebas sí aplican y cuáles no.
- Evitar copiar una estrategia de una parte a todo el repositorio.
