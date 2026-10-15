# Entrada de ejemplo: decisión sobre un piloto

Este caso es sintético. Los datos se proporcionan solo para ilustrar el uso de la skill.

Usa `prepare-audience-presentation` para planear una reunión virtual de 15 minutos: 8 de exposición y 7 de discusión. Participarán una responsable de producto, una arquitecta y un responsable de operaciones. Quiero que decidan si autorizan explorar con un piloto el procesamiento asíncrono de reportes.

Contexto confirmado para el ejemplo:

- La generación actual tarda entre 3 y 8 segundos, según una medición interna.
- Hoy el usuario espera a que termine la petición; no existe consulta de estado.
- Producto permite proponer una experiencia que confirme recepción y permita consultar el resultado más tarde.
- El equipo no opera actualmente una cola; no hay piloto autorizado ni resultados de esta propuesta.
- También queremos considerar medir y optimizar el proceso síncrono existente.

Necesito solo el plan en el chat: mensaje principal, secuencia de la exposición, apoyo visual y preguntas para decidir. El formato final de apoyo será HTML local, sin Internet; no lo generes todavía. Usaré fondo claro por legibilidad. Enviaremos por nuestra cuenta una página de lectura previa para que puedan revisar los datos y alternativas. Propón el contenido de esa página de forma breve, sin enviar nada.

No inventes ahorro, costes ni fechas. El plan debe dejar claro que autorizar un piloto no equivale a aprobar una migración a producción.
