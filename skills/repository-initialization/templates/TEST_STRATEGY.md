# Estrategia de Pruebas

Este documento define qué tipos de pruebas aplican al repositorio, cuáles no aplican por ahora y cómo debe evolucionar la estrategia.

## Propósito

Evitar que las pruebas se agreguen de forma improvisada. Este archivo debe guiar a personas y LLMs antes de crear, modificar o reorganizar pruebas.

## Perfil de pruebas seleccionado

Seleccionar uno:

- `no-code-validation`
- `unit-only`
- `unit-plus-integration`
- `layered-testing`
- `frontend-component-testing`
- `api-contract-testing`
- `e2e-critical-flows`
- `full-quality-gate`
- `custom`

Perfil elegido:

```text
Pendiente de definir
```

## Motivo del perfil elegido

Explica por qué este perfil es suficiente para el estado actual del repositorio.

```text
Pendiente de definir
```

## Matriz de tipos de pruebas

| Tipo de prueba | Aplica | Motivo | Ubicación sugerida | Estado |
|---|---|---|---|---|
| Validación documental | Pendiente | Repos con docs, prompts o Markdown | `evals/`, `docs/`, `scripts/` | Pendiente |
| Unitarias | Pendiente | Lógica aislada, dominio, utilidades | `tests/unit/` | Pendiente |
| Integración | Pendiente | DB, archivos, servicios, framework | `tests/integration/` | Pendiente |
| API | Pendiente | Endpoints, controladores, rutas | `tests/api/` | Pendiente |
| Contrato | Pendiente | APIs consumidas por terceros | `tests/contracts/` | Pendiente |
| Componentes UI | Pendiente | Componentes, hooks, servicios cliente | `tests/components/` | Pendiente |
| E2E | Pendiente | Flujos críticos de usuario | `tests/e2e/` | Pendiente |
| Seguridad | Pendiente | Auth, permisos, datos sensibles | `tests/security/` | Pendiente |
| Performance | Pendiente | Rendimiento o carga crítica | `tests/performance/` | Pendiente |

## Criterios mínimos iniciales

- No agregar pruebas sin saber qué perfil aplica.
- No crear carpetas vacías de pruebas si no hay una necesidad clara.
- Priorizar pruebas unitarias para lógica de negocio aislada.
- Usar pruebas de integración para dependencias reales o simuladas con infraestructura.
- Usar E2E solo para flujos críticos, no para todo.
- Documentar cambios relevantes de estrategia en `DECISIONS.md`.

## Herramientas sugeridas

Completar según stack:

| Stack | Herramientas candidatas | Estado |
|---|---|---|
| .NET | MSTest, xUnit, NUnit, WebApplicationFactory | Pendiente |
| Django / Python | unittest, pytest, Django TestCase | Pendiente |
| Angular | Vitest, Jasmine, Testing Library, Playwright | Pendiente |
| React / TypeScript | Vitest, Jest, Testing Library, Playwright | Pendiente |
| Node.js | Vitest, Jest, Supertest | Pendiente |
| Markdown / Docs | markdownlint, link checkers, scripts custom | Pendiente |

## Qué no se probará al inicio

Lista de pruebas o validaciones que no se implementarán en la fase inicial.

- Pendiente de definir.

## Riesgos de pruebas insuficientes

- Pendiente de definir.

## Decisiones relacionadas

Registrar en `DECISIONS.md` cualquier decisión relevante, por ejemplo:

- adoptar un framework de pruebas;
- excluir E2E por costo inicial;
- definir umbrales de cobertura;
- usar base de datos real, en memoria o contenedor;
- separar pruebas por capa, módulo o feature.

## Reglas para LLMs

Antes de crear o modificar pruebas:

1. Leer este archivo.
2. Confirmar el perfil de pruebas seleccionado.
3. No agregar un nuevo tipo de prueba sin actualizar este documento.
4. No agregar herramientas nuevas sin registrar la decisión.
5. Sugerir cambios proporcionales al tamaño y riesgo del proyecto.
