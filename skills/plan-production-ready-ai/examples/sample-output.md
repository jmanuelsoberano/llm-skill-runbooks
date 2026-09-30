# Salida de ejemplo sintética

## Recomendación
Preparar evaluación independiente y limitar la ejecución de reembolsos antes de ampliar el piloto. Los 40 casos aportan evidencia de desarrollo, con generalización pendiente.

## Plan
- **Datos:** inventariar documentos autorizados y segmentar permisos de lectura por usuario. Crear casos sintéticos de evaluación con políticas contradictorias, pedidos ajenos y contenido que intenta cambiar instrucciones.
- **Acciones:** validar identidad, pertenencia del pedido, límites y reglas de reembolso en el servicio. Determinar con negocio cuáles requieren revisión humana.
- **Evaluación:** comparar resolución del caso, errores de dinero/datos, fidelidad a políticas, abstención y latencia/costo; umbrales pendientes según impacto. Mantener un conjunto reservado.
- **Operación:** versionar prompt, modelo, corpus y reglas; observar errores sin almacenar información sensible innecesaria; expansión gradual con criterios acordados.
- **Recuperación:** desactivar ejecución y volver a propuestas si falla un control. Los reembolsos ya realizados requieren reconciliación del negocio.

**E1:** escenario aportado, leído directamente como información reportada; no se ejecutó el prototipo. Ninguna métrica de producción fue medida.

