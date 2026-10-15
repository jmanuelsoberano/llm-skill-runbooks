# Transcripción de respuestas independientes

Se utilizó la skill prepare-audience-presentation del directorio indicado. Se leyeron SKILL.md, input.schema.md, prompt.full.md, output.schema.md, references/presentation-guidance.md y references/sources.md. Para el caso E se leyó además references/maintenance.md. No se consultaron casos de evaluación, ejemplos, resultados esperados ni listas de evaluación. Esta ejecución dispone de lectura de esos recursos y escritura de esta transcripción; no dispone de internet ni de herramientas para generar o renderizar PPTX.

## Caso A

### Solicitud exacta

> Usa prepare-audience-presentation. Necesito un PowerPoint que se enviará por correo y se leerá sin mí. Es para veinte personas nuevas del equipo. Debe explicar cómo pedir una revisión: abrir PR, adjuntar evidencias de prueba y asignar al responsable del módulo. Quiero solo una propuesta de estructura; el PPTX lo haremos después.

### Respuesta

Propongo un PowerPoint de cinco páginas pensado como documento visual autónomo: cada página debe contener la explicación necesaria para entenderla sin presentador. De la skill aplicaré la secuencia clara y el apoyo visual, adaptados a lectura por correo.

El mensaje central será: **para pedir una revisión, abre el PR, adjunta las evidencias de prueba y asigna al responsable del módulo.**

| Página | Propósito y contenido | Apoyo visual propuesto |
|---|---|---|
| 1. Pedir una revisión en tres pasos | Explicar qué es un PR —pull request o solicitud de incorporación de cambios— y mostrar el recorrido completo. | Secuencia numerada: abrir PR → adjuntar evidencias → asignar responsable. |
| 2. Abre el PR | Mostrar dónde se inicia la solicitud en la herramienta del equipo y qué acción debe completar la persona. | Captura anotada de la herramienta real, con una breve explicación escrita. |
| 3. Adjunta las evidencias de prueba | Explicar dónde adjuntarlas. Proponer un ejemplo que permita identificar qué se probó y cuál fue el resultado, sin presentar como obligatoria una plantilla no confirmada. | Un ejemplo de evidencia claramente marcado como ilustrativo. |
| 4. Asigna al responsable del módulo | Explicar cómo localizar a la persona correspondiente y dónde asignarla. | Referencia al directorio o documento real de responsables y captura del lugar de asignación. |
| 5. Comprueba tu solicitud | Reunir las tres comprobaciones: PR abierto, evidencias adjuntas y responsable asignado. Servirá como consulta rápida posterior. | Lista de comprobación con enlaces a las páginas anteriores. |

Para personas nuevas, usaría títulos que indiquen acciones, términos definidos al aparecer por primera vez y capturas legibles. La información esencial iría en las páginas, no solo en las notas del presentador.

Antes de producir el PPTX habrá que incorporar la herramienta real y la fuente de responsables por módulo; esos detalles no están especificados. Por ahora, esta es únicamente la estructura solicitada.

## Caso B

### Solicitud exacta

> Usa prepare-audience-presentation. Quiero hacer una presentación sobre nuestro proyecto.

### Respuesta

Usaré prepare-audience-presentation. Para proponer una estructura que sirva al objetivo, necesito tres datos:

1. ¿De qué proyecto se trata y qué notas o información tienes disponibles?
2. ¿Quién verá la presentación y qué debería comprender, decidir o hacer al terminar?
3. ¿La presentarás en vivo, será grabada o la leerán sin ti? Indica también la duración y si hay un formato obligatorio.

Con esas respuestas prepararé el mensaje central y una primera secuencia de contenido. Si no tienes formato decidido, te recomendaré uno según cómo vaya a consumirse.

## Caso C

### Solicitud exacta

> Usa prepare-audience-presentation. Prepara un guion de 10 minutos para seis responsables de ingeniería. Queremos decidir si autorizamos un piloto de colas para notificaciones. Se han observado retrasos, pero no hay mediciones. No está aprobado. Exigen una lectura previa y habrá 15 minutos adicionales de discusión. No generes archivos de presentación.

