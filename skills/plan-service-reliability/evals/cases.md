# Casos de evaluación

## Normal: procesamiento asíncrono
### Entrada
Servicio acepta solicitudes de exportación y las procesa con workers. HTTP devuelve 202, pero los usuarios reportan exportaciones que nunca terminan. Hay métricas de HTTP y logs de jobs; no hay SLO aprobado. Pide un plan.
### Criterios esperados
Incluye finalización/antigüedad de trabajos y fallos del recorrido, no usa HTTP 2xx como único éxito. Propone instrumentación y objetivos candidatos. Examina reintentos, duplicación y recuperación de trabajos. No inventa porcentajes de disponibilidad.

## Información ausente
### Entrada
“Necesitamos alta disponibilidad para facturación. No tenemos métricas, RTO, RPO ni presupuesto.”
### Criterios esperados
Delimita resultados críticos y necesidades de negocio, propone medición y decisiones pendientes; no diseña multi-región automáticamente ni inventa compromisos.

## Límite de alcance
### Entrada
“Producción no procesa pagos desde hace diez minutos; analiza estos logs y encuentra una mitigación.”
### Criterios esperados
Reconoce investigación de incidente, prioriza señales/mitigación dentro de autorización y evita sustituir la tarea por un plan largo de confiabilidad.

## Evidencia de recuperación insuficiente
### Entrada
El proveedor informa “backup diario habilitado”. El equipo afirma que recuperará todos los datos en diez minutos, sin restauraciones de prueba.
### Criterios esperados
Distingue configuración de backup y capacidad comprobada; identifica RPO y RTO sin demostrar, y propone ensayo de restauración y verificación de integridad.

