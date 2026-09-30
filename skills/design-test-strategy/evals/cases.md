# Casos de evaluación

## Normal: reintento de pago
### Entrada
Servicio procesa PaymentRequested con paymentId. Un mensaje puede duplicarse; el contrato exige como máximo un cargo por paymentId. Se persiste estado en SQL y se llama a proveedor externo. Pide estrategia, sin ejecutar.
### Criterios esperados
Prioriza idempotencia, fallos entre cargo/persistencia, duplicados concurrentes y reconciliación; distingue unitarias de integración y contrato del proveedor, no basta mock que siempre responde OK. No inventa atomicidad entre proveedor y SQL.

## Información ausente
### Entrada
“Escribe casos para calcular descuentos. Solo dice descuentos especiales; no hay reglas ni ejemplos.”
### Criterios esperados
No inventa porcentajes, acumulación o elegibilidad. Identifica reglas/oráculos faltantes y puede proponer estructura de casos condicionados sin presentarlos como aceptación aprobada.

## Límite de alcance
### Entrada
“Corrige un error tipográfico en documentación.”
### Criterios esperados
Usa comprobación proporcionada; no exige unitarias, integración ni umbral de cobertura.

## Prueba con falsa confianza
### Entrada
La suite prueba migraciones sustituyendo la base por un mock que siempre confirma success. Debe cambiar una restricción única en producción.
### Criterios esperados
Explica que el mock no verifica semántica de la restricción/migración; propone integración en motor/versión pertinentes con datos conflictivos, compatibilidad y recuperación, sin ejecutar en producción.

