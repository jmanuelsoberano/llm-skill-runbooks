# Procedimiento: pronóstico de entrega

## Definición y datos

Confirma qué significa «terminado», la fecha de referencia, el horizonte, la unidad de trabajo y si se pregunta por fecha para un alcance fijo o por alcance para una fecha fija. Identifica calendario laboral, disponibilidad, tareas de lanzamiento y dependencias. No sumes story points de equipos con escalas diferentes ni trates tickets de tamaño muy desigual como unidades intercambiables sin declarar esa limitación.

Inspecciona el trabajo restante y el flujo histórico accesible: fechas de inicio/fin, trabajo completado por periodo, bloqueos, cambios de alcance y trabajo reabierto. Evita contar iniciado como terminado. Comprueba si la muestra corresponde al equipo, proceso y clase de trabajo actuales; una reorganización, aprendizaje inicial, cambios de definición de terminado o una dependencia nueva pueden invalidar la extrapolación.

## Método proporcional

1. Elige el método según la información. Con pocos datos, usa escenarios condicionales transparentes; con historial comparable suficiente puede ser apropiada una simulación o una distribución empírica. Indica por qué es razonable, no una regla universal de número mínimo de muestras.
2. Expresa unidades y aritmética. Un escenario simple puede usar `remaining_items / items_per_week`; redondea a periodos completos cuando se promete completar todo el alcance y explica semanas parciales. No lo conviertas en probabilidad.
3. Si utilizas simulación, registra datos de entrada, exclusiones, unidad temporal, tratamiento de ceros, iteraciones y semilla cuando aplique; ejecuta realmente el cálculo antes de presentar percentiles. Distingue percentiles del modelo de garantías y revisa sensibilidad a supuestos, dependencia serial y cambios de alcance.
4. No asumas que duplicar personas duplica capacidad ni sumes rendimientos de equipos que se bloquean entre sí. Representa dependencias que condicionan la fecha, actividades secuenciales y capacidad compartida.
5. Separa incertidumbre del tamaño/flujo, riesgo identificado y reserva acordada. No agregues márgenes múltiples para el mismo riesgo ni inventes un porcentaje estándar.
6. Evalúa opciones accionables: reducir alcance, resolver una dependencia, cambiar secuencia o mejorar un cuello de botella. Describe el supuesto de mejora; no lo trates como rendimiento observado.

## Conclusión y actualización

Entrega un intervalo o escenarios solo si los datos permiten construirlos. Si falta historial, devuelve las condiciones necesarias, un método de recolección y, si el usuario lo necesita, escenarios claramente hipotéticos. Nunca presentes una fecha inventada para satisfacer una pregunta cerrada.

Distingue objetivo de negocio, pronóstico y compromiso. Señala la fecha de los datos, qué avance nuevo permitiría actualizar el pronóstico y qué cambio lo invalidaría. Ajusta el detalle al lector; conserva un rastro suficiente para reproducir cálculos realmente realizados.

## Evidencia y alcance

Aplica [el contrato común de evidencia](references/evidence-contract.md). Reutiliza hallazgos con identificadores y comprueba si su versión y contexto siguen siendo pertinentes. Distingue la afirmación de la fuente de su aplicación al proyecto; declara supuestos, objeciones y datos faltantes. Una referencia encontrada o una respuesta de Answers no equivale a haber leído su pasaje.

Selecciona fuentes en proporción a la decisión. Si `oreilly-research` está descubierta y aporta, puedes usarla para obtener evidencia; su ausencia no bloquea el trabajo. Si el usuario solicita una fuente o Answers expresamente, intenta ese acceso mediante herramientas disponibles y comunica cualquier bloqueo. No asumas herramientas Expert ni acceso por una suscripción distinta. Consulta documentación oficial vigente para detalles dependientes de versiones cuando sea necesario. Envía a consultas externas solo contexto técnico mínimo y autorizado.

Puedes trabajar de forma autónoma con el material accesible o devolver tu resultado a un coordinador. No invoques recursivamente `evidence-guided-development`. La elaboración o revisión de un documento no autoriza publicarlo, modificar sistemas, comprometer fechas ni comunicar decisiones a terceros. Respeta el entregable solicitado y distingue comprobaciones ejecutadas de propuestas.
