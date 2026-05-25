# Extensión: Quality Gates

Esta extensión amplía `repository.initialization` para descubrir validaciones automáticas del repositorio.

## Objetivo

Definir qué debe validarse antes de aceptar cambios en el repositorio, sin imponer herramientas innecesarias ni sobrecargar el flujo local.

## Perfiles soportados

| Perfil | Uso recomendado |
|---|---|
| `no-code-quality-gate` | Repos de documentación, prompts, skills o runbooks. |
| `format-only` | Repos iniciales o muy pequeños. |
| `format-and-lint` | Repos con código que requieren formato y reglas de estilo. |
| `format-lint-test` | Repos con código productivo y pruebas rápidas. |
| `layered-quality-gate` | Apps por capas con reglas de arquitectura. |
| `full-quality-gate` | Sistemas productivos o críticos con validaciones completas en CI. |
| `custom` | Repos mixtos o con restricciones particulares. |

## Flujo de descubrimiento

Al inicializar un repositorio, el agente debe identificar:

1. Stack tecnológico.
2. Patrón estructural.
3. Perfil de pruebas.
4. Criticidad del sistema.
5. Dependencias externas.
6. Si hay UI, API o contratos.
7. Qué validaciones deben correr en `pre-commit`.
8. Qué validaciones deben correr en `pre-push`.
9. Qué validaciones deben correr en PR/CI.
10. Qué validaciones quedan para release.

## Reglas de diseño

- `pre-commit` debe ser rápido.
- `pre-push` puede ser moderado.
- CI debe ser la fuente de verdad.
- No ejecutar todo en hooks locales.
- No imponer herramientas sin considerar stack.
- No agregar validaciones lentas sin justificación.
- Documentar decisiones en `DECISIONS.md`.

## Documentos relacionados

- `templates/QUALITY_GATES.md`
- `examples/quality-gates-by-stack-example.md`
- `examples/quality-gates-by-stage-example.md`
- `templates/TEST_STRATEGY.md`
- `evals/checklist.md`
