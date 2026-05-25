# Ejemplo: perfiles de validación

Este archivo ayuda a elegir un nivel inicial de validaciones automáticas.

## Perfiles

| Perfil | Uso recomendado |
|---|---|
| `no-code-quality-gate` | Repos de documentación, prompts, skills o runbooks. |
| `format-only` | Repos pequeños o iniciales. |
| `format-and-lint` | Repos con código que requieren formato y estilo. |
| `format-lint-test` | Repos con código productivo y pruebas rápidas. |
| `layered-quality-gate` | Apps por capas con reglas de arquitectura. |
| `full-quality-gate` | Sistemas productivos o críticos con validaciones completas. |
| `custom` | Repos mixtos o con restricciones particulares. |

## Regla

El perfil debe ser proporcional al riesgo del proyecto y al costo de mantenimiento.
