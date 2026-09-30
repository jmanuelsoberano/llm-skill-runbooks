# Capacidades y acceso

Comprobar lo anunciado por el cliente y los esquemas reales antes de cada uso relevante. Los prefijos varían.

| Capacidad | Qué permite comprobar | Límites |
|---|---|---|
| Search MCP, normalmente search_oreilly_content | Descubrir títulos, autores, formatos y enlaces | Metadatos no son pasajes leídos |
| Answers accesible en la plataforma | Obtener orientación y citas para investigar | La respuesta y sus fuentes son evidencias distintas |
| Navegador con sesión autorizada | Leer contenido que la cuenta puede abrir | OAuth del MCP no garantiza sesión en el lector |
| Expert, si está contratado y anunciado | Consultas y citas mediante sus herramientas reales | No se obtiene acceso creando una skill |

## Search

Usar filtros/parametrización soportados por el esquema, sin inventar nombres. Si existe un campo libre skill_used, identificar oreilly-research; si el esquema restringe valores, respetarlo. El endpoint Search documentado es https://api.oreilly.com/api/search/v1/mcp; no configurar ni cambiar conexiones automáticamente como efecto de investigar.

## Navegador y Answers

Reutilizar pestañas/sesión cuando existan; inspeccionar el estado actual. Si falta acceso, usar vías de autenticación permitidas o pedir el fragmento pertinente cuando sea decisivo. No sortear barreras. La comprobación histórica de un libro no garantiza acceso actual. No extraer tokens del navegador ni guardarlos en archivos.

## Expert opcional

Usar ask_oreilly_experts/get_oreilly_citation únicamente si están anunciadas y autorizadas. Respetar su esquema y reutilizar los identificadores devueltos por el servicio; nunca fabricar product_id/offset. Un 403 por licencia xmcp no se resuelve repitiendo OAuth: informar y continuar con las capacidades disponibles.

## Referencias verificadas para el diseño, 2026-09-29

- [Guía MCP](https://www.oreilly.com/online-learning/support/mcp-guide.html).
- [Skills oficiales](https://github.com/oreillymedia/expert-intelligence-skills).
- [Answers](https://www.oreilly.com/radar/oreilly-answers-now-leveraging-genai-that-cites-its-sources/).

Estas fuentes documentan el producto. Nuestro procedimiento Search/Answers/lector es una adaptación propia; no una equivalencia de motor, cobertura, calidad, rapidez o prestaciones empresariales.
