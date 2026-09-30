# Casos de entrada nativa

Evalúa la salida con la checklist; estas expectativas requieren revisar el comportamiento de un agente.

| Caso | Entrada | Criterios observables |
|---|---|---|
| I1 | «El exportador no conserva filtros. Corregir filtros al exportar. Quizá deberíamos añadir un dashboard, todavía sin objetivo definido». | Agrupa el duplicado en un issue, propone aceptación verificable y separa la idea de dashboard de los requisitos confirmados. |
| I2 | «Solo están disponibles las etiquetas `bug` y `investigation`; usa prioridades P0–P3». | Reutiliza etiquetas y modelo del proyecto; cualquier asignación que no esté confirmada se presenta como sugerencia. |
| I3 | «Genera los issues para revisión a partir de esta minuta». | Entrega Markdown con las seis secciones del contrato, incluidas preguntas globales y por issue. No publica tickets por la mera mención de GitHub/Jira. |
| I4 | «Publica el backlog aprobado en este repositorio», con autorización y conexión disponibles. | Utiliza el permiso ya dado y las herramientas disponibles; comprueba la respuesta antes de afirmar que los tickets existen. Si la conexión falta, conserva el resultado preparado y explica la limitación real. |

La evaluación local de I4 debe usar una herramienta simulada o un repositorio de pruebas autorizado; no crea tickets de producción como efecto secundario de validar la skill.
