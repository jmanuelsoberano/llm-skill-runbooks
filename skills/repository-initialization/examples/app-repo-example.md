# Ejemplo: repositorio de aplicación

## Tipo

Aplicación web, móvil, escritorio o sistema con varias capas.

## Cuándo usar esta estructura

Úsala cuando el repositorio incluya frontend, backend, documentación, pruebas o scripts de soporte.

## Estructura posible

```text
.
├─ frontend/
├─ backend/
├─ docs/
├─ tests/
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
| `frontend/` | Interfaz de usuario o cliente. |
| `backend/` | API, servicios o lógica de servidor. |
| `docs/` | Documentación técnica, funcional o de arquitectura. |
| `tests/` | Pruebas automatizadas, manuales o casos de validación. |
| `scripts/` | Scripts de build, despliegue, validación o mantenimiento. |

## Notas de mantenimiento

- Separar frontend y backend solo si realmente existen ambas capas.
- Documentar variables de entorno sin incluir secretos.
- Registrar decisiones de arquitectura en `DECISIONS.md`.
- Mantener instrucciones de ejecución actualizadas en `README.md`.
- Evitar subir artefactos generados como `dist/`, `build/` o dependencias instaladas.
