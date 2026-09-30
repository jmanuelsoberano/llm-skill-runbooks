# Procedimiento

## Situación y alcance
Identifica si el incidente está activo o se analiza después. Determina síntoma, usuarios/operaciones afectados, comienzo conocido, última situación normal, integridad de datos y alcance de acceso. Distingue reportes, observaciones directas y supuestos. Prioriza contener el impacto dentro de la autorización vigente; no retrases una medida reversible justificada por completar documentación exhaustiva.

Lee evidencia del entorno autorizado: logs, métricas, trazas, alertas, cambios, configuración y cronología. Normaliza tiempos a una zona explícita o conserva zona/origen cuando no pueda relacionarse; no inventes orden de eventos de relojes no sincronizados. Preserva referencias y unidades sin extraer secretos o datos personales innecesarios.

## Hipótesis contrastables
Reconstruye una línea de tiempo de hechos y decisiones con origen. Formula hipótesis con mecanismo, hechos a favor/en contra y comprobación que las distingue. Un despliegue cercano es correlación; investigar diferencias y recuperación puede reforzar o refutar causalidad, no demuestra todos los factores por sí solo.

Relaciona síntomas entre componentes y evita equiparar último error registrado con causa inicial. Diferencia disparador, condiciones contribuyentes y fallos de detección/recuperación. Una ausencia en logs puede significar falta de instrumentación.

## Mitigación y recuperación
Propón acciones con efecto esperado, riesgos para datos, alcance, reversibilidad, señal de éxito y condición de parada. Reutiliza runbooks verificados; confirma que versión/contexto coinciden. Acciones como rollback, reinicio, replay, cambio de permisos, eliminación o reprocesamiento no quedan autorizadas por esta skill: ejecuta solo lo incluido en la tarea y entorno.

Antes de reintentar o repetir operaciones con efectos, considera idempotencia, conciliación y duplicados. Recuperar disponibilidad no demuestra integridad restaurada. Si la tarea incluye ejecutar, registra acción, tiempo, resultado y desviaciones; si solo se recomienda, mantiene estado propuesto.

## Conclusiones y prevención
Declara causa como confirmada solo con evidencia suficiente para el mecanismo; si queda abierta, entrega hipótesis más sustentada y comprobación pendiente. Describe factores técnicos y de proceso sin inventar culpas. Asocia prevención con un modo de fallo y criterio verificable, diferenciando contención inmediata de solución duradera.

Para incidentes activos entrega actualizaciones compactas: impacto conocido, evidencia nueva, siguiente acción/decisión; no envíes mensajes a terceros sin autorización. Para revisión posterior entrega cronología y acciones priorizadas.

Aplica references/evidence-contract.md. Documentación oficial y O'Reilly opcional vía oreilly-research pueden explicar mecanismos; nunca reemplazan evidencia causal del sistema. Funciona con artefactos locales e información parcial. No llames recursivamente a evidence-guided-development.

