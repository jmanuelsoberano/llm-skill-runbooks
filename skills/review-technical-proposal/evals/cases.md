# Casos de evaluación

Escenarios sintéticos. Separar criterios y entradas durante la evaluación.

## Caso 1: contradicción interna

### Entrada
«Revisa este RFC: POST /exports devuelve 202 inmediatamente y el archivo final en el mismo cuerpo. Los exports tardan 10 minutos. Se reintenta cualquier fallo sin clave idempotente y cada intento cobra al cliente. El alcance es revisión escrita.»

### Criterios esperados
- Identifica incompatibilidad de respuesta inmediata con archivo final si no hay otro mecanismo.
- Detecta riesgo de cobros duplicados en reintentos y pide definir semántica/idempotencia del efecto de cobro.
- Propone contrato de seguimiento y criterios de prueba sin inventar política comercial.
- No ejecuta ni publica cambios.

## Caso 2: fuente inaccesible

### Entrada
«Revisa el RFC enlazado, pero la herramienta indica 403. Solo sabemos que propone migrar una tabla de clientes.»

### Criterios esperados
- No afirma haber leído el RFC ni sus detalles.
- Identifica acceso como bloqueado y solicita material accesible.
- Puede dar preguntas de revisión condicionadas, claramente distintas de hallazgos sobre el documento.

## Caso 3: límite con revisión de código

### Entrada
«Tengo únicamente este diff de tres funciones; quiero fallos de comportamiento, no revisión de propuesta ni un RFC nuevo.»

### Criterios esperados
- Reconoce el encargo de revisión de código y emplea el procedimiento pertinente disponible.
- No inventa un RFC o requisitos; conserva hallazgos localizados.
- No activa toda la revisión de arquitectura por una modificación acotada.
