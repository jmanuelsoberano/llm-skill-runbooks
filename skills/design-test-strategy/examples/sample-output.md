# Salida de ejemplo sintética

## Prioridad
Comprobar duplicados y fallos entre proveedor y persistencia. El orden descrito deja una ventana cuya resolución depende del contrato de idempotencia/consulta del proveedor.

| Caso | Comprobación | Nivel propuesto |
|---|---|---|
| Mismo paymentId recibido dos veces | Un único efecto de cargo y estado coherente | Integración del flujo con contrato del proveedor comprobado |
| Dos entregas concurrentes | Protección efectiva frente a carrera | Integración con persistencia real |
| Cargo aceptado, persistencia falla | Reintento no duplica; resultado recuperable | Integración y prueba de fallo controlada |
| Respuesta del proveedor desconocida | Conciliación antes de repetir efecto | Contrato y comportamiento del flujo |

**Pendiente:** semántica de idempotencia y consulta del proveedor. No asumimos transacción atómica entre proveedor y SQL.

**E1:** contrato reportado por el usuario. Casos propuestos; ninguno implementado ni ejecutado.

