# Salida ilustrativa — datos sintéticos

**Dictamen: ajustar antes de aceptar.** La independencia de despliegue no está demostrada y falta resolver el invariante transaccional.

### Importante — coordinación de datos sin resolver

- **Ubicación:** ADR-007, separación de bases.
- **Evidencia:** E1, requisito R-12 reportado: reserva y confirmación atómicas. E2, propuesta recibida: bases distintas sin mecanismo de coordinación.
- **Impacto:** la descripción no permite comprobar que se eviten pedidos confirmados sin reserva. Es una brecha de diseño; no prueba que ya exista un defecto en producción.
- **Acción:** conservar una unidad transaccional o definir una estrategia que satisfaga explícitamente R-12. Una compensación posterior requeriría que negocio acepte una semántica distinta; no puede asumirse.

**Aceptación propuesta.** Describir estados e invariantes y comprobar fallos entre reserva y confirmación antes de aprobar. Revisar contratos y secuencia de despliegue para evaluar la independencia prometida.

No se inspeccionó código ni se ejecutaron pruebas. La revisión usa la descripción sintética recibida y no cambia el estado formal del ADR.
