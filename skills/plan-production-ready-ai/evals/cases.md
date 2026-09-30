# Casos de evaluación

## Normal: asistente con herramientas
### Entrada
Asistente interno consulta documentos y propone reembolsos. El prototipo puede ejecutar refund(orderId, amount). Hay 40 ejemplos del equipo pero no dataset independiente ni límites de permisos. Pide plan, sin implementar.
### Criterios esperados
Distingue consulta, propuesta y ejecución; define autorización/validación fuera del modelo, evaluación independiente por riesgo, prompt injection desde documentos, revisión humana según costo del error, aislamiento de datos, medición de costo/latencia y rollback que no deshace reembolsos.

## Información ausente
### Entrada
“Quiero predecir abandono de clientes; no tengo dataset ni baseline todavía.”
### Criterios esperados
Define etiqueta/horizonte y datos necesarios, partición temporal/entidad y fuga potencial; propone baseline y plan verificable, sin inventar exactitud ni afirmar que un modelo ya es adecuado.

## Límite de alcance
### Entrada
“¿Cómo se escribe una llamada HTTP al proveedor X? Solo necesito un ejemplo actual del SDK.”
### Criterios esperados
Mantiene la respuesta en uso de API/documentación vigente; no impone un programa completo de producción.

## Evaluación contaminada
### Entrada
El equipo ajustó prompts con las mismas 100 preguntas que llama conjunto de prueba; obtuvo 98% y quiere aprobar producción automáticamente.
### Criterios esperados
Identifica que el resultado no demuestra generalización independiente, propone un conjunto reservado y casos de riesgo, explica límites del porcentaje y no acepta un gate arbitrario.

