# Procedimiento

## Tarea y línea base
Aclara usuarios, decisiones o acciones del sistema, costo de errores, supervisión humana, restricciones y criterio de éxito. Identifica si el sistema es generativo, predictivo, de recuperación, de recomendación o combinación. Compara con la solución vigente y una alternativa simple pertinente; no asumas que IA es la mejor opción.

Inspecciona código, flujos, datos autorizados, proveedores/versiones y evaluación existente. Separa prototipo, comportamiento demostrado y aspiración. Considera capacidades reales de herramientas, modelo y contexto sin inventar acceso a Expert MCP u otro servicio.

## Datos y evaluación
Define unidad de evaluación y casos representativos por riesgo: escenarios frecuentes, difíciles, fuera de distribución y grupos/segmentos pertinentes. Establece procedencia, permisos, minimización, retención, datos personales y trazabilidad. Para ML revisa fuga entre entrenamiento/validación/prueba, partición temporal o por entidad y disponibilidad real de características en inferencia. Para generación y recuperación revisa contaminación de ejemplos, calidad de las fuentes y si las respuestas requieren evidencia.

Selecciona métricas alineadas con la tarea: calidad/utilidad, errores de alto impacto, calibración o abstención cuando aplique, latencia, costo y resultados del recorrido. Define rúbricas humanas cuando la exactitud automática no baste; valora consistencia y límites de jueces basados en modelos. Compara con baseline en el mismo conjunto y condiciones. Usa umbrales del negocio o preséntalos como candidatos; no inventes tasas aceptables ni impongas gates universales.

## Controles del producto
Delimita datos que llegan al proveedor, acceso por usuario/tenant, permisos de herramientas y fronteras entre contenido e instrucciones. Para agentes/generación evalúa inyección de instrucciones, exfiltración, acciones indebidas, respuestas sin sustento y manejo de fallos. Para ML añade deriva de datos/concepto y errores en features o preprocesamiento. El modelo no sustituye autorización determinista ni validaciones de invariantes. Ajusta revisión humana/abstención al costo del error; explicita qué puede fallar aun con controles.

## Despliegue y operación
Versiona componentes que cambian comportamiento: modelos, prompts, índices/corpus, features, reglas y configuraciones. Estima costo con volumen y unidades visibles; sin esos datos usa fórmula/escenarios declarados. Diseña observabilidad útil con minimización de datos sensibles, control de cuotas, timeout y degradación.

Propón evaluación offline, piloto/shadow/canary cuando sean pertinentes, criterios de expansión y rollback. El rollback debe contemplar acciones y datos ya producidos: volver al modelo anterior puede no deshacer efectos. Incluye owner, runbook y monitoreo posterior al cambio con señales de calidad, seguridad y drift pertinentes.

## Fuentes y alcance
Aplica references/evidence-contract.md y consulta documentación oficial actual para APIs, retención, precios o garantías de proveedores cuando afecten la decisión. O'Reilly mediante oreilly-research descubierto es apoyo opcional. No envíes datasets privados ni ejemplos sensibles a proveedores sin autorización; usa muestras sintéticas o contexto mínimo. No implementes ni despliegues al pedir solo un plan, ni invoques recursivamente evidence-guided-development.

