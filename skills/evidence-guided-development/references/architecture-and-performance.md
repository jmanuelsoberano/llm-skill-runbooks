# Arquitectura, proyectos, migración y rendimiento

- Para un proyecto nuevo, parte de objetivos, dominio, restricciones y capacidades del equipo. Reutiliza decisiones ya tomadas y justifica cualquier estructura adicional por un problema concreto.
- Compara alternativas viables incluyendo una mejora localizada cuando aplique. Relaciona modularidad y separación de servicios con límites de dominio, propiedad de datos, transacciones y autonomía real de despliegue.
- Convierte aspiraciones como «rápido» o «pequeño» en criterios medibles y priorizados. Identifica los objetivos propuestos; no inventes carga, presupuesto, cifras de mejora ni rankings sin criterios acordados.
- Para lentitud, sigue una operación y separa tiempos de aplicación, red y almacenamiento. Consulta métricas, planes, esperas, bloqueos y recursos pertinentes. La presencia de una base de datos en el recorrido no demuestra que sea el cuello de botella.
- Para migraciones, identifica qué se mueve y qué permanece, compatibilidad de runtime, conectividad, estado, identidad y procesos en segundo plano. Comprueba requisitos vigentes del servicio elegido.
- Si faltan mediciones, formula hipótesis y experimentos que puedan refutarlas. Una fuente explica mecanismos posibles, no prueba la causa de un incidente del sistema.
- Propón etapas con prerrequisitos, responsables conocidos, criterios de aceptación y reversión. Ejecuta cambios solo cuando formen parte del pedido y estén autorizados en ese entorno.
