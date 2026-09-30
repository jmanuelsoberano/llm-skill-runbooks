# Procedimiento

## Objetivo y baseline
Identifica operación, población, entorno, versión, carga, tamaño de datos, concurrencia y criterio de éxito. Convierte “lento” en una medida pertinente: distribución de latencias, throughput útil, recursos o costo por operación. Si el objetivo es propuesto, márcalo; no inventes carga ni compromisos.

Inspecciona la ruta de ejecución y mediciones disponibles antes de optimizar. Documenta origen, ventana y limitaciones: logs, trazas, métricas, profiler, planes de ejecución o benchmark. Separa latencia percibida, espera, ejecución y trabajo asíncrono. La presencia de base de datos, red o serialización no prueba el cuello de botella.

## Hipótesis y experimentos
Formula hipótesis con mecanismo, señal esperada y observación que las refutaría. Prioriza por plausibilidad, impacto y costo de obtener evidencia. Considera saturación, colas, contención, I/O, recursos y trabajo repetido cuando el recorrido lo indique; evita una lista genérica de ajustes.

Para comparar baseline y alternativa registra condiciones: hardware/entorno, dataset, versión/configuración, distribución de peticiones, concurrencia, warmup, caches, conexiones, duración y repeticiones pertinentes. Cambia factores de manera interpretable; si cambian varios, declara el límite causal. No trates un promedio o una ejecución aislada como distribución. No promedies percentiles de poblaciones distintas como si fueran un percentil global.

Evalúa throughput junto con errores, latencia y trabajo completado. Distingue mejora por cache de mejora para solicitudes frías, estado estacionario de arranque y benchmark sintético de carga representativa. Considera sobrecarga del instrumento y límites del generador cuando afecten conclusiones.

## Cambio y comprobación
Propón el cambio mínimo que aborda la señal observada; detalla costo, complejidad, memoria/datos/consistencia y reversibilidad. Verifica contratos funcionales relevantes: una respuesta rápida e incorrecta no es mejora. Si se pide implementar, edita y prueba dentro del alcance autorizado; si se pide análisis, entrega experimento y criterio.

Compara resultados con unidades y condiciones. Calcula mejora solo desde mediciones compatibles y conserva variabilidad/limitaciones relevantes. Señala regresiones de colas/percentiles o casos que el agregado oculte. No infieras mejora de producción a partir de una prueba local sin evidencia de representatividad.

## Fuentes y salida
Aplica references/evidence-contract.md. Usa documentación oficial vigente para semántica de runtime, base de datos o servicio. O'Reilly mediante oreilly-research disponible puede explicar mecanismos; no demuestra la causa local. Sin mediciones entrega hipótesis y plan de instrumentación, no diagnóstico confirmado. No ejecutes cargas dañinas o cambios de producción fuera de la autorización ni llames recursivamente a evidence-guided-development.

