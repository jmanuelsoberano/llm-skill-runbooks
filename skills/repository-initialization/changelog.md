# Changelog

## 0.3.0 - Descubrimiento de estrategia de pruebas

### Added

- Descubrimiento explícito del perfil inicial de pruebas durante la inicialización del repositorio.
- Perfiles de pruebas soportados: `no-code-validation`, `unit-only`, `unit-plus-integration`, `layered-testing`, `frontend-component-testing`, `api-contract-testing`, `e2e-critical-flows`, `full-quality-gate` y `custom`.
- Plantilla `TEST_STRATEGY.md` para documentar estrategia de pruebas, tipos aplicables, herramientas candidatas, exclusiones y reglas para LLMs.
- Campos de entrada para criticidad, dependencias externas, UI, API, preferencias y restricciones de pruebas.

### Improved

- El contrato de salida ahora exige `Perfil de pruebas recomendado` y `Estrategia de pruebas inicial`.
- Los prompts ahora piden descubrir la estrategia de pruebas como parte del flujo guiado.
- La checklist ahora valida proporcionalidad de pruebas y evita proponer todos los tipos por default.
- `LLM_GUIDE.md` ahora indica revisar `TEST_STRATEGY.md` antes de crear o modificar pruebas.
- `registry.yaml` actualiza la skill a `0.3.0` y agrega el tag `pruebas`.

---

## 0.2.0 - Patrones de estructura de aplicaciones

### Added

- Clasificación explícita por patrón estructural antes de proponer carpetas.
- Patrones soportados: `docs-only`, `code-library`, `split-frontend-backend`, `single-src-layered`, `framework-native`, `monorepo-workspace`, `prompt-skill-repo` y `mixed`.
- Ejemplo para aplicaciones con frontend y backend separados.
- Ejemplo para aplicaciones con `src/` y capas internas.
- Ejemplo para aplicaciones que respetan la estructura nativa del framework.
- Ejemplo para monorepos o workspaces.

### Improved

- El prompt completo ahora pide clasificar el patrón estructural y justificarlo.
- El prompt rápido ahora incluye patrón estructural recomendado.
- El prompt con contexto adjunto ahora infiere el patrón a partir de archivos o árbol existente.
- El contrato de salida ahora exige `Patrón estructural recomendado`.
- La checklist ahora valida que no se fuerce `frontend/` y `backend/` cuando no corresponde.

---

## 0.1.0 - Draft inicial

### Added

- Definición inicial de la skill `repository.initialization`.
- Metadata compatible con el registro del repositorio.
- Contratos de entrada y salida.
- Prompt completo para inicialización guiada.
- Prompt rápido para inicialización mínima.
- Prompt para trabajar con archivos o contexto adjunto.
- Plantillas base para `README.md`, contexto, estructura, decisiones, changelog, TODO y guía para LLMs.
- Plantilla de referencia para `.gitignore`.
- Ejemplos para repositorios de código, documentación y aplicación.
- Checklist de evaluación.

### Improved

- Se ampliaron las plantillas base para reducir ambigüedad.
- Se fortalecieron reglas de manejo de incertidumbre.
- Se agregaron recomendaciones de trazabilidad y seguridad.
- Se mejoraron ejemplos con propósito, estructura y notas de mantenimiento.
- Se alineó el prompt rápido con el contrato de salida de la skill.

### Removed

- Se eliminó el archivo temporal `.gitkeep` usado para crear la carpeta inicial.
