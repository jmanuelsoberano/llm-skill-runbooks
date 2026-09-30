# Procedimiento: diseño de cambios de datos

## Significado e invariantes

Empieza por el concepto de dominio: qué significa el dato, quién lo determina, cuándo se conoce, valores permitidos, obligatoriedad y relación con invariantes. Ausencia, desconocido, no aplicable y valor cero pueden representar estados distintos. No conviertas una necesidad de pantalla o columna en una regla de negocio inventada.

Inspecciona el recorrido afectado: dominio, aplicación, almacenamiento, API/eventos, exportaciones, analítica y otros consumidores que existan. Distingue validación técnica de entrada, invariantes de dominio y restricciones de integridad. Conserva cómo el proyecto asigna esas responsabilidades y evita duplicarlas innecesariamente.

## Estado actual y compatibilidad

1. Identifica motor y versión, esquema, tamaños, distribución y calidad de datos, índices, claves y restricciones existentes. Registra qué proviene de inspección autorizada y qué es reportado. Si no hay motor o volumen conocido, condiciona las recomendaciones físicas.
2. Define semántica de lectura/escritura y representación externa. Evalúa null, default y conversiones por su significado; un default no es una forma válida de ocultar datos cuyo valor se desconoce.
3. Mapea productores y consumidores, versiones que coexistirán, contratos API/eventos y compatibilidad. Identifica quién puede seguir escribiendo el esquema anterior durante la transición.
4. Evalúa alcance real de bloqueos, transacciones, operaciones online, índices y restricciones en documentación oficial del motor y versión cuando importen. No transfieras garantías de otro producto ni afirme que una operación es sin bloqueo por el nombre del comando.

## Transición

Diseña la secuencia mínima adecuada al volumen y la incompatibilidad: cambio compatible, despliegue de lectores/escritores, carga de datos existentes, validación y eventual retiro de la forma anterior. No impongas una transición en varias fases a una tabla vacía sin consumidores si no hay riesgo que la justifique.

Para backfill, define fuente de verdad, selección, transformación, lotes, reanudación, idempotencia, progreso, tratamiento de fallos y escrituras concurrentes según necesidad. Detecta valores ambiguos o inválidos; deriva los casos a una decisión de negocio en lugar de inventar valores. Si propones doble escritura, aborda fallos parciales y reconciliación.

Comprueba unicidad, relaciones y equivalencia semántica además de conteos. Los conteos iguales no prueban que cada valor sea correcto. Define comprobaciones antes/después y umbrales de pausa a partir de restricciones reales o como propuestas explícitas.

## Recuperación y operación

Distingue rollback de código, de esquema y de datos. Una transformación con pérdida o una eliminación de columna puede requerir restauración o compensación; un script inverso no garantiza recuperar información. Identifica la ventana de compatibilidad, retención necesaria y punto después del cual revertir exige otra estrategia. No prometa cero pérdida ni cero interrupciones sin evidencia.

Incluye indicadores de avance, errores, bloqueos y latencia relevantes, responsables cuando estén documentados y condiciones para detener. Un plan no cambia producción. Solo ejecuta consultas o migraciones en el entorno y alcance autorizados; si la petición es diseño, entrega diseño. El acceso técnico a una conexión no equivale a autorización de una mutación.

## Entrega

Relaciona cada decisión de datos con su invariante, consumidor y verificación. Si se solicita código, puede prepararse para revisión conforme al contexto; conserva explícito si fue ejecutado y dónde. Falta de acceso a una base permite diseñar con supuestos, pero impide afirmar que los datos cumplen las condiciones.

## Evidencia y alcance

Aplica [el contrato común de evidencia](references/evidence-contract.md). Reutiliza hallazgos con identificadores y comprueba si su versión y contexto siguen siendo pertinentes. Distingue la afirmación de la fuente de su aplicación al proyecto; declara supuestos, objeciones y datos faltantes. Una referencia encontrada o una respuesta de Answers no equivale a haber leído su pasaje.

Selecciona fuentes en proporción a la decisión. Si `oreilly-research` está descubierta y aporta, puedes usarla para obtener evidencia; su ausencia no bloquea el trabajo. Si el usuario solicita una fuente o Answers expresamente, intenta ese acceso mediante herramientas disponibles y comunica cualquier bloqueo. No asumas herramientas Expert ni acceso por una suscripción distinta. Consulta documentación oficial vigente para detalles dependientes de versiones cuando sea necesario. Envía a consultas externas solo contexto técnico mínimo y autorizado.

Puedes trabajar de forma autónoma con el material accesible o devolver tu resultado a un coordinador. No invoques recursivamente `evidence-guided-development`. La elaboración o revisión de un documento no autoriza publicarlo, modificar sistemas, comprometer fechas ni comunicar decisiones a terceros. Respeta el entregable solicitado y distingue comprobaciones ejecutadas de propuestas.
