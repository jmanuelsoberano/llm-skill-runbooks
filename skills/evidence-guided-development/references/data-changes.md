# Datos, campos y contratos

- Empieza por el significado del dato: a qué concepto pertenece, quién lo define y modifica, obligatoriedad, ausencia, valores permitidos y relación con invariantes existentes. Añadir una columna no define por sí solo el modelo del dominio.
- Inspecciona el recorrido real: dominio, aplicación, persistencia, contratos de API/eventos, validaciones y consumidores. Cambia únicamente las piezas afectadas y evita duplicar la regla de negocio.
- Separa validación técnica de entrada, invariantes de dominio y restricciones de integridad en almacenamiento. Respeta cómo el proyecto distribuye esas responsabilidades.
- Para datos existentes, determina valores iniciales, necesidad de backfill, volumen, índices y efectos sobre escritura/lectura. No elijas un valor por defecto que cambie el significado de registros anteriores sin acuerdo.
- Evalúa compatibilidad entre versiones y orden de despliegue cuando existan consumidores independientes. Propón una transición gradual si la incompatibilidad o el volumen lo justifican.
- Comprueba en la documentación del motor y versión los detalles que puedan afectar bloqueos, transacciones, restricciones y operaciones online. Un ejemplo de otro motor no demuestra el comportamiento del utilizado.
- Prueba creación, actualización, lectura, ausencia y casos inválidos pertinentes. Para migraciones, incluye integridad/reconciliación, validación antes/después y reversión o mitigación realista si no es reversible.

Preparar código o scripts de migración no implica ejecutarlos sobre una base real. Usa solo el entorno autorizado por el usuario.
