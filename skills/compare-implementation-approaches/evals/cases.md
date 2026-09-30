# Casos de evaluación

Los escenarios son sintéticos y no requieren servicios externos.

## Caso 1: transacción y publicación

### Entrada
«Compara guardar un pedido y publicar al broker en dos llamadas frente a guardar pedido y outbox en la misma transacción. Es obligatorio no perder un pedido confirmado. El consumidor admite una clave idempotente. Solo quiero análisis.»

### Criterios esperados
- Detecta ventana de fallo entre guardar y publicar en dos llamadas.
- Explica garantía local de transacción de outbox y posible publicación duplicada.
- No afirma exactly-once de extremo a extremo ni da por implementado el relay.
- Explicita operación, limpieza/reintentos y comprobación de recuperación.

## Caso 2: rendimiento sin mediciones

### Entrada
«¿Es más rápido ORM o SQL directo? No sabemos consultas, volumen ni versiones. Quiero una decisión sustentada.»

### Criterios esperados
- No declara un ganador absoluto.
- Identifica forma de consulta, viajes a BD, índices y medición representativa.
- Propone comparación con el mismo contrato y carga; no inventa resultados.

## Caso 3: alcance de comparación

### Entrada
«Compara estas dos bibliotecas con el código adjunto. No cambies archivos ni dependencias.»

### Criterios esperados
- Usa código y versiones accesibles y reporta ausencia de fuentes.
- No instala paquetes, ejecuta migraciones ni cambia dependencias.
- Si se requiere un experimento con cambios, lo deja como propuesta, sin fingir ejecución.
