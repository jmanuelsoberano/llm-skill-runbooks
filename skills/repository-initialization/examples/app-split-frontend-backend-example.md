# Ejemplo: aplicación con frontend y backend separados

## Patrón

`split-frontend-backend`

## Cuándo usar este patrón

Úsalo cuando el frontend y el backend son proyectos claramente separados, con dependencias, builds, pruebas o despliegues independientes.

Ejemplos comunes:

- Angular + .NET API.
- React + Node API.
- Vue + Django REST API.
- Frontend estático + backend de servicios.

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
| `frontend/` | Aplicación cliente, interfaz o SPA. |
| `backend/` | API, servicios, lógica de servidor o acceso a datos. |
| `docs/` | Documentación funcional, técnica o de arquitectura. |
| `tests/` | Pruebas transversales o de integración. |
| `scripts/` | Scripts de build, despliegue o mantenimiento. |

## Señales de que este patrón aplica

- Frontend y backend tienen comandos de ejecución separados.
- Cada parte tiene dependencias propias.
- Pueden desplegarse de forma independiente.
- Equipos distintos podrían trabajar en cada parte.

## Señales de que NO aplica

- El frontend vive como una capa interna del backend.
- El framework ya define una estructura integrada.
- Todo el producto se compila o despliega como una sola unidad.

## Notas de mantenimiento

- Documentar cómo ejecutar frontend y backend por separado.
- Mantener `.env.example` para cada parte si aplica.
- Evitar duplicar documentación entre `frontend/` y `backend/`.
- Registrar decisiones de integración en `DECISIONS.md`.
