# Procedimiento

## Contexto y recorridos
Lee la arquitectura, contratos, incidentes conocidos y procedimientos disponibles. Identifica usuarios, operaciones críticas, dependencia síncrona/asíncrona, estado persistente, modos de degradación aceptables y responsables conocidos. Distingue requisitos acordados de expectativas candidatas. No impongas alta disponibilidad o redundancia sin impacto y necesidades concretas.

## Indicadores y objetivos
Define SLIs desde resultados observables del usuario, con numerador, denominador, población, ventana, exclusiones justificadas y fuente de medición. Para latencia especifica qué operación y percentil se considera; para trabajo asíncrono considera antigüedad o finalización de tareas cuando reflejen mejor la experiencia. Distingue error técnico, rechazo de negocio y petición inválida.

Si no hay objetivos acordados, presenta SLOs como candidatos y explica qué datos/decisión faltan; no inventes 99.9%, ventanas o presupuestos como compromisos. Calcula presupuesto de error solo con fórmula, ventana y denominador compatibles y datos aportados. Separa SLO de SLA contractual. RTO y RPO son requisitos de negocio por confirmar, no cifras elegidas por costumbre.

## Riesgos y diseño operacional
Para modos de fallo relevantes revisa propagación entre dependencias, límites de concurrencia, timeouts, reintentos con presupuesto, idempotencia, pérdida/duplicación de mensajes, agotamiento de recursos y degradación. Propón controles localizados; explica sus costos y nuevas fallas posibles. Un respaldo existente no acredita recuperación hasta que se comprueba restauración y consistencia.

Asocia cada riesgo prioritario con señal, umbral candidato o criterio, acción y responsable conocido. Diseña alertas accionables; no alertes por cada métrica disponible. Conecta observabilidad con diagnóstico, datos personales y costo de retención.

## Plan y comprobación
Propón etapas por impacto y reversibilidad: medición inicial, reducción de riesgo, ensayo controlado, despliegue y revisión. Cada etapa necesita prerrequisitos, resultado observable, recuperación y owner conocido o pendiente. Simulaciones, pruebas de carga/fallo, restauraciones y cambios en producción requieren el alcance y autorización de la tarea; planificarlos no significa ejecutarlos.

Si hay incidente activo, centra la entrega en lo pedido y remite hallazgos a una investigación específica si está disponible; no demores una mitigación autorizada para completar un programa de SLOs.

## Evidencia
Aplica references/evidence-contract.md. Usa datos locales y documentación oficial vigente para comportamiento de dependencias. O'Reilly, mediante oreilly-research si se descubre, puede aportar patrones y objeciones. Su acceso no es condición para entregar el plan. No invoques recursivamente evidence-guided-development.

