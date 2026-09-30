---
name: investigate-technical-incident
description: "Investiga un fallo técnico con síntomas, cronología, cambios, logs y métricas para delimitar impacto, contrastar hipótesis y proponer mitigación o prevención. Úsala en incidentes y análisis posterior; un plan general de SLOs o un benchmark aislado tienen otros objetivos."
metadata:
  id: "operations.incident.investigate"
  version: "0.1.0"
  status: "experimental"
---

# Investigación de incidente técnico

Reduce incertidumbre sobre un fallo y orienta acciones proporcionales al impacto, conservando evidencia y separando recuperación del servicio de causa demostrada.

Al usar esta skill:

1. Lee [prompt.full.md](prompt.full.md) para el procedimiento específico.
2. Interpreta el contexto con [input.schema.md](input.schema.md) y conserva el contrato de [output.schema.md](output.schema.md), ajustando profundidad al pedido.
3. Lee [references/evidence-contract.md](references/evidence-contract.md) para distinguir procedencia, comprobación y aplicabilidad. Reutiliza evidencia pertinente ya obtenida, revalidando lo sensible a cambios.

Funciona por sí sola y puede recibir una tarea de otro flujo. Investiga fuentes en proporción al riesgo; usa `oreilly-research` cuando aporte y esté descubierta. No exige O'Reilly ni herramientas Expert. No llama de regreso al coordinador. Conserva el alcance del usuario y sus autorizaciones.

Los [casos](evals/cases.md), [criterios de evaluación](evals/checklist.md) y [ejemplo](examples/sample-output.md) sirven para mantener la skill; no son hechos sobre el proyecto del usuario.

