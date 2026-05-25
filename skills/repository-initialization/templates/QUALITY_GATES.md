# Quality Gates

Este documento define qué validaciones automáticas debe cumplir el repositorio antes de aceptar cambios.

## Propósito

Establecer guardrails técnicos para reducir errores, mantener consistencia y evitar que entren cambios que no cumplen criterios mínimos de calidad.

Los quality gates pueden ejecutarse localmente, antes de hacer commit o push, y también en Pull Requests mediante CI.

## Perfil seleccionado

Seleccionar uno:

- `no-code-quality-gate`
- `format-only`
- `format-and-lint`
- `format-lint-test`
- `layered-quality-gate`
- `full-quality-gate`
- `custom`

Perfil elegido:

```text
Pendiente de definir
```

## Momentos de validación

| Momento | Aplica | Qué valida | Debe bloquear |
|---|---|---|---|
| `pre-commit` | Pendiente | Formato, lint rápido, imports, whitespace, secretos obvios | Commit |
| `pre-push` | Pendiente | Pruebas rápidas, typecheck, build parcial | Push |
| `pull-request` | Pendiente | Pruebas completas, integración, arquitectura, cobertura, seguridad | Merge |
| `release` | Pendiente | Build final, smoke tests, seguridad, versionado | Release |

## Categorías de validación

| Categoría | Aplica | Herramienta sugerida | Stage recomendado | Estado |
|---|---|---|---|---|
| Formato | Pendiente | Según stack | `pre-commit` | Pendiente |
| Lint | Pendiente | Según stack | `pre-commit` / CI | Pendiente |
| Imports | Pendiente | Según stack | `pre-commit` | Pendiente |
| Typecheck | Pendiente | Según stack | `pre-push` / CI | Pendiente |
| Unit tests | Pendiente | Según stack | `pre-push` / CI | Pendiente |
| Integration tests | Pendiente | Según stack | CI | Pendiente |
| Architecture rules | Pendiente | Según stack | CI | Pendiente |
| Security checks | Pendiente | Según stack | CI | Pendiente |
| Coverage | Pendiente | Según stack | CI | Pendiente |
| Docs validation | Pendiente | Markdown tools | `pre-commit` / CI | Pendiente |

## Reglas generales

- Los hooks locales ayudan, pero CI debe ser la fuente de verdad.
- No todos los proyectos necesitan todos los gates.
- No ejecutar validaciones lentas en `pre-commit`.
- No bloquear commits por pruebas pesadas.
- Usar `pre-push` para pruebas rápidas o typecheck cuando aplique.
- Usar CI para validaciones completas y obligatorias antes del merge.
- Registrar decisiones relevantes en `DECISIONS.md`.

## Reglas para LLMs

Antes de agregar herramientas, hooks o validaciones:

1. Leer este archivo.
2. Revisar `TEST_STRATEGY.md` si existe.
3. No agregar gates nuevos sin justificar el motivo.
4. No agregar herramientas específicas sin considerar el stack.
5. No convertir todos los gates en obligatorios si el proyecto no lo necesita.
6. Mantener los cambios incrementales y documentados.
