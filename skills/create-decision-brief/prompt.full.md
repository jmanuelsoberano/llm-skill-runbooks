# Procedimiento: resumen de decisión técnica

## Encuadre

Identifica la pregunta concreta, quién utilizará el documento, su horizonte y el estado: propuesta, pendiente de aprobación, aprobada o sustituida. Que el usuario pida «redactar la decisión» no demuestra aprobación; conserva la información disponible. Si la petición es resumir una decisión ya tomada, representa fielmente sus motivos y dudas, sin reabrirla salvo que el usuario lo pida o aparezca una contradicción material.

Delimita el problema, los resultados deseados, las restricciones y los criterios de aceptación. Separa restricciones obligatorias de preferencias. Reutiliza el ADR, RFC, acta o evidencia local existente antes de investigar cuestiones ya resueltas.

## Opciones y juicio

1. Construye un conjunto pequeño de opciones viables a partir del contexto. Incluye mantener la situación actual o posponer si realmente son alternativas. No inventes una alternativa débil para favorecer la propuesta.
2. Descarta una opción solo con la restricción incumplida o la evidencia correspondiente. Conserva el costo de transición y el costo de no actuar cuando sean relevantes.
3. Compara por criterios que cambien la elección: comportamiento requerido, integridad, operación, plazo, costo, reversibilidad o dependencia externa. No conviertas criterios desconocidos en puntuaciones numéricas. Si se utilizan pesos, indica quién los fijó y si el resultado cambia con otros valores plausibles.
4. Recomienda una opción o una decisión condicional. Explica el mecanismo que conecta los hechos con la recomendación y qué evidencia contradice o limita esa interpretación. Una preferencia sin datos sigue siendo una preferencia.
5. Para incertidumbres decisivas, propone una comprobación concreta y acotada que permita decidir: qué medir o validar, qué resultado favorecería cada opción y qué acción seguiría. No asegures que el experimento ya ocurrió.
6. Explicita consecuencias aceptadas, riesgos residuales y condiciones de revisión. Si hay un costo, una fecha o un responsable no documentado, déjalo como pendiente; no atribuyas compromisos.

## Entrega

Comienza por la decisión solicitada o recomendada y su estado. Mantén visibles los pocos argumentos que permiten aceptarla o refutarla. Separa respaldo directo, interpretación y acción propuesta sin convertir el documento breve en una investigación completa. Los detalles pueden quedar como anexos solo si ayudan al lector.

Si el problema principal requiere comparar mecanismos de implementación o revisar un ADR, puedes apoyarte en una especialidad disponible, reutilizando su evidencia. Sigue siendo responsable de entregar el resumen solicitado.

## Evidencia y alcance

Aplica [el contrato común de evidencia](references/evidence-contract.md). Reutiliza hallazgos con identificadores y comprueba si su versión y contexto siguen siendo pertinentes. Distingue la afirmación de la fuente de su aplicación al proyecto; declara supuestos, objeciones y datos faltantes. Una referencia encontrada o una respuesta de Answers no equivale a haber leído su pasaje.

Selecciona fuentes en proporción a la decisión. Si `oreilly-research` está descubierta y aporta, puedes usarla para obtener evidencia; su ausencia no bloquea el trabajo. Si el usuario solicita una fuente o Answers expresamente, intenta ese acceso mediante herramientas disponibles y comunica cualquier bloqueo. No asumas herramientas Expert ni acceso por una suscripción distinta. Consulta documentación oficial vigente para detalles dependientes de versiones cuando sea necesario. Envía a consultas externas solo contexto técnico mínimo y autorizado.

Puedes trabajar de forma autónoma con el material accesible o devolver tu resultado a un coordinador. No invoques recursivamente `evidence-guided-development`. La elaboración o revisión de un documento no autoriza publicarlo, modificar sistemas, comprometer fechas ni comunicar decisiones a terceros. Respeta el entregable solicitado y distingue comprobaciones ejecutadas de propuestas.
