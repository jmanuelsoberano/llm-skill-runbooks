# Salida de ejemplo sintética

## Conclusión
Primero instrumentar el resultado de exportación y la recuperación de trabajos. Los códigos HTTP actuales no demuestran que el usuario reciba su archivo.

## Indicadores propuestos
- Proporción de jobs válidos finalizados en el plazo acordado. Plazo y ventana pendientes de negocio; fuente propuesta: eventos de aceptación/finalización correlacionados por jobId.
- Antigüedad de jobs no terminales, segmentada por tipo/tamaño; tratamiento de cancelaciones explícito.
- Fallos de entrega del archivo, si la descarga pertenece al recorrido crítico.

## Riesgos y plan
1. Comprobar estados y reintentos: no está demostrado si un worker fallido deja trabajos sin recuperación.
2. Instrumentar una cohorte de jobs y contrastar logs con resultados.
3. Ensayar interrupción y recuperación en un entorno autorizado; verificar finalización única o duplicación controlada.
4. Establecer objetivo y alertas con el owner a partir del impacto y la medición.

**E1:** logs descritos y reporte del usuario; evidencia reportada. No se ejecutaron ensayos ni se midió disponibilidad. RTO/RPO y restauración quedan pendientes.

