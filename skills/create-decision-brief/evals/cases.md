# Casos de evaluación

Los casos son sintéticos. Los criterios esperados sirven para evaluar; no deben entregarse como entrada al agente que se prueba.

## Caso 1: resumen con una incertidumbre decisiva

### Entrada
«Prepara una nota para decidir entre procesamiento síncrono y cola. Debemos responder en menos de 2 s. El proveedor tarda de 0.4 a 8 s según el informe adjunto. El negocio permite confirmar recepción y mostrar estado. No hay cola operada actualmente. La propuesta aún no está aprobada.»

### Criterios esperados
- Recomienda de forma motivada un acuse y procesamiento asíncrono o una alternativa que cumpla las restricciones.
- Distingue latencia del acuse y tiempo final; registra costo operativo y semántica de reintentos.
- No presenta la propuesta como aprobada ni inventa SLA, presupuesto o mediciones.
- Define una comprobación de fallo/reintento y el criterio que cambiaría la decisión.

## Caso 2: evidencia insuficiente

### Entrada
«Dime en una página si compramos o construimos el buscador. No sé volumen, requisitos ni presupuesto. Solo existe la preferencia del equipo por construir.»

### Criterios esperados
- Devuelve un resumen condicionado y preguntas que cambian la elección.
- No inventa costo total, pesos, fechas ni retorno económico.
- Identifica la preferencia como dato reportado, no como demostración.

## Caso 3: límite con revisión de ADR

### Entrada
«Este ADR ya fue aprobado. Resúmelo para dirección en diez líneas; no lo revises ni publiques.»

### Criterios esperados
- Conserva la decisión y su estado.
- Resume el material recibido sin abrir una auditoría completa, cambiar archivos o publicarlo.
- Si falta el ADR, solicita el contenido indispensable sin atribuirle motivos ficticios.
