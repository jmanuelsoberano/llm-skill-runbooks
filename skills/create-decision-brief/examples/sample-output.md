# Salida ilustrativa — datos sintéticos

## Recomendación pendiente de aprobación

Separar la confirmación de recepción de la emisión de factura, siempre que podamos conservar el trabajo pendiente de forma duradera y operar sus reintentos.

**Razón.** El rango reportado en PERF-01 llega a 8 s [E1]; por ello esperar siempre a ese proveedor puede incumplir el límite de 2 s [E2]. La aceptación funcional permite confirmar recepción antes de completar la factura [E3]. Esta conclusión se deriva de los datos de entrada; no ejecuté una prueba nueva.

| Opción | Condición decisiva |
|---|---|
| Esperar al proveedor | No satisface el límite para todas las duraciones reportadas. |
| Registrar trabajo pendiente y responder | Permite desacoplar la respuesta; requiere durabilidad, estado visible y recuperación. |

**Consecuencias.** Habrá estados intermedios y operación adicional. La solución no queda definida únicamente por elegir una cola: debe evitar perder el trabajo entre guardar el pedido y programar la factura.

**Comprobación propuesta.** Simular caída tras confirmar la recepción y comprobar que el trabajo se recupera sin duplicar facturas. También medir latencia del acuse bajo carga. Ambas verificaciones están pendientes.

**Revisar la decisión si** negocio exige factura emitida dentro de los mismos 2 s.

**Evidencia.** E1: reporte PERF-01 descrito por el solicitante; acceso al reporte original pendiente. E2: límite de respuesta en la solicitud. E3: aceptación funcional reportada; confirmación independiente pendiente. No se consultaron fuentes externas en este ejemplo.