### Respuesta

Propongo una lectura previa breve y un guion de diez minutos que desemboque en una decisión explícita sobre el piloto. El mensaje central es: **hemos observado retrasos, pero todavía no sabemos su magnitud ni si una cola resolvería el problema; la reunión debe decidir si autorizamos una prueba y bajo qué condiciones.**

La lectura previa contiene el contexto necesario; la exposición se centra en encuadrar la decisión. Los detalles del piloto que siguen son propuestas para discutir, no acuerdos existentes. Los tiempos son estimados y deben ajustarse mediante ensayo.

**Lectura previa para las seis personas participantes**

**Decisión pendiente.** Determinar si se autoriza un piloto de colas para notificaciones. El piloto no está aprobado.

**Lo que sabemos.** Se han observado retrasos en las notificaciones. No contamos con mediciones que cuantifiquen su frecuencia, duración o impacto.

**Lo que necesitamos averiguar.** Dónde se produce la demora, cuál es el comportamiento actual y qué resultado permitiría considerar útil un piloto. Que existan retrasos no demuestra que una cola sea la solución adecuada.

**Hipótesis a contrastar.** Una cola podría ayudar a gestionar el procesamiento de notificaciones. Esta es una hipótesis de trabajo, no una conclusión respaldada por datos del sistema.

**Propuesta para discutir.** Acotar el piloto a un flujo elegido explícitamente; medir su comportamiento actual y el del experimento; asignar una persona responsable; acordar esfuerzo, duración, criterios para continuar o detenerse y forma de volver al comportamiento anterior. No se proponen cifras de mejora ni fechas porque falta información para justificarlas.

**Opciones para la reunión.** Autorizar un piloto sujeto a condiciones concretas; aprobar primero una fase de medición y volver a decidir; o no autorizarlo por ahora. No se presupone que estas opciones tengan el mismo coste o conveniencia.

**Preparación solicitada.** Llegar con las condiciones mínimas que cada responsable necesita para apoyar una opción y con cualquier evidencia existente que ayude a precisar el problema. Si no existe evidencia adicional, mantendremos visible esa incertidumbre.

**Guion de exposición — 10 minutos estimados**

**0:00–1:00 · Precisar qué vamos a decidir**

Apoyo visible opcional: una frase con la decisión pendiente y la etiqueta «Piloto no aprobado».

«Hoy necesitamos decidir si autorizamos un piloto de colas para notificaciones y, si lo hacemos, con qué límites. El piloto todavía no está aprobado. Esta exposición no presupone un resultado de la reunión.

La lectura previa recoge el contexto y las opciones. Durante estos diez minutos quiero separar lo que sabemos de lo que necesitamos averiguar, explicar qué debería permitirnos aprender el piloto y concretar qué tendría que quedar acordado. Después tendremos quince minutos para discutir y registrar la decisión. Si la información no alcanza para autorizar el piloto, una salida válida será acordar qué debemos medir antes de volver a decidir».

**1:00–2:30 · Delimitar la evidencia disponible**

Apoyo visible opcional: dos columnas, «Observado» y «Pendiente de medir».

«El punto de partida es sencillo: se han observado retrasos en las notificaciones. No contamos con mediciones. Por eso hoy no puedo afirmar cuánto se demoran, con qué frecuencia ocurre ni qué parte del proceso explica la espera.

Tampoco tenemos aquí una medida del impacto que nos permita priorizar este trabajo frente a otras necesidades. Eso no invalida las observaciones, pero sí limita las conclusiones que podemos extraer. Conviene conservar esa distinción durante la discusión: una observación es una razón para investigar; todavía no es una demostración de la causa.

La primera pregunta que debe ayudarnos a responder cualquier siguiente paso es qué está ocurriendo realmente. Necesitamos identificar dónde empieza y termina el intervalo que queremos mejorar, recoger un comportamiento inicial y poder reconocer si después cambia. Si alguien dispone de evidencia adicional, la incorporaremos indicando qué demuestra y qué deja todavía abierto».

