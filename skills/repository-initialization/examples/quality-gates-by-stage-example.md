# Ejemplo: quality gates por stage

Este archivo ayuda a decidir qué validar en `pre-commit`, `pre-push`, Pull Request/CI y release.

## Regla principal

Mientras más temprano se ejecuta un gate, más rápido y barato debe ser.

## `pre-commit`

Usar para validaciones rápidas sobre cambios locales.

Candidatos:

- Formato.
- Lint rápido.
- Imports.
- Espacios finales.
- Fin de archivo.
- Secretos obvios.
- Markdown básico.

Evitar:

- Pruebas lentas.
- E2E.
- Builds completos.
- Validaciones que dependan de infraestructura externa.

## `pre-push`

Usar para validaciones moderadas antes de subir cambios.

Candidatos:

- Unit tests rápidos.
- Typecheck.
- Build parcial.
- Validación de paquetes afectados.

Evitar:

- Suites completas demasiado lentas.
- E2E extensivos.
- Validaciones que bloqueen demasiado el flujo local.

## Pull Request / CI

Usar como fuente de verdad antes del merge.

Candidatos:

- Build completo.
- Unit tests.
- Integration tests.
- API tests.
- Architecture tests.
- Coverage.
- Security checks.
- Lint completo.
- Validación documental y registry.

## Release

Usar para validaciones finales antes de publicar.

Candidatos:

- Smoke tests.
- Build de release.
- Versionado.
- Seguridad.
- Artefactos.
- Validación de configuración.

## Recomendación

No confiar solo en hooks locales. Los hooks ayudan, pero CI debe ser obligatorio para proteger la rama principal.
