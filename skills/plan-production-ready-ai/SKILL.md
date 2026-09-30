---
name: plan-production-ready-ai
description: "Prepara un plan para llevar una función con IA generativa o aprendizaje automático a producción. Úsala para definir evaluación, datos, seguridad, costos, integración y operación; no sustituye el análisis de negocio ni exige IA cuando una solución convencional basta."
metadata:
  id: "ai.production.plan"
  version: "0.1.0"
  status: "experimental"
---

# Plan para IA en producción

Determina qué evidencia y controles necesita una función de IA para cumplir su tarea en un entorno real, con aceptación medible, despliegue gradual y recuperación.

Al usar esta skill:

1. Lee [prompt.full.md](prompt.full.md) para el procedimiento específico.
2. Interpreta el contexto con [input.schema.md](input.schema.md) y conserva el contrato de [output.schema.md](output.schema.md), ajustando profundidad al pedido.
3. Lee [references/evidence-contract.md](references/evidence-contract.md) para distinguir procedencia, comprobación y aplicabilidad. Reutiliza evidencia pertinente ya obtenida, revalidando lo sensible a cambios.

Funciona por sí sola y puede recibir una tarea de otro flujo. Investiga fuentes en proporción al riesgo; usa `oreilly-research` cuando aporte y esté descubierta. No exige O'Reilly ni herramientas Expert. No llama de regreso al coordinador. Conserva el alcance del usuario y sus autorizaciones.

Los [casos](evals/cases.md), [criterios de evaluación](evals/checklist.md) y [ejemplo](examples/sample-output.md) sirven para mantener la skill; no son hechos sobre el proyecto del usuario.

