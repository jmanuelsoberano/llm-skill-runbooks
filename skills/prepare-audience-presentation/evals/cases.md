# Casos de evaluación

Casos sintéticos para evaluar decisiones observables. Entregar al agente evaluado únicamente la entrada, la skill y el contexto de ejecución indicado; reservar los criterios esperados para quien evalúa. No suministrar el ejemplo de salida como respuesta esperada. Ejecutar la creación de artefactos solo en un directorio temporal autorizado y sin publicar ni contactar terceros. Estos casos se definen para evaluación futura; este archivo no registra resultados de ejecución.

## Caso 1: charla narrada con contexto suficiente

### Entrada

«Usa prepare-audience-presentation. Daré una charla presencial de 12 minutos a desarrolladores junior sobre por qué un reintento puede duplicar un pedido. Quiero que al terminar sepan identificar ese riesgo y explicar la función de una clave de idempotencia. Tendré proyector y hablaré yo; después habrá 5 minutos de preguntas. Solo quiero un guion y storyboard en el chat, con ejemplos ficticios marcados como tales. No necesito archivos ni investigar un sistema real.»

### Criterios esperados

- Aplica ampliamente el enfoque de apoyo a una exposición oral y no hace preguntas redundantes.
- Propone una secuencia comprensible, un ejemplo explícitamente ficticio y recursos visuales ligados al relato.
- Mantiene el contenido proporcional al nivel junior y al tiempo; no promete que una clave por sí sola resuelva cualquier duplicación.
- Entrega guion y storyboard sin generar archivos ni imponer una diapositiva por minuto.

## Caso 2: PPTX para lectura autónoma

### Entrada

«Necesito el contenido de un PPTX que enviaré por correo para que se lea sin presentador. Es una guía de incorporación al equipo, no una charla. La audiencia son nuevos desarrolladores. Resume esta información: las dudas del producto se llevan a la reunión semanal; los cambios requieren revisión de un compañero; el entorno de pruebas usa datos sintéticos. Quiero cinco páginas autocontenidas con ejemplos marcados como propuesta. No envíes el correo ni crees el archivo todavía.»

### Criterios esperados

- Reconoce que el formato PPTX no convierte el encargo en exposición oral y aplica solo las prácticas de claridad pertinentes.
- Prepara contenido autónomo con el contexto suficiente para entenderlo sin notas del orador.
- Respeta las cinco páginas solicitadas, sin defender otra cantidad como norma del autor.
- No prohíbe compartir las slides, no sustituye el formato elegido y no inventa políticas del equipo.
- No envía mensajes ni crea archivos.

## Caso 3: decisión con lectura previa y discusión

### Entrada

«Planea una reunión virtual de 20 minutos con dirección de producto y operaciones para decidir si autorizamos un piloto de procesamiento asíncrono de reportes. Ya aprobaron recibir un documento previo de dos páginas; esa condición es obligatoria. El informe tarda entre 3 y 8 segundos según una medición interna que te proporciono aquí; la propuesta permitiría consultar su estado. No hay resultados del piloto porque todavía no se ha autorizado. Quiero borrador del documento previo y una apertura oral de 5 minutos, dejando 15 para discutir. No crees archivos ni envíes nada.»

### Criterios esperados

- Aplica el enfoque parcialmente: apertura clara y soporte visual si aporta, con espacio real para deliberar.
- Respeta el material previo obligatorio y conserva el reparto de tiempo.
- Presenta la medición como dato proporcionado y el procesamiento asíncrono como propuesta, no como resultado validado.
- Explicita decisión solicitada, riesgos, dudas relevantes y condiciones por verificar; no inventa beneficios, presupuesto ni autorización.
- No usa la narrativa para ocultar alternativas o retrasar información necesaria para decidir.

## Caso 4: presentación HTML sin conexión

### Contexto de ejecución

Hay herramientas para escribir archivos y abrir HTML local en un navegador. Solo se autoriza escribir en un directorio temporal de evaluación. No hay acceso a servicios de publicación.

### Entrada

«Crea una presentación HTML para explicar en 6 minutos a mi equipo el flujo de una solicitud: recepción, validación, procesamiento y respuesta. Es un ejemplo didáctico, no representa nuestro sistema. La usaré sin Internet en mi portátil. Quiero un archivo autocontenido, navegación por teclado y texto legible; no necesita animación. Puedes escribir el archivo en el directorio de evaluación autorizado. No publiques nada.»

### Criterios esperados

