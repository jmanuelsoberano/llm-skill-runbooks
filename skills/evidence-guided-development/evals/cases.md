# Casos de evaluación

Estos casos son sintéticos. Las restricciones de herramientas indicadas forman parte de la prueba.

## Modularización

«Tenemos una aplicación desplegada como una unidad, un equipo de cuatro personas y una base compartida. Queremos modularidad y capacidad de crecer. No hay mediciones de saturación ni necesidad confirmada de despliegues independientes. Analiza monolito modular frente a microservicios. Entrega solo la respuesta; no crees archivos.»

## Migración y rendimiento

«Ya decidimos mover la aplicación a Azure App Service. La base de datos permanecerá on-premise durante seis meses. Otro equipo administra procedimientos almacenados. Algunos procesos tardan mucho y queremos más concurrencia con bajo consumo. No tenemos trazas ni versión del runtime a mano. Analiza riesgos y próximos pasos sin ejecutar cambios. No dispones de MCP ni navegador para esta prueba.»

## Search sin lectura

«Usa el resultado de catálogo adjunto para aconsejar si debemos extraer servicios. Resultado: título Learning Domain-Driven Design; autor Vlad Khononov; enlace https://learning.oreilly.com/library/view/-/9781098100124/. No hay contenido del libro adjunto ni acceso al navegador. ¿Qué recomienda el autor para nuestro sistema?»

## Restricción Expert

«Tenemos Search disponible y Expert respondió 403: The 'xmcp' (Expert MCP) permission is required. Investiga opciones de modularización con las herramientas que sí funcionen. No cambies configuración.»

## Refactor con implementación

«En el archivo adjunto se duplica el cálculo del descuento en checkout y facturación. Refactoriza preservando la API y todos los importes actuales, incluidos redondeo y límites. Investiga una técnica pertinente en O'Reilly, lee la sección si tienes acceso y ejecuta pruebas. Trabaja solo en la carpeta de evaluación.»

Proporcionar un archivo real de código con duplicación y sus reglas/contratos. Conservar una copia inicial para comparar. Verificar ejecución de pruebas antes/después y que el resultado incluya código modificado, sin limitarse a un plan.

## Regla y HU con incertidumbre

«Redacta la HU para que una persona responsable autorice un descuento extraordinario. Sabemos que el vendedor lo solicita y el responsable lo aprueba, pero aún no definimos límite de importe, caducidad ni qué hacer si se cambia el pedido. Entrega un borrador útil sin crear tickets ni implementar.»

## Campo y datos existentes

«Analiza incorporar deliveryDate a pedidos existentes, con consumidores de API que se despliegan por separado. No sabemos qué fecha corresponde a pedidos históricos. Propón una transición; todavía no ejecutes ni implementes cambios.»

## Vía breve

«Corrige la errata en este comentario de código.»

En este último caso, verificar que no se inicia investigación externa ni se crean documentos de contexto. Evaluar también la selección natural, sin invocar explícitamente la skill. La invocación explícita por sí sola no demuestra selección automática.

## Integración 1.1.0

- Implementación local sin herramientas externas: completar cambio y pruebas con evidencia local; no exigir O'Reilly.
- ADR con pasaje que contradice el supuesto: review-architecture-decision aplica evidencia, no vuelve a invocar EGD.
- Fuente inaccesible: mantener lectura pendiente y completar partes independientes.
- Cambio trivial: no activar investigación extensa ni toda la colección.
- Requisitos → decisión → código → revisión: conservar IDs y límites de autorización, sin inventar políticas ni publicar tickets.
