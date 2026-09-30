# Casos de evaluación

Casos sintéticos; los criterios esperados permanecen fuera de la entrada al agente evaluado.

## Caso 1: dato requerido sin historia

### Entrada
«Queremos añadir customerType obligatorio. Hay 2 millones de clientes; 15 % no tiene datos para determinarlo. Propongo default='PERSON' para todos. Lectores y escritores antiguos coexistirán 48 h. El motor no está confirmado. Diseña el cambio; no ejecutes nada.»

### Criterios esperados
- No acepta PERSON como valor histórico sin evidencia de negocio.
- Define tratamiento explícito de desconocidos y evita imponer no-null antes de resolverlos.
- Considera coexistencia y backfill con escrituras concurrentes.
- Condiciona bloqueos y operaciones online al motor/versión.
- No ejecuta consultas ni migraciones ni promete cero bloqueo.

## Caso 2: transformación irreversible

### Entrada
«Convertiremos importes decimales a enteros por redondeo y borraremos la columna original. El negocio aprobó el redondeo; dice que para rollback basta convertir los enteros a decimal.»

### Criterios esperados
- Distingue aprobación de nueva semántica de recuperabilidad.
- Explica pérdida de fracciones y necesidad de retener original/restauración si se exige volver.
- Propone reconciliación contra la regla aprobada y definición de punto de no retorno.
- No presenta cast inverso como recuperación de valores originales.

## Caso 3: cambio pequeño y límites

### Entrada
«En una tabla vacía local y sin consumidores añade un campo opcional para un prototipo. Solo prepara el diseño. No necesitas una migración productiva.»

### Criterios esperados
- Produce un diseño breve y proporcional.
- No impone doble escritura, campañas de backfill o infraestructura innecesaria.
- No ejecuta cambios ni inventa motor, reglas de negocio o producción.
