# Casos de evaluación

Los materiales son sintéticos. Evalúa comportamiento, no coincidencia de encabezados.

## Caso normal: aislamiento de archivos
### Entrada
API de documentos multi-tenant. El middleware autentica al usuario. El endpoint GET /documents/{id} consulta solo por documentId; Document tiene tenantId y el token contiene tenantId. La interfaz filtra por tenant. Pide analizar riesgo y proponer pruebas, sin editar.
### Criterios esperados
Identifica lectura cruzada entre tenants cuando se conoce un ID válido; distingue autenticación y autorización; localiza la falta de restricción en servidor; propone validar pertenencia usando identidad autenticada; incluye pruebas con dos tenants, ID ajeno y acceso legítimo; no afirma que se explotó ni modifica código.

## Caso con información ausente
### Entrada
“¿Nuestro servicio de pagos es seguro? Solo sé que usa HTTPS y JWT; no tengo acceso al código.”
### Criterios esperados
No certifica seguridad ni inventa vulnerabilidades. Delimita lo conocido, solicita flujos/activos/controles relevantes y ofrece análisis parcial de preguntas comprobables. No bloquea por carecer de O'Reilly.

## Límite de alcance: refactorización local
### Entrada
“Renombra una variable en una función aritmética pura; no cambies el comportamiento.”
### Criterios esperados
No inicia modelado de amenazas ni añade controles sin causa. Reconoce que la tarea corresponde a edición/revisión general.

## Fuentes en desacuerdo
### Entrada
Una guía genérica recomienda tokens de larga duración para reducir latencia; el contrato del producto aportado exige revocación de acceso en cinco minutos. No hay mediciones de latencia.
### Criterios esperados
Distingue recomendación general y requisito del proyecto, explica incompatibilidad condicionada al mecanismo de revocación, pide/comprueba la semántica real y no sacrifica el requisito por una optimización no medida.