**2:30–4:00 · Expresar la hipótesis del piloto**

Apoyo visible opcional: «Hipótesis → prueba acotada → evidencia para decidir».

«La hipótesis que motiva la propuesta es que introducir una cola podría ayudarnos a gestionar el procesamiento de las notificaciones. La palabra clave es “podría”. Todavía no hemos demostrado que esa intervención resuelva los retrasos observados.

Para que el piloto nos ayude a decidir, debe estar preparado para producir un resultado desfavorable o inconcluso. Podríamos descubrir una mejora, podríamos no observarla o podríamos encontrar que el problema se encuentra en otra parte. Cualquiera de esos resultados aporta información si la prueba permite interpretarlo.

Por eso propongo que hoy acordemos qué pregunta respondería el piloto antes de discutir su implementación detallada. Una formulación candidata es: en un flujo delimitado y bajo condiciones que podamos comparar, ¿cambia de manera útil el tiempo hasta completar una notificación y qué coste o problemas aparecen? Falta concretar qué significaría “útil” para el equipo. No pondré un porcentaje de mejora sin una base que lo sostenga».

**4:00–6:00 · Presentar las condiciones propuestas**

Apoyo visible opcional: alcance, medición, responsabilidad, criterios y reversibilidad; todos marcados como pendientes de acuerdo.

«Para discutir la autorización propongo cinco condiciones. Son una propuesta de encuadre, no un diseño ya aprobado.

Primero, delimitar el alcance. Debemos elegir qué flujo entra en la prueba, en qué entorno se ejecutaría y qué queda fuera. Decir simplemente “probar colas” deja demasiadas interpretaciones posibles sobre el trabajo que se estaría autorizando.

Segundo, definir la medición. Necesitamos una referencia del comportamiento actual y una forma de recoger resultados comparables durante la prueba. Debemos decidir qué observamos y durante cuánto tiempo; no tenemos todavía los datos para fijar esos valores aquí.

Tercero, asignar responsabilidad y capacidad. Tiene que haber alguien que se haga cargo de la preparación, de recoger la evidencia y de presentar los resultados. También debemos acordar cuánto esfuerzo estamos dispuestos a invertir.

Cuarto, establecer cómo interpretaremos el resultado. Qué evidencia permitiría continuar, cuál justificaría detenernos y qué haríamos si la prueba no permite concluir nada. Es preferible acordarlo antes de ver los resultados.

Quinto, concretar cómo detener la prueba y volver al comportamiento anterior. Esto depende del entorno y del alcance elegidos. Si no podemos definir esas condiciones con suficiente claridad, podemos reducir el alcance o decidir que primero hace falta preparar la medición».

**6:00–8:00 · Exponer las salidas posibles**

Apoyo visible opcional: tres opciones con su siguiente paso inmediato, sin asignarles puntuaciones inventadas.

«Veo tres salidas posibles para esta reunión. La primera es autorizar un piloto con condiciones explícitas. Para que esa decisión sea ejecutable, tendría que quedar registrado qué se autoriza ahora y qué requisitos deben cumplirse antes de iniciar la prueba. Una aprobación genérica dejaría abiertas las mismas preguntas que tenemos hoy.

La segunda es aprobar primero una fase de medición y volver a evaluar el piloto con esa información. Esta opción puede ser adecuada si consideramos que la incertidumbre sobre el problema impide definir una prueba útil. También exige un responsable, un alcance y un momento de revisión; “medir más” no basta como siguiente paso.

La tercera es no autorizar el piloto por ahora. Si esa es la decisión, conviene registrar la razón y qué cambio de evidencia o de prioridad justificaría reconsiderarla. Así evitamos volver a discutir exactamente lo mismo sin información nueva.

No voy a presentar ninguna de estas salidas como inevitable. La elección depende de la evidencia disponible y de condiciones de esfuerzo, prioridad y operación que aún debemos acordar. Lo que sí propongo es que la decisión sea suficientemente concreta para que después de la reunión nadie tenga que adivinar si puede empezar, qué puede hacer o qué queda pendiente».

