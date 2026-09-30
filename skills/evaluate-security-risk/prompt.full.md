# Procedimiento

## Delimitar el sistema y la decisión
Identifica cambio, entorno y alcance solicitado: diseño, código, configuración o revisión de controles. Lee los artefactos del proyecto disponibles. Ubica datos/activos protegidos, actores legítimos y adversarios plausibles, operaciones sensibles, entradas, componentes externos, privilegios, límites de confianza y consecuencias para integridad, confidencialidad y disponibilidad. Distingue sistema actual y diseño propuesto; marca flujos desconocidos.

## Formular amenazas concretas
Describe cada amenaza como actor/precondición → vía de ataque o abuso → activo/impacto. Busca fallos en las fronteras pertinentes: identidad frente a autorización, aislamiento de tenants, manejo de secretos, validación e interpretación de entradas, cadena de dependencias o privilegios operativos. No conviertas todas esas áreas en hallazgos por defecto. Un patrón vulnerable requiere evidencia del camino de exposición; si falta, trátalo como hipótesis con comprobación pendiente.

Considera abuso de funciones legítimas, accesos internos y errores operativos cuando el contexto lo justifique. Explica qué rompe el control propuesto y qué ataques quedan fuera de su cobertura. No confíes en controles de interfaz para proteger operaciones del servidor.

## Valorar y tratar
Prioriza con impacto, exposición, precondiciones, controles existentes y confianza de la evidencia. Usa la escala del proyecto si existe. Si no existe, utiliza crítico/importante/sugerencia con motivos; no inventes probabilidades, puntuaciones CVSS o cumplimiento normativo. Separa severidad del riesgo y certeza del hallazgo.

Propón el cambio mínimo efectivo, responsable candidato si se conoce, dependencias, compatibilidad y riesgo residual. Controles compensatorios y aceptación de riesgo son opciones que requieren dueño de decisión; no declares riesgo aceptado en su nombre.

## Verificar
Para cada riesgo prioritario define prueba observable: acción, identidad/tenant, condición inicial, resultado permitido/denegado y efecto sobre los datos. Añade comprobación de regresión del uso legítimo. Si se ejecutan pruebas autorizadas, registra entorno y resultados; si solo se propone el plan, no declares mitigación probada.

Esta skill no concede autorización para explotar, escanear sistemas ajenos o cambiar entornos. Respeta la autorización vigente de la tarea y no amplíes el objetivo del análisis. Evita extraer secretos; cuando sean relevantes, registra ubicación o categoría sin su valor.

## Fuentes y límites
Aplica references/evidence-contract.md. Consulta documentación oficial vigente cuando una conclusión dependa de versiones, configuración o controles de un producto. O'Reilly puede aclarar mecanismos mediante oreilly-research si está disponible; no es requisito ni acredita seguridad del sistema. Declara lo inaccesible y avanza con los artefactos útiles. No llames recursivamente a evidence-guided-development; devuelve resultados utilizables por el solicitante.

