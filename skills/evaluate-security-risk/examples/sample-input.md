# Entrada de ejemplo sintética

Evalúa el riesgo del endpoint GET /documents/{id}. Document almacena id y tenantId. El middleware autentica y obtiene tenantId del token validado. El repositorio ejecuta FindById(id) sin validar el tenant; la interfaz sí filtra documentos. Queremos recomendaciones y pruebas propuestas, sin cambiar archivos.

