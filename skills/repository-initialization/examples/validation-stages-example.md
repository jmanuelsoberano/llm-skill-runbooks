# Ejemplo: stages de validación

Este archivo ayuda a decidir cuándo ejecutar cada validación.

## Stages

| Stage | Uso recomendado |
|---|---|
| `pre-commit` | Validaciones rápidas antes del commit. |
| `pre-push` | Validaciones moderadas antes de subir cambios. |
| `pull-request` | Validaciones completas antes de merge. |
| `release` | Validaciones finales antes de publicar. |

## Reglas

- Mientras más temprano sea el stage, más rápida debe ser la validación.
- Las validaciones locales ayudan, pero CI debe proteger la rama principal.
- Evitar pruebas lentas antes del commit.
- Usar Pull Request/CI para build completo, integración, arquitectura y seguridad.
