# Selección de especialidades

Seleccionar por el resultado solicitado y el riesgo concreto. No ejecutar todo el catálogo. Invocar una skill aquí significa aplicar sus instrucciones si está descubierta/accesible; no presupone un servicio de orquestación. Si falta, continuar con el método general y las herramientas presentes, declarando la limitación que afecte al resultado.

| Necesidad | Especialista | Resultado |
|---|---|---|
| Evidencia O'Reilly | oreilly-research | Pasajes, contraste y trazabilidad |
| Resumen para decidir/comunicar | create-decision-brief | Opciones, recomendación y riesgos |
| Pronóstico de entrega | forecast-project-delivery | Escenarios con datos e incertidumbre |
| Responsabilidades entre equipos | assess-team-structure | Dependencias y alternativas organizativas |
| Elegir implementación | compare-implementation-approaches | Comparación y comprobación discriminante |
| Revisar ADR/decisión arquitectónica | review-architecture-decision | Supuestos, consecuencias y reversibilidad |
| Revisar RFC/propuesta integral | review-technical-proposal | Coherencia, vacíos y viabilidad |
| Riesgo de seguridad solicitado o concreto | evaluate-security-risk | Amenazas, controles y verificaciones |
| Confiabilidad del servicio | plan-service-reliability | Objetivos y recuperación |
| IA en producción | plan-production-ready-ai | Evaluación, controles y operación |
| Incorporación a dominio/sistema | plan-domain-rampup | Comprensión y trabajo guiado |
| Aprendizaje de competencia | create-learning-plan | Estudio, práctica y avances |
| Revisar código/PR | review-code-change | Hallazgos localizados por severidad |
| Cambiar datos/migración | design-data-change | Integridad, compatibilidad y transición |
| Rendimiento | analyze-system-performance | Mediciones y experimentos |
| Incidente técnico | investigate-technical-incident | Diagnóstico, mitigación y pendientes |
| Estrategia de pruebas | design-test-strategy | Cobertura por riesgo y contratos |
| Extraer requisitos de fuentes | technical-requirements-extractor | Confirmados, inferidos y preguntas |
| Preparar backlog | repository-issue-generator | Issues y criterios de aceptación |

## Flujo sin ciclos

EGD identifica el objetivo y elige especialista; el especialista obtiene evidencia cuando hace falta y devuelve su artefacto. Los especialistas no vuelven a invocar EGD. Al consolidar, conservar IDs de evidencia y resolver discrepancias por contexto, no por votación. No repetir toda la investigación por cada etapa.

Un especialista puede usarse directamente. Implementación, refactorización, reglas de negocio, HU y documentación siguen siendo entregables de EGD; utilizar los especialistas que aporten al riesgo concreto. No convertir una petición de implementar en una cadena interminable de análisis.

## Otras fuentes

- Código/pruebas/configuración: inspeccionar lo pertinente y su versión; distinguir lectura estática de ejecución.
- Documentación oficial: verificar versión, contrato, límites y compatibilidad vigentes.
- Artículos académicos: comprobar método, contexto y límites, además de conclusiones.
- Benchmarks: aplicar controles de carga, entorno, caché, unidades y comparación de analyze-system-performance cuando corresponda.
- Observaciones de producción: distinguir registros inspeccionados, reportes y causalidad; usar investigate-technical-incident cuando haya un incidente.

Estas vías no requieren skills proveedoras adicionales. Mantener consulta mínima, procedencia y alcance según el contrato común.