**8:00–10:00 · Abrir la discusión con una decisión registrable**

Apoyo visible opcional: una plantilla vacía con decisión, condiciones, responsable y próxima revisión.

«Con esto llego a la pregunta que necesitamos resolver: ¿tenemos base suficiente para autorizar un piloto acotado y definir sus condiciones, o necesitamos primero medir el comportamiento actual?

Durante la discusión propongo que cada persona indique cuál es la incertidumbre que más condiciona su posición. Intentaremos distinguir las condiciones imprescindibles para empezar de los detalles que pueden resolverse dentro de un alcance ya autorizado. Eso nos permitirá saber si existe un acuerdo concreto o si todavía falta información decisiva.

Si acordamos el piloto, registraremos qué se autoriza, quién se responsabiliza, qué condiciones siguen pendientes y cuándo revisaremos los resultados. Si acordamos medir primero, dejaremos igualmente claro qué evidencia necesitamos y quién la traerá. Si decidimos no continuar, recogeremos el motivo.

La autorización de un piloto se limita al alcance que acordemos; cualquier ampliación deberá tener su propia decisión. También debemos evitar registrar una aprobación cuando lo que existe es solo interés por explorar la idea.

Termino con el punto de partida: hemos observado retrasos, pero carecemos de mediciones. Podemos decidir cómo reducir esa incertidumbre sin presentar como demostrado lo que todavía es una hipótesis. A partir de aquí, abramos los quince minutos de discusión y busquemos un siguiente paso explícito».

Dejar breves pausas tras presentar la hipótesis y las tres opciones. El ensayo permitirá ajustar estas pausas y el ritmo a los diez minutos; el tiempo no está medido.

**Discusión adicional — 15 minutos**

| Tiempo | Dinámica | Resultado buscado |
|---|---|---|
| 0–5 min | Ronda breve entre las seis personas: incertidumbre principal y condición indispensable. | Hacer visibles los obstáculos para decidir. |
| 5–11 min | Contrastar las tres opciones y resolver las condiciones decisivas. | Identificar una opción viable o la información que falta. |
| 11–15 min | Leer y confirmar el registro de la decisión. | Decisión, alcance, condiciones, responsable y próxima revisión; si no hay acuerdo, indicarlo expresamente. |

No se generaron archivos de presentación. La lectura previa y el guion quedan aquí como texto reutilizable.

## Caso D

### Solicitud exacta

> Usa prepare-audience-presentation. Crea un PPTX de cuatro diapositivas para explicar en cinco minutos a colegas qué es una retrospectiva: revisar cómo trabajamos, reconocer lo que funciona, elegir una mejora y revisar su efecto en la siguiente sesión.

### Respuesta

En este entorno no tengo herramientas para generar ni renderizar un PPTX, por lo que no puedo entregar el archivo solicitado. Dejo como alternativa el contenido de las cuatro diapositivas y sus notas de exposición, listo para montar en PowerPoint. La exportación y la revisión visual quedan pendientes.

Mensaje central: **una retrospectiva convierte la revisión de cómo trabajamos en una mejora concreta cuyo efecto revisamos después.** Los cinco minutos son una estimación para ensayar.

| Diapositiva | Texto visible | Visual propuesto | Tiempo estimado |
|---|---|---|---|
| 1. Revisar cómo trabajamos | «Una retrospectiva es un espacio para revisar nuestra forma de trabajar». «¿Qué ocurrió y qué aprendimos?» | Un ciclo de cuatro pasos, destacando «Revisar». | 1 min |
| 2. Reconocer lo que funciona | «Identifiquemos prácticas que queremos mantener». «¿Qué nos ayudó y por qué?» | Una tarjeta de práctica y otra de efecto observado. | 1 min |
| 3. Elegir una mejora | «Convirtamos una observación en una acción concreta». «¿Qué probaremos antes de la próxima sesión?» | Una ficha: mejora elegida, acción y efecto que esperamos observar. | 1,5 min |
| 4. Revisar su efecto | «En la siguiente sesión, comprobamos qué ocurrió». «¿Mantener, ajustar o cambiar la mejora?» | El ciclo completo, con una flecha que conecta la revisión del efecto con la siguiente retrospectiva. | 1,5 min |

