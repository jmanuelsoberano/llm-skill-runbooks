# Output schema

## Salida esperada

La skill debe producir una propuesta de inicialización en Markdown, lista para convertirse en estructura de repositorio, documentos base, estrategia de pruebas o tareas de arranque.

## Secciones obligatorias

1. `Resumen del repositorio`
2. `Tipo de repositorio identificado`
3. `Patrón estructural recomendado`
4. `Perfil de pruebas recomendado`
5. `Supuestos e incertidumbres`
6. `Estructura propuesta`
7. `Archivos base sugeridos`
8. `Estrategia de pruebas inicial`
9. `Decisiones iniciales recomendadas`
10. `Checklist de arranque`
11. `Primer commit sugerido`
12. `Siguientes pasos`

## Patrones estructurales permitidos

- `docs-only`
- `code-library`
- `split-frontend-backend`
- `single-src-layered`
- `framework-native`
- `monorepo-workspace`
- `prompt-skill-repo`
- `mixed`

## Perfiles de pruebas permitidos

- `no-code-validation`
- `unit-only`
- `unit-plus-integration`
- `layered-testing`
- `frontend-component-testing`
- `api-contract-testing`
- `e2e-critical-flows`
- `full-quality-gate`
- `custom`

## Secciones opcionales

- `Riesgos o puntos de cuidado`
- `Carpetas que conviene evitar por ahora`
- `Automatizaciones futuras`
- `Plantillas recomendadas`
- `Notas para LLMs futuros`

## Valores de incertidumbre

Usar estos valores cuando aplique:

- `Pendiente de definir`
- `Ambiguo`
- `Requiere confirmación`
- `Inferencia`

## Reglas de salida

- No inventar información como si fuera confirmada.
- Separar hechos, inferencias y pendientes.
- No recomendar estructuras excesivas si el repositorio es pequeño.
- No forzar `frontend/` y `backend/` si el patrón adecuado es `single-src-layered`, `framework-native` o `monorepo-workspace`.
- No proponer todos los tipos de pruebas si el repositorio no los necesita.
- No crear una estrategia de pruebas más pesada que el riesgo real del proyecto.
- No mezclar decisiones tomadas con decisiones sugeridas.
- No incluir secretos o datos sensibles.
- Sugerir nombres de archivos claros y consistentes.

## Formato del primer commit

Incluir un mensaje sugerido, por ejemplo:

```bash
git add .
git commit -m "Initial repository structure"
git push
```

## Calidad esperada

La salida debe ser:

- clara;
- accionable;
- reutilizable;
- compatible con Git;
- fácil de mantener por humanos y LLMs.
