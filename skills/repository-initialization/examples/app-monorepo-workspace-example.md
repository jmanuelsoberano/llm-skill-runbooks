# Ejemplo: monorepo o workspace

## Patrón

`monorepo-workspace`

## Cuándo usar este patrón

Úsalo cuando un mismo repositorio contiene varias aplicaciones, paquetes, librerías o módulos reutilizables.

## Estructura posible

```text
.
├─ apps/
│  ├─ web/
│  └─ api/
├─ libs/
│  ├─ shared/
│  └─ domain/
├─ packages/
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

## Variante tipo workspace Angular

```text
.
├─ projects/
│  ├─ admin-app/
│  ├─ student-app/
│  └─ shared-ui/
├─ src/
├─ angular.json
└─ docs/
```

## Propósito de carpetas

| Ruta | Propósito |
|---|---|
| `apps/` | Aplicaciones ejecutables. |
| `libs/` | Librerías internas del dominio o de UI. |
| `packages/` | Paquetes reutilizables o publicables. |
| `docs/` | Documentación transversal. |
| `scripts/` | Automatizaciones comunes del repositorio. |

## Señales de que este patrón aplica

- Hay más de una aplicación en el mismo repositorio.
- Existen librerías compartidas entre aplicaciones.
- Se requiere coordinación de versiones o builds dentro de un mismo workspace.
- El repositorio representa un producto o ecosistema, no una sola app aislada.

## Notas de mantenimiento

- Documentar límites entre apps y librerías.
- Evitar dependencias circulares.
- Mantener scripts comunes en una ubicación clara.
- Registrar decisiones sobre nombres, ownership y versionado.
