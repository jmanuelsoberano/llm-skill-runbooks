# Contrato de entrada

Acepta lenguaje natural, código, repositorios, HU, documentos, incidencias y evidencia técnica accesibles con autorización. No requiere JSON ni un formulario. La entrada mínima es una tarea identificable y su contexto disponible; para un cambio mecánico basta con el archivo o texto afectado.

Infiere el modo de las instrucciones: analizar, planificar, implementar, refactorizar, revisar, probar o documentar. Si hay ambigüedad que pueda causar una modificación no deseada, aclara esa intención mientras avanzas con inspección segura.

Usa los datos relevantes, sin exigirlos todos:

| Dato | Para qué sirve |
|---|---|
| Resultado solicitado y límites | Elegir el artefacto y el alcance autorizado. |
| Comportamiento actual y esperado | Preservar contratos o implementar la variación pedida. |
| Reglas, invariantes, actores y ejemplos | Modelar el dominio y redactar criterios comprobables. |
| Código, pruebas, tecnologías y versiones | Entender patrones existentes y compatibilidad. |
| Datos, consumidores y topología | Evaluar impacto y transición. |
| Dependencias, propietarios y restricciones | Identificar responsabilidades y opciones viables. |
| Métricas, trazas, incidentes y fechas | Sustentar hipótesis de rendimiento u operación. |
| Fuentes y herramientas accesibles | Delimitar qué puede verificarse. |

Marca ausencias relevantes como `No especificado`, contradicciones como `Ambiguo`, propuestas pendientes como `Requiere confirmación` y conclusiones derivadas como `Inferencia`. Un reporte del usuario no equivale a una medición inspeccionada.

Si un archivo no se puede leer, identifica la limitación y trabaja con lo restante. Solicita la mínima evidencia adicional necesaria, preferentemente anonimizada; no solicites credenciales dentro del chat. Las nuevas reglas de negocio que cambien el comportamiento requieren sustento en el contexto o una aclaración, no una suposición extraída de bibliografía.

Puede recibir hallazgos previos con evidence_id y procedencia según references/evidence-contract.md. Son opcionales: no cambia la entrada mínima ni se exige invocar otra skill. Revalidar lo que dependa de una versión o estado modificado.
