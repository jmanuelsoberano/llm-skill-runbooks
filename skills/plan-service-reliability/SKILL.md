---
name: plan-service-reliability
description: "Planifica confiabilidad de un servicio mediante recorridos críticos, SLIs, SLOs candidatos, dependencias, observabilidad y recuperación. Úsala para diseñar o mejorar operación; un incidente activo requiere diagnóstico y mitigación específicos."
metadata:
  id: "operations.reliability.plan"
  version: "0.1.0"
  status: "experimental"
---

# Plan de confiabilidad del servicio

Convierte expectativas de continuidad y experiencia del usuario en objetivos observables y un plan de operación y recuperación ajustado al servicio.

Al usar esta skill:

1. Lee [prompt.full.md](prompt.full.md) para el procedimiento específico.
2. Interpreta el contexto con [input.schema.md](input.schema.md) y conserva el contrato de [output.schema.md](output.schema.md), ajustando profundidad al pedido.
3. Lee [references/evidence-contract.md](references/evidence-contract.md) para distinguir procedencia, comprobación y aplicabilidad. Reutiliza evidencia pertinente ya obtenida, revalidando lo sensible a cambios.

Funciona por sí sola y puede recibir una tarea de otro flujo. Investiga fuentes en proporción al riesgo; usa `oreilly-research` cuando aporte y esté descubierta. No exige O'Reilly ni herramientas Expert. No llama de regreso al coordinador. Conserva el alcance del usuario y sus autorizaciones.

Los [casos](evals/cases.md), [criterios de evaluación](evals/checklist.md) y [ejemplo](examples/sample-output.md) sirven para mantener la skill; no son hechos sobre el proyecto del usuario.

