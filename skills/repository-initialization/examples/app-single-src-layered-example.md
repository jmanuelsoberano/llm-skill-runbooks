# Ejemplo: aplicación con `src/` y capas internas

## Patrón

`single-src-layered`

## Cuándo usar este patrón

Úsalo cuando la aplicación vive principalmente bajo una carpeta `src/` y dentro se organizan capas, módulos o componentes del sistema.

Este patrón es útil cuando frontend, backend, dominio, infraestructura o presentación forman parte de un mismo producto y no conviene separarlos como proyectos raíz independientes.

## Estructura posible

```text
.
├─ src/
│  ├─ domain/
│  ├─ application/
│  ├─ infrastructure/
│  ├─ presentation/
│  └─ web/
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

## Variante común en .NET

```text
.
├─ src/
│  ├─ Project.Domain/
│  ├─ Project.Application/
│  ├─ Project.Infrastructure/
│  └─ Project.Web/
├─ tests/
└─ docs/
```

## Variante con frontend integrado

```text
.
├─ src/
│  ├─ core/
│  ├─ services/
│  ├─ infrastructure/
│  └─ ui/
├─ tests/
└─ docs/
```

## Señales de que este patrón aplica

- Existe una carpeta `src/` como raíz del producto.
- Las capas internas representan responsabilidades técnicas o de negocio.
- El frontend es una capa o módulo, no un proyecto raíz separado.
- La aplicación se despliega como una unidad o con fuerte acoplamiento interno.

## Notas de mantenimiento

- Nombrar capas por responsabilidad, no por moda.
- Evitar crear capas vacías.
- Documentar dependencias permitidas entre capas.
- Registrar decisiones arquitectónicas en `DECISIONS.md`.
