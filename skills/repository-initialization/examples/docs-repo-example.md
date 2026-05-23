# Ejemplo: repositorio de documentación

## Tipo

Documentación versionada, base de conocimiento, guías, runbooks o material de referencia.

## Cuándo usar esta estructura

Úsala cuando el valor principal del repositorio sean documentos y no código ejecutable.

## Estructura posible

```text
.
├─ docs/
│  ├─ active/
│  ├─ archive/
│  └─ references/
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
| `docs/active/` | Documentos vigentes o en uso. |
| `docs/archive/` | Documentos históricos que no deben perderse. |
| `docs/references/` | Material fuente, enlaces, notas o referencias. |

## Notas de mantenimiento

- No borrar documentos antiguos sin razón clara; moverlos a `archive/` si conservan valor histórico.
- Mantener documentos activos separados de referencias.
- Registrar cambios relevantes en `CHANGELOG.md`.
- Registrar decisiones de organización en `DECISIONS.md`.
- Evitar duplicar el mismo documento en varias carpetas.
