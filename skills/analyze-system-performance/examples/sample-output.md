# Salida de ejemplo sintética

## Conclusión
Los tiempos reportados tienen una relación de 20, pero no demuestran que el cambio de código produjo esa mejora: dataset y cache cambiaron simultáneamente.

**E1:** mediciones reportadas por el usuario; discovery_kind: benchmark; access: read; claim_relation: qualifies. No se inspeccionó un arnés ni se repitieron pruebas.

## Comprobación propuesta
Comparar ambas versiones sobre el mismo dataset, carga, entorno y política de cache; separar escenarios fríos y calientes. Registrar errores y resultados funcionales, warmup pertinente y variabilidad con repeticiones justificadas.

La afirmación de mejora queda pendiente. No hay evidencia para extrapolar rendimiento a producción.