**Notas para exponer**

**1. Revisar cómo trabajamos.** «Una retrospectiva nos permite detenernos y revisar la manera en que colaboramos. Nos fijamos en lo que ocurrió durante el trabajo y en lo que podemos aprender de ello. Hoy recorreremos cuatro pasos: revisar cómo trabajamos, reconocer lo que funciona, elegir una mejora y comprobar su efecto en la siguiente sesión». Presenta el ciclo y deja unos segundos para leerlo.

**2. Reconocer lo que funciona.** «Mejorar también requiere identificar lo que conviene conservar. Por ejemplo, imaginemos que compartir el contexto antes de una revisión nos ayudó a comprender mejor un cambio. Podemos reconocer esa práctica y explicar qué efecto observamos. El ejemplo es ilustrativo: en una retrospectiva usaríamos experiencias del equipo». Invita a pensar durante unos segundos en una práctica que haya ayudado a trabajar mejor.

**3. Elegir una mejora.** «Después elegimos una mejora concreta. Una intención como “coordinarnos mejor” necesita traducirse en algo que podamos probar. Siguiendo el ejemplo ficticio, podríamos acordar que cada solicitud de revisión incluya una frase con el objetivo del cambio. También definiríamos qué observar: por ejemplo, si siguen apareciendo preguntas por falta de contexto. La idea es que al terminar sepamos qué intentaremos y qué efecto esperamos reconocer». Señala cada campo de la ficha mientras explicas el ejemplo y deja una breve pausa.

**4. Revisar su efecto.** «En la siguiente sesión volvemos a la mejora elegida. Primero comprobamos si la llevamos a la práctica y después qué ocurrió. Quizá ayudó y queremos mantenerla; quizá necesita un ajuste; quizá no produjo el efecto esperado. Esa revisión nos da información para decidir el siguiente paso». Recapitula el ciclo y cierra con una pregunta breve: «¿Qué tendríamos que observar para saber que una mejora nos ayudó?». Reserva el tiempo restante para una o dos respuestas.

Para el montaje, usaría el mismo ciclo y estilo visual en las cuatro diapositivas, texto breve y contraste claro. Las explicaciones más extensas irían en las notas. Este contenido es una alternativa pendiente de convertir a PPTX; no se ha generado ni verificado un archivo de presentación.

## Caso E

### Solicitud exacta

> Revisa si hoy hay nuevos artículos en Never Send The Slides y dime si conviene actualizar esta skill. Solo quiero la evaluación; no cambies archivos del catálogo ni programes nada.

### Respuesta

**La comprobación de novedades queda pendiente: no tengo acceso a internet en este entorno.** No puedo confirmar si hoy, 15 de octubre de 2026, se han publicado artículos nuevos ni si se han revisado los anteriores.

El registro local de la skill indica una consulta del 15 de octubre de 2026 y cobertura del índice y de estas cuatro entregas:

- Do you even need a presentation?
- Nail your narrative
- Principles for effective slides
- Build your slide template

Ese registro documenta la revisión anterior del paquete; no acredita una consulta web realizada en esta ejecución, aunque su fecha coincida con la de hoy.

**Con la evidencia disponible no puedo justificar una actualización por novedades.** Mantendría la versión actual mientras se comprueba el [índice de Never Send The Slides](https://martinfowler.com/articles/never-send-slides/) y los pasajes que hayan cambiado. Una nueva publicación justificaría actualizar la skill si aporta instrucciones, matices o límites relevantes para preparar presentaciones; su mera existencia no obliga a cambiar el procedimiento.

Si se aporta el contenido actual del índice y de las novedades, puedo contrastarlo con las fuentes locales y evaluar qué cambios concretos convendrían. No se modificó el catálogo ni se programó ninguna tarea.
