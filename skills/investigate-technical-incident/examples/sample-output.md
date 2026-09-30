# Salida de ejemplo sintética

## Estado
La tasa de error bajó según el reporte. Recuperación completa e integridad de datos no comprobadas; zona horaria no especificada.

## Hechos y explicación
- 10:00: despliegue B reportado.
- 10:05: timeouts reportados.
- Alrededor de 10:12: rollback y recuperación de proveedor, ambos reportados.

**E1:** cronología aportada, leída; no métricas originales. **H1:** B introdujo una regresión. **H2:** la dependencia externa causó los timeouts. Ambas siguen abiertas; la coincidencia de recuperaciones impide aislar su efecto.

## Comprobaciones propuestas
Comparar cambios A/B con el recorrido afectado, obtener métricas de llamadas externas y sus ventanas, comprobar errores restantes e integridad de operaciones interrumpidas. No repetir operaciones con efectos sin revisar idempotencia.

El rollback fue una mitigación reportada, no una causa raíz demostrada. No se ejecutó ninguna acción.

