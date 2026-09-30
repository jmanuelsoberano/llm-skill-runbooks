# Salida ilustrativa — datos sintéticos

**Conclusión:** resolver dos aspectos antes de implementar el contrato descrito. Revisión limitada al resumen de RFC-12 proporcionado.

### Importante — respuesta incompatible con la duración

**Ubicación:** secciones 2 y 3. E1 indica respuesta inmediata con archivo final; E2 indica 10 minutos de generación. Falta un mecanismo que haga compatibles ambas afirmaciones. Definir un recurso de seguimiento y la entrega posterior del archivo, o ajustar la semántica de respuesta según el requisito real.

**Cierre propuesto:** comprobar que el cliente puede observar el estado y obtener el archivo final sin interpretar la aceptación como finalización.

### Importante — reintentos pueden repetir el cobro

**Ubicación:** sección 4. E3 describe un cobro por intento sin idempotencia. Una respuesta perdida puede provocar un nuevo intento tras un cobro exitoso. El diseño debe definir una operación de negocio identificable y recuperación del resultado, junto con la política de cobro que confirme negocio.

**Cierre propuesto:** simular pérdida de respuesta después del cobro y verificar el efecto permitido por esa política.

Los hallazgos se derivan del texto sintético recibido. No prueban un defecto del sistema actual; no se ejecutaron pruebas, cambios ni publicaciones.
