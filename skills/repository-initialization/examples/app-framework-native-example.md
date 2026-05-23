# Ejemplo: aplicación con estructura nativa del framework

## Patrón

`framework-native`

## Cuándo usar este patrón

Úsalo cuando el framework ya propone una estructura clara mediante documentación oficial, CLI o convenciones ampliamente adoptadas.

La regla principal es: respeta la estructura del framework salvo que tengas una razón fuerte y documentada para cambiarla.

## Ejemplo Django

```text
.
├─ manage.py
├─ config/
├─ apps/
│  ├─ users/
│  ├─ reports/
│  └─ billing/
├─ templates/
├─ static/
├─ tests/
└─ docs/
```

## Ejemplo Angular

```text
.
├─ src/
│  ├─ app/
│  ├─ assets/
│  └─ environments/
├─ angular.json
├─ package.json
└─ docs/
```

## Ejemplo React / Next.js

```text
.
├─ app/
├─ components/
├─ lib/
├─ public/
├─ package.json
└─ docs/
```

## Ejemplo .NET simple

```text
.
├─ src/
│  └─ MyApp.Web/
├─ tests/
├─ MyApp.sln
└─ docs/
```

## Señales de que este patrón aplica

- El proyecto fue creado con una CLI oficial o plantilla del framework.
- El equipo espera seguir convenciones conocidas del ecosistema.
- Cambiar la estructura dificultaría documentación, onboarding o mantenimiento.
- El framework define rutas, assets, módulos o apps de forma específica.

## Notas de mantenimiento

- Documentar qué estructura proviene del framework.
- No mover carpetas generadas por CLI sin una decisión registrada.
- Agregar carpetas propias alrededor de la estructura nativa, no contra ella.
- Registrar desviaciones en `DECISIONS.md`.
