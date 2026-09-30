# Procedimiento: comparación de implementaciones

## Comportamiento antes que herramientas

Delimita el comportamiento observable, invariantes y restricciones del proyecto. Identifica stack/versiones cuando afecten compatibilidad, volumen y distribución de carga, modelo de fallos, contratos existentes y habilidades operativas. No conviertas una preferencia de biblioteca en requisito funcional.

Revisa el diseño actual y representa las opciones al mismo nivel de detalle. Incluye conservar o ajustar la solución existente cuando sea viable. Si el usuario fijó alternativas, compáralas primero; agrega otra solo si resuelve una limitación material.

## Comparación por mecanismos

1. Para cada alternativa, explica cómo cumple el contrato en el caso normal y ante fallos. Incluye orden, concurrencia, reintentos, duplicados, idempotencia, atomicidad, aislamiento o cancelación cuando afecten el comportamiento.
2. Identifica dónde vive el estado, quién es responsable de su integridad y cómo se recupera. No atribuyas «exactly once», consistencia o seguridad a una herramienta sin definir el ámbito de la garantía.
3. Evalúa complejidad añadida, dependencias, compatibilidad, costo de transición y operación. Evita comparar solo la cantidad de líneas o popularidad.
4. Usa mediciones locales para afirmaciones de rendimiento. Los benchmarks externos orientan mecanismos y experimentos; no prueban el rendimiento del proyecto. Verifica versiones de APIs y límites de producto en documentación oficial accesible cuando sean determinantes.
5. Distingue incompatibilidades demostradas, ventajas condicionadas y desconocidos. No construyas puntuaciones precisas sobre criterios no medidos ni declare una opción universalmente superior.
6. Para una incertidumbre que cambie la selección, diseña una prueba pequeña con entrada representativa, métrica, contrato de corrección y regla de decisión. Solo ejecútala cuando el alcance lo permita; informa qué se ejecutó y bajo qué condiciones.

## Recomendación

Entrega la opción preferida, las condiciones que la justifican y los casos que harían escoger otra. Señala una vía incremental o reversible cuando sea viable. Si no hay evidencia suficiente para elegir, recomienda la comprobación más útil, no una tecnología por defecto.

Una solicitud de comparación produce análisis. Si la misma tarea autoriza implementación, conserva esa autorización y facilita la decisión al flujo de implementación; no invoca recursivamente al coordinador ni trata el documento comparativo como si fuera código ya entregado.

## Evidencia y alcance

Aplica [el contrato común de evidencia](references/evidence-contract.md). Reutiliza hallazgos con identificadores y comprueba si su versión y contexto siguen siendo pertinentes. Distingue la afirmación de la fuente de su aplicación al proyecto; declara supuestos, objeciones y datos faltantes. Una referencia encontrada o una respuesta de Answers no equivale a haber leído su pasaje.

Selecciona fuentes en proporción a la decisión. Si `oreilly-research` está descubierta y aporta, puedes usarla para obtener evidencia; su ausencia no bloquea el trabajo. Si el usuario solicita una fuente o Answers expresamente, intenta ese acceso mediante herramientas disponibles y comunica cualquier bloqueo. No asumas herramientas Expert ni acceso por una suscripción distinta. Consulta documentación oficial vigente para detalles dependientes de versiones cuando sea necesario. Envía a consultas externas solo contexto técnico mínimo y autorizado.

Puedes trabajar de forma autónoma con el material accesible o devolver tu resultado a un coordinador. No invoques recursivamente `evidence-guided-development`. La elaboración o revisión de un documento no autoriza publicarlo, modificar sistemas, comprometer fechas ni comunicar decisiones a terceros. Respeta el entregable solicitado y distingue comprobaciones ejecutadas de propuestas.
