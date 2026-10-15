# Validación de 0.1.0

Fecha: 2026-10-15. Estado del paquete: experimental.

## Entorno y método

- Cliente: Codex desktop en Windows. Modelo de los agentes: heredado de la sesión; el identificador exacto no fue expuesto al evaluador.
- Los subagentes de ejecución recibieron solicitudes y recursos de la skill, sin respuestas esperadas, ejemplos ni casos de evaluación. Las cinco solicitudes de texto se resolvieron por un mismo subagente como casos separados; esto no equivale a cinco sesiones aisladas.
- Otro subagente produjo el HTML; un tercero realizó selección usando solo descripciones. El agente principal, autor del núcleo, revisó sus salidas. La revisión del núcleo se delegó a un colaborador que no lo escribió y no reportó hallazgos.
- Datos y contenidos de prueba sintéticos. No se publicó contenido ni se enviaron mensajes a terceros. El acceso a Internet y exportación PPTX se restringió expresamente en los casos de texto para comprobar su respuesta ante esas limitaciones.

## Resultados observados

| Ejecución | Resultado | Evidencia |
|---|---|---|
| A: PPTX para leer sin presentador | Conforme: estructura autónoma, sin forzar narración ni crear archivo no pedido. | [Transcripción](behavior.md) |
| B: contexto insuficiente | Conforme: tres preguntas agrupadas y sin inventar contenido del proyecto. | [Transcripción](behavior.md) |
| C: piloto sin métricas ni aprobación | Conforme: lectura previa, guion y discusión; observaciones, hipótesis y condiciones diferenciadas. | [Transcripción](behavior.md) |
| D: PPTX sin capacidad de exportación | Conforme: declara la limitación y entrega contenido alternativo, sin fingir archivo o renderizado. | [Transcripción](behavior.md) |
| E: comprobar nuevas fuentes sin Internet | Conforme: no afirma actualidad verificada ni cambia el catálogo o programa tareas. | [Transcripción](behavior.md) |
| HTML local: preparación de revisión de código | Conforme: archivo real con controles, teclado y notas, probado en navegador sin conexión. | [HTML](code-review-presentation.html), [ejecución](html-result.md), [comprobaciones](browser-checks.json) |
| R1–R4: selección por descripciones | Conforme: reserva esta skill para narrativa/apoyos; elige edición de presentaciones para color/conversión y brief para análisis de decisión. | [Selección](routing.md) |

El HTML se abrió desde archivo local en Chrome 155.0.8059.79, con modo offline. Se probaron anterior/siguiente, flechas, RePág/AvPág, Inicio/Fin y notas. No hubo errores JavaScript ni solicitudes HTTP/HTTPS. Se comprobaron las seis diapositivas a 1280 × 800 y una vista estrecha a 390 × 844. El agente principal inspeccionó también capturas de las diapositivas 1 y 4. Esto no es una auditoría completa de accesibilidad ni una prueba de proyector o ensayo de duración.

## Validación estructural e instalación

- `python scripts/validate_repo.py`: aprobado para el catálogo con la nueva entrada.
- `python -m unittest discover -s tests -v`: 39 casos, 38 aprobados y 1 omitido porque este sistema de archivos no admite nombres distintos solo por mayúsculas. Son pruebas existentes del repositorio, no 39 pruebas semánticas de la nueva skill.
- Validador `quick_validate.py` de skill-creator: aprobado.
- Frontmatter común limitado a campos de Agent Skills; sin dependencias de herramientas o rutas personales en el procedimiento. Interfaz opcional de Codex separada en `agents/openai.yaml`.
- Copia completa instalada en la ubicación personal reconocida por Codex. La consulta nativa `skills/list` con recarga encontró exactamente una instancia, `scope=user`, `enabled=true`, sin errores de esta skill.

## Límites

Las entradas de `evals/cases.md` son un catálogo para futuras regresiones; no se afirma que se ejecutaran literalmente sus nueve casos. Estas ejecuciones cubren variantes representativas, no todos los escenarios ni todos los modelos.

No se ejecutó la skill en Claude Code ni en otros clientes. La compatibilidad de formato está contrastada con la especificación; sus capacidades de archivo y selección deben comprobarse en cada entorno. Tampoco se probó exportación real a PPTX/PDF ni una actualización con artículos futuros.

Los resultados describen observaciones de esta versión, no garantías de respuestas idénticas. Las rutas temporales de los registros se normalizaron al guardar estos archivos para mantener el paquete portable.
