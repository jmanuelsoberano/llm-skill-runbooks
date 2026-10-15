# Mantener la skill y sus fuentes

Esta guía se aplica solo a una petición de mantenimiento. La actualización del conocimiento no es una tarea automática de cada presentación ni un monitor programado.

## Actualización revisable

1. Localiza el repositorio fuente indicado por el usuario y revisa sus instrucciones, estado Git, versión y convenciones. Si solo tienes una copia instalada y no puedes identificar la fuente, pregunta por su ubicación; no edites silenciosamente la copia como si fuera la fuente.
2. Lee el registro de fuentes del paquete y el índice de la serie: https://martinfowler.com/articles/never-send-slides/ . Comprueba tanto nuevas entregas como revisiones de las existentes. La fecha del índice por sí sola no demuestra que todos los artículos cambiaron.
3. Lee los pasajes pertinentes accesibles. Registra URL, título, fecha de revisión, alcance leído y limitaciones. Si no hay acceso, conserva el conocimiento anterior, registra el intento como pendiente y no actualices una fecha de verificación como si hubieras leído el contenido. Usa material aportado por el usuario si está disponible y distingue su procedencia.
4. Decide qué cambia realmente el comportamiento. Separa consejo del autor, evidencia de referencias y adaptación propia. No copies libros ni conviertas cada novedad en una regla universal. Si un nuevo texto contradice uno previo, documenta el matiz y su contexto antes de modificar las instrucciones.
5. Modifica solo procedimiento, guía, contratos, referencias o casos afectados. Conserva preferencias explícitas y límites del encargo. Actualiza metadata y registro del catálogo coherentemente, con versionado semántico y changelog: patch para aclaraciones compatibles, minor para capacidades compatibles, major para cambios incompatibles de un contrato estable.
6. Ejecuta la validación del catálogo y los casos de comportamiento afectados, incluyendo al menos un caso donde el método no deba imponerse. Distingue pruebas realizadas de propuestas y conserva resultados de ejecuciones relevantes.
7. Resume novedades, cambios de alcance y pendientes. Sincroniza las instalaciones solo cuando el encargo lo incluya, comprobando versión y archivos completos; publicar en GitHub o activar automatizaciones no forma parte implícita de actualizar el contenido local.

## Portabilidad

El núcleo usa el formato Agent Skills y referencias relativas dentro del paquete. No introduzcas rutas personales, nombres de herramientas obligatorias, sintaxis de shell interpolada ni campos exclusivos de un cliente en el frontmatter común.

La metadata de interfaz de Codex puede permanecer en `agents/openai.yaml`; no es necesaria para ejecutar el procedimiento en Claude Code u otro agente compatible. Configura la activación específica de cada cliente por separado si el usuario la solicita. El comportamiento por defecto se delimita por la descripción: crear un archivo PowerPoint no basta para seleccionar esta skill.

Las herramientas de exportación, navegación y publicación pertenecen al entorno. Mantén una vía de uso manual proporcionando procedimiento, contratos y referencias relevantes a clientes sin descubrimiento automático. No atribuyas compatibilidad probada a clientes donde no se ejecutó.

Fuentes del formato consultadas el 2026-10-15: [Agent Skills](https://agentskills.io/specification), [Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://learn.chatgpt.com/docs/build-skills).
