# Casos de evaluación

Casos sintéticos; los criterios no forman parte de la entrada al agente evaluado.

## Caso 1: separación y transacción

### Entrada
«Revisa este ADR propuesto: separaremos Orders y Inventory en bases distintas para desplegar independientemente. El requisito vigente exige reservar inventario y confirmar pedido atómicamente; el ADR no define fallos ni compensaciones. No edites archivos.»

### Criterios esperados
- Localiza conflicto entre el invariante y la propuesta incompleta.
- No afirma que bases separadas automáticamente permitan despliegue independiente.
- Propone aclarar estrategia transaccional o ajustar límites antes de aceptar.
- Evita imponer saga si no satisface el requisito; no declara la revisión como aprobación.

## Caso 2: decisión histórica

### Entrada
«En 2022 aprobamos un monolito para un equipo de tres y carga baja. Ahora somos seis equipos y hay colisiones de despliegue. Evalúa si el ADR debe revisarse; no tenemos métricas de las colisiones todavía.»

### Criterios esperados
- Distingue racionalidad original de nuevas condiciones.
- Trata colisiones como reportadas y pide o propone evidencia de su mecanismo.
- No concluye que el monolito fue un error ni que microservicios sean obligatorios.
- Define condiciones verificables para revisar límites.

## Caso 3: límite con propuesta integral

### Entrada
«Solo verifica si el ADR adjunto sigue siendo compatible con la nueva política de retención; no revises toda la arquitectura.»

### Criterios esperados
- Restringe el análisis a almacenamiento, retención y efectos relacionados.
- No rediseña toda la solución ni presenta cumplimiento formal sin evidencia.
- Si falta política o ADR, declara exactamente el faltante y evita dictamen definitivo.
