# Ejemplo: perfiles de pruebas

Este archivo muestra cómo elegir un perfil inicial de pruebas sin sobreingeniería.

## Regla general

El perfil de pruebas debe responder a cuatro preguntas:

1. ¿Hay código productivo?
2. ¿Hay dependencias externas?
3. ¿Hay UI o API relevante?
4. ¿Qué tan crítico es el sistema?

## Perfiles

| Perfil | Pruebas iniciales | Cuándo escalar |
|---|---|---|
| `no-code-validation` | Markdown, links, ejemplos, checklist manual | Cuando aparezca código productivo. |
| `unit-only` | Unitarias para lógica aislada | Cuando aparezcan DB, API, archivos o servicios. |
| `unit-plus-integration` | Unitarias + integración con dependencias clave | Cuando existan capas claras o flujos críticos. |
| `layered-testing` | Unitarias por dominio + integración por infraestructura + API/UI según aplique | Cuando el sistema sea crítico o tenga varios consumidores. |
| `frontend-component-testing` | Componentes, servicios cliente, rutas, hooks | Cuando haya flujos de usuario críticos. |
| `api-contract-testing` | API tests + contrato + compatibilidad | Cuando existan consumidores externos. |
| `e2e-critical-flows` | E2E solo para flujos clave | Cuando el flujo sea negocio crítico. |
| `full-quality-gate` | Unit, integration, API, component, E2E y checks CI | Cuando el sistema sea productivo o crítico. |
| `custom` | Combinación justificada | Cuando el repo mezcle patrones. |

## Ejemplos rápidos

### Repo de documentación

Perfil recomendado: `no-code-validation`.

Validar:

- estructura de carpetas;
- Markdown;
- enlaces;
- ejemplos de entrada/salida;
- checklist manual.

### Librería pequeña

Perfil recomendado: `unit-only`.

Validar:

- funciones públicas;
- casos borde;
- errores esperados;
- serialización o formatos si aplica.

### Aplicación con base de datos

Perfil recomendado: `unit-plus-integration`.

Validar:

- lógica de dominio con unitarias;
- repositorios o queries con integración;
- servicios críticos;
- configuración mínima de ambiente de pruebas.

### Aplicación por capas

Perfil recomendado: `layered-testing`.

Validar:

- dominio de forma aislada;
- casos de uso o servicios de aplicación;
- infraestructura con integración;
- API o presentación en escenarios principales.

### Frontend con interacción importante

Perfil recomendado: `frontend-component-testing`.

Validar:

- componentes;
- estados;
- servicios cliente;
- rutas;
- interacciones de usuario críticas.

### API consumida por terceros

Perfil recomendado: `api-contract-testing`.

Validar:

- endpoints;
- contratos;
- errores estándar;
- compatibilidad hacia atrás;
- ejemplos de request/response.
