# Output schema

## Salida esperada

La skill debe producir una propuesta de inicialización en Markdown, lista para convertirse en estructura de repositorio, documentos base o tareas de arranque.

## Secciones obligatorias

1. `Resumen del repositorio`
2. `Tipo de repositorio identificado`
3. `Supuestos e incertidumbres`
4. `Estructura propuesta`
5. `Archivos base sugeridos`
6. `Decisiones iniciales recomendadas`
7. `Checklist de arranque`
8. `Primer commit sugerido`
9. `Siguientes pasos`

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
