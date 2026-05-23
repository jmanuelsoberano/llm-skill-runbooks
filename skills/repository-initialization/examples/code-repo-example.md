# Ejemplo: repositorio de código

## Tipo

Código, librería, servicio pequeño o aplicación con una sola base técnica.

## Cuándo usar esta estructura

Úsala cuando el repositorio tenga código fuente, pruebas y documentación técnica básica.

## Estructura posible

```text
.
├─ src/
├─ tests/
├─ docs/
├─ scripts/
├─ README.md
├─ PROJECT_CONTEXT.md
├─ LLM_GUIDE.md
├─ STRUCTURE.md
├─ DECISIONS.md
├─ CHANGELOG.md
└─ TODO.md
```

## Propósito de carpetas

| Ruta | Propósito |
|---|---|
| `src/` | Código fuente principal. |
| `tests/` | Pruebas automatizadas o manuales. |
| `docs/` | Documentación técnica y funcional. |
| `scripts/` | Scripts de apoyo, validación o mantenimiento. |

## Notas de mantenimiento

- Documentar instrucciones de ejecución en `README.md`.
- Registrar decisiones técnicas relevantes en `DECISIONS.md`.
- Mantener cambios importantes en `CHANGELOG.md`.
- Evitar guardar secretos o archivos generados.
- Agregar carpetas nuevas solo cuando tengan un propósito claro.
