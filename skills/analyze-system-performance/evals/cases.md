# Casos de evaluación

## Normal: medición de recorrido
### Entrada
GET /orders tiene p95 de 2 s en el período observado. Trazas de una muestra muestran 1.6 s esperando una llamada de inventario; consulta SQL tarda 40 ms. El equipo propone añadir índice SQL. Pide analizar y definir experimento, sin ejecutar.
### Criterios esperados
Prioriza validar espera de inventario y representatividad de muestra, no atribuye causa a SQL. Define experimento/refutación y objetivos por confirmar; no calcula mejora garantizada de p95 sumando componentes de muestras diferentes.

## Información ausente
### Entrada
“La API se siente lenta; usa PostgreSQL. Optimízala.”
### Criterios esperados
Pide/obtiene recorrido, carga y métricas; formula plan inicial de instrumentación y evita cambiar índices o caches sin evidencia.

## Límite de alcance
### Entrada
“Se perdieron cobros tras desplegar y necesitamos contener el daño.”
### Criterios esperados
Reconoce incidente de integridad; no reduce el problema a throughput ni lanza cargas de rendimiento.

## Benchmark no comparable
### Entrada
Baseline: dataset grande y cache fría. Nuevo código: dataset diez veces menor y cache caliente. Una sola ejecución cae de 4 s a 0.2 s.
### Criterios esperados
No atribuye 20× al código ni generaliza a producción. Identifica variables confundidas y define comparación equivalente con comprobación de resultados.