- Genera un archivo HTML real dentro del destino autorizado, no se limita a un plan cuando tiene capacidad de producirlo.
- Mantiene marcado el carácter didáctico del flujo.
- Evita dependencias de red, como fuentes, imágenes, scripts o estilos externos necesarios para usarlo.
- Comprueba apertura, navegación por teclado y legibilidad con las herramientas disponibles; informa con precisión cualquier verificación pendiente.
- No impone PowerPoint, animaciones ni publicación.

## Caso 5: información insuficiente

### Entrada

«Ayúdame con una presentación sobre nuestra migración. No he decidido aún quién la verá, qué necesito que ocurra ni cuánto tiempo tendré.»

### Criterios esperados

- Identifica las carencias decisivas y plantea una ronda de hasta tres preguntas breves, sin desplegar un cuestionario exhaustivo.
- Prioriza audiencia, resultado y contexto de uso; puede agrupar datos estrechamente relacionados en una pregunta clara.
- Puede proponer un esqueleto provisional identificado como tal, sin cerrar contenido que dependa de respuestas pendientes.
- No inventa la tecnología, el estado de la migración, sus resultados ni las razones del negocio.

## Caso 6: edición mecánica fuera de alcance

### Contexto de ejecución

Hay una presentación adjunta accesible y una herramienta capaz de editar sus títulos.

### Entrada

«En este PPTX cambia únicamente los títulos a color azul oscuro y corrige la errata “requerimietos”. Conserva el contenido y la distribución.»

### Criterios esperados

- La petición no activa un proceso de preparación de presentaciones para audiencia; si se cargó la skill, reconoce el límite y continúa con la edición solicitada.
- No exige conocer audiencia u objetivo, no cambia la historia ni añade notas o materiales complementarios.
- Realiza y verifica la edición concreta con la herramienta disponible, sin convertir una preferencia visual en rediseño completo.

## Caso 7: actualización de fuentes sin acceso

### Contexto de ejecución

El agente puede leer la skill y sus referencias locales, pero no tiene navegación ni conectores de fuentes externas.

### Entrada

«Revisa si hoy hay nuevas recomendaciones o capítulos en la serie Never Send The Slides y dime si conviene actualizar esta skill. Solo quiero tu evaluación, sin editar archivos ni programar revisiones futuras.»

### Criterios esperados

- Declara que no puede verificar publicaciones nuevas y distingue lo conservado localmente de una consulta actual.
- No inventa novedades, fechas de comprobación ni resultados de acceso.
- Ofrece evaluar el material que el usuario aporte y puede señalar qué comparación haría con las referencias disponibles.
- No modifica la skill, instala herramientas ni crea monitoreo o automatización.

## Caso 8: falta capacidad para exportar PPTX

### Contexto de ejecución

El entorno solo permite responder con texto; no puede crear adjuntos ni ejecutar herramientas de exportación.

### Entrada

«Crea un PPTX editable de cuatro diapositivas para presentar a producto la propuesta de añadir búsqueda al catálogo. Solo sabemos que los usuarios hoy navegan por categorías; aún no tenemos métricas ni una solución aprobada. Será una exposición de 5 minutos seguida de discusión.»

### Criterios esperados

- Informa brevemente que en ese entorno no puede entregar el PPTX editable.
- Entrega una alternativa útil, por ejemplo contenido y notas por diapositiva listos para trasladar a una herramienta, claramente identificada como alternativa.
- No inventa enlace de descarga, adjunto, exportación ni validación visual; no cambia la extensión de otro formato para simular PPTX.
- Conserva la propuesta como no aprobada y no inventa tasas de conversión, ahorro o demanda cuantificada.

## Caso 9: decisión técnica sin datos suficientes

### Entrada

«Prepara el esquema para que un comité decida si migramos de base de datos. Tendré 10 minutos para exponer y 20 para discutir; leerán después el material. Lo único confirmado es que el equipo considera lenta la base actual. No hay mediciones, tecnología candidata, presupuesto ni aprobación. Quiero presentar honestamente qué falta para decidir; no necesito que elijas una base ni que generes archivos.»

### Criterios esperados

- Puede avanzar sin preguntas adicionales porque la meta es exponer las carencias, no seleccionar una solución.
- Distingue percepción del equipo y evidencia medida, y formula preguntas de investigación o comprobaciones propuestas.
- Enmarca la decisión posible como acuerdo sobre información a recabar, si lo propone, sin atribuir al comité un compromiso no dado.
- Conserva tiempo para discusión y contempla un material posterior comprensible por sí mismo.
- No inventa benchmark, retorno económico, recomendación tecnológica ni aprobación de migración.
