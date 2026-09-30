# Procedimiento

## Punto de partida
Aclara el rol y la responsabilidad que se asumirá, la primera tarea real, tiempo disponible, experiencia previa y restricciones de acceso. Si faltan, ofrece un plan adaptable con supuestos visibles; no impongas semanas o horas inexistentes.

Inspecciona documentación del proyecto, glosario, requisitos, diagramas, repositorio, pruebas y runbooks accesibles. Prioriza fuentes cercanas al comportamiento observado y registra contradicciones entre documento, código y relato. El código demuestra implementación; no convierte automáticamente una regla accidental en una regla de negocio aprobada.

## Mapa de comprensión
Relaciona actores, lenguaje del dominio, capacidades, eventos, estados, invariantes y excepciones conocidas. Traza pocos recorridos críticos completos: entrada del usuario/sistema, decisión del negocio, persistencia, integración y resultado observable. Ubica ownership de datos, límites de dominio, contratos, dependencias, ejecución asíncrona y fallas relevantes. Señala lo no especificado sin completar reglas imaginarias.

Identifica decisiones arquitectónicas y motivos documentados; separa motivos confirmados de inferencias. Incluye cómo ejecutar y verificar un cambio local, dónde observar fallos y quién decide cuestiones de negocio/operación si se conoce.

## Secuencia práctica
Ordena actividades según dependencias y valor para la primera responsabilidad. Combina lectura de artefactos, recorrido de código, ejecución autorizada de pruebas y explicación del flujo. Vincula cada actividad a una pregunta que resuelve y a una comprobación: explicar una invariante, localizar su implementación, reproducir un escenario o proponer un cambio acotado.

Incluye una primera contribución reversible si el usuario desea trabajar en el sistema. No realices cambios, envíes preguntas a terceros o solicites permisos externos solo porque estén previstos en el plan. Redacta las preguntas para el owner cuando haga falta, y distingue candidatos de personas verificadas.

## Evidencia y mantenimiento
Entrega un mapa compacto de lo comprendido, las fuentes y las dudas; evita copiar manuales enteros. Usa referencias del proyecto existentes. Si el usuario autoriza conservar documentación, indica qué artefactos deben mantenerse y cómo saber que se quedaron obsoletos.

Consulta documentación oficial para tecnologías/versiones que condicionan los recorridos. O'Reilly mediante oreilly-research disponible puede cubrir fundamentos faltantes, sin sustituir reglas del negocio local. Aplica references/evidence-contract.md y no llames recursivamente a evidence-guided-development.

