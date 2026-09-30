---
name: create-learning-plan
description: "Crea un plan de aprendizaje de una tecnología o competencia con objetivos, prerrequisitos, práctica y comprobaciones de progreso. Úsala para estudio deliberado o desarrollo profesional; conocer un dominio y sistema empresarial concreto corresponde a incorporación al dominio."
metadata:
  id: "learning.plan.create"
  version: "0.1.0"
  status: "experimental"
---

# Plan de aprendizaje técnico

Transforma una intención de aprender en una secuencia realista de estudio y práctica, adaptada al nivel y tiempo disponibles, con resultados comprobables.

Al usar esta skill:

1. Lee [prompt.full.md](prompt.full.md) para el procedimiento específico.
2. Interpreta el contexto con [input.schema.md](input.schema.md) y conserva el contrato de [output.schema.md](output.schema.md), ajustando profundidad al pedido.
3. Lee [references/evidence-contract.md](references/evidence-contract.md) para distinguir procedencia, comprobación y aplicabilidad. Reutiliza evidencia pertinente ya obtenida, revalidando lo sensible a cambios.

Funciona por sí sola y puede recibir una tarea de otro flujo. Investiga fuentes en proporción al riesgo; usa `oreilly-research` cuando aporte y esté descubierta. No exige O'Reilly ni herramientas Expert. No llama de regreso al coordinador. Conserva el alcance del usuario y sus autorizaciones.

Los [casos](evals/cases.md), [criterios de evaluación](evals/checklist.md) y [ejemplo](examples/sample-output.md) sirven para mantener la skill; no son hechos sobre el proyecto del usuario.

