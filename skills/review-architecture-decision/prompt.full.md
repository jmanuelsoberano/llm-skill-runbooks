# Procedimiento: revisión de decisión arquitectónica

## Reconstruir la decisión

Lee el ADR o formula con fidelidad la decisión recibida. Identifica fecha, estado, alcance, contexto, opciones rechazadas y consecuencias aceptadas. Distingue la evidencia disponible cuando se decidió de la actual. No juzgues retrospectivamente como error una elección que era razonable bajo restricciones documentadas distintas.

Identifica las fuerzas determinantes: límites de dominio, invariantes, integridad, latencia, disponibilidad, despliegue, ownership, operación, costo y restricciones normativas según el caso. Comprueba cómo se manifiestan en el sistema concreto. Un diagrama no demuestra que los límites descritos se mantengan en código o datos.

## Contraste

1. Enumera los supuestos que sostienen la decisión y separa los confirmados de los reportados o pendientes. Para cada supuesto material, identifica qué observación lo refutaría.
2. Revisa alineación entre límites de dominio, transacciones, contratos, dependencias y responsabilidad operativa. Localiza acoplamientos que la decisión crea o desplaza; por ejemplo, una separación de despliegue puede mantener dependencia temporal o de datos.
3. Examina escenarios normales y de fallo relacionados con los atributos de calidad prometidos. Las etiquetas «escalable», «desacoplado» o «resiliente» requieren un mecanismo y un escenario verificable.
4. Contrasta alternativas pertinentes y condiciones de aplicación de las fuentes. Distingue contradicción real de diferencias de contexto. No impongas un patrón bibliográfico si las condiciones del proyecto no están presentes.
5. Evalúa la evolución: migración, coexistencia, compatibilidad, observabilidad, recuperación y costo de revertir. La reversión de código puede no deshacer transformaciones de datos; identifica ese límite.
6. Clasifica hallazgos como crítico, importante o sugerencia por impacto demostrado y probabilidad plausible. No eleves severidad solo por faltar una preferencia del revisor. Cada hallazgo enlaza decisión o ubicación, evidencia, consecuencia y acción proporcional.

## Dictamen y alcance

Entrega «sostener», «ajustar» o «reexaminar», o un juicio condicionado cuando falten datos decisivos. La revisión del asistente no equivale a aprobación formal. Describe condiciones de aceptación y eventos que justificarían revisar el ADR.

Cuando el encargo incluya actualizar el documento, conserva su historial y estado conforme a las convenciones del repositorio. Si se pidió solo revisar, entrega hallazgos sin alterar archivos ni construir una arquitectura alternativa completa. Si la fuente central no es accesible, delimita el juicio al material realmente leído.

## Evidencia y alcance

Aplica [el contrato común de evidencia](references/evidence-contract.md). Reutiliza hallazgos con identificadores y comprueba si su versión y contexto siguen siendo pertinentes. Distingue la afirmación de la fuente de su aplicación al proyecto; declara supuestos, objeciones y datos faltantes. Una referencia encontrada o una respuesta de Answers no equivale a haber leído su pasaje.

Selecciona fuentes en proporción a la decisión. Si `oreilly-research` está descubierta y aporta, puedes usarla para obtener evidencia; su ausencia no bloquea el trabajo. Si el usuario solicita una fuente o Answers expresamente, intenta ese acceso mediante herramientas disponibles y comunica cualquier bloqueo. No asumas herramientas Expert ni acceso por una suscripción distinta. Consulta documentación oficial vigente para detalles dependientes de versiones cuando sea necesario. Envía a consultas externas solo contexto técnico mínimo y autorizado.

Puedes trabajar de forma autónoma con el material accesible o devolver tu resultado a un coordinador. No invoques recursivamente `evidence-guided-development`. La elaboración o revisión de un documento no autoriza publicarlo, modificar sistemas, comprometer fechas ni comunicar decisiones a terceros. Respeta el entregable solicitado y distingue comprobaciones ejecutadas de propuestas.
