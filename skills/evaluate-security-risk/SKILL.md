---
name: evaluate-security-risk
description: "Evalúa riesgos de seguridad de un cambio, propuesta o sistema a partir de activos, actores, flujos y límites de confianza. Úsala para modelar amenazas, priorizar controles y definir verificaciones; la revisión general de código y la ejecución de pruebas intrusivas tienen alcance propio."
metadata:
  id: "security.risk.evaluate"
  version: "0.1.0"
  status: "experimental"
---

# Evaluación de riesgos de seguridad

Identifica cómo un cambio puede comprometer activos concretos y qué controles y comprobaciones reducen ese riesgo. Adapta la profundidad a las superficies expuestas y al impacto.

Al usar esta skill:

1. Lee [prompt.full.md](prompt.full.md) para el procedimiento específico.
2. Interpreta el contexto con [input.schema.md](input.schema.md) y conserva el contrato de [output.schema.md](output.schema.md), ajustando profundidad al pedido.
3. Lee [references/evidence-contract.md](references/evidence-contract.md) para distinguir procedencia, comprobación y aplicabilidad. Reutiliza evidencia pertinente ya obtenida, revalidando lo sensible a cambios.

Funciona por sí sola y puede recibir una tarea de otro flujo. Investiga fuentes en proporción al riesgo; usa `oreilly-research` cuando aporte y esté descubierta. No exige O'Reilly ni herramientas Expert. No llama de regreso al coordinador. Conserva el alcance del usuario y sus autorizaciones.

Los [casos](evals/cases.md), [criterios de evaluación](evals/checklist.md) y [ejemplo](examples/sample-output.md) sirven para mantener la skill; no son hechos sobre el proyecto del usuario.

