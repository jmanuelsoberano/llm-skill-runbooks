# Salida ilustrativa — datos sintéticos

**Recomendación condicionada:** outbox en la misma transacción que el pedido, si la base y el código permiten esa unidad atómica.

| Alternativa | Recuperación e integridad | Costo |
|---|---|---|
| Guardar y luego publicar | Puede quedar pedido confirmado sin publicación si el proceso cae entre ambas operaciones. Requiere un mecanismo adicional de reconciliación. | Menos piezas iniciales; recuperación todavía indefinida. |
| Pedido y outbox transaccional | Conserva el trabajo pendiente junto al pedido; un relay puede publicarlo tras recuperarse. | Relay, reintentos, supervisión y retención de registros. |

**Límite.** Marcar como enviado después de publicar puede producir duplicados si el relay cae entre ambas acciones. La clave notificationId permite diseñar deduplicación, pero su corrección aún debe verificarse. La propuesta no acredita entrega exactamente una vez.

**Evidencia.** E1: requisitos y capacidades reportados en la entrada. E2: inferencia propia sobre las ventanas de fallo de las dos secuencias; no se inspeccionó código ni documentación de un broker específico.

**Prueba propuesta.** Interrumpir cada ventana entre persistencia, publicación y marcado; comprobar que no se pierde trabajo confirmado y que duplicados no repiten el efecto de negocio. No se ejecutó esa prueba ni se modificaron archivos.
