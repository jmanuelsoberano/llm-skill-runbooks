# Casos de evaluación

## Normal: nuevo ownership
### Entrada
Ingeniero hereda servicio de reservas. Debe corregir cancelaciones en dos semanas. Hay README, estados Booking y pruebas; una regla de reembolso difiere entre ticket y código. Dispone de seis horas para incorporación antes del cambio.
### Criterios esperados
Prioriza flujo de cancelación, estados/invariantes, transacciones y pruebas; registra contradicción de negocio y owner pendiente; programa actividades dentro de seis horas con incertidumbre y evita curso genérico de microservicios.

## Información ausente
### Entrada
“Me incorporo al equipo de liquidaciones, pero aún no tengo acceso al repo ni sé quién aprueba reglas.”
### Criterios esperados
Ofrece mapa de preguntas y materiales a localizar, actividades que sí pueden realizarse y bloqueos; no inventa flujos financieros ni responsables.

## Límite de alcance
### Entrada
“Quiero aprender Rust desde cero; no estoy trabajando en un sistema específico.”
### Criterios esperados
Reconoce plan de aprendizaje general; no inventa dominio empresarial ni onboarding de un repositorio.

## Documento desactualizado
### Entrada
README dice procesamiento síncrono, código aportado encola trabajos y tests verifican transición Pending → Completed.
### Criterios esperados
Expone la discrepancia; considera el código/pruebas evidencia del comportamiento implementado, con ejecución pendiente si no se corrió; investiga decisión/contrato sin atribuir intención desconocida.

