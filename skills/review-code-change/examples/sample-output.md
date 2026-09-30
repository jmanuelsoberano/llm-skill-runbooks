# Salida ilustrativa — datos sintéticos

### Importante — la consulta deja de acotar por propietario

**Ubicación:** filtro de GetInvoice del fragmento recibido; no se proporcionaron archivo ni líneas.

**Condición e impacto:** si un usuario solicita el id de una factura ajena, el filtro nuevo ya no aplica la restricción de propietario indicada por el contrato. Bajo el contexto suministrado, esto permite devolver datos de otro usuario.

**Evidencia:** E1, contrato reportado; E2, eliminación de la condición OwnerId == currentUserId descrita en el diff. No se verificaron otros controles fuera del fragmento.

**Corrección sugerida:** conservar el límite de propietario en la ruta de acceso apropiada y comprobar que consultar una factura ajena se rechaza conforme al contrato de errores.

**Verificación:** revisión estática del fragmento; no hubo ejecución de pruebas, modificaciones ni publicación de comentarios.
