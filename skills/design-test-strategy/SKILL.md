---
name: design-test-strategy
description: "Diseña una estrategia de pruebas para un cambio o sistema a partir de invariantes, contratos y riesgos de regresión. Úsala para decidir escenarios, niveles, datos y criterios de aceptación; una edición trivial no requiere un programa de pruebas completo."
metadata:
  id: "engineering.test.strategy"
  version: "0.1.0"
  status: "experimental"
---

# Estrategia de pruebas

Define qué comportamientos deben comprobarse, en qué nivel y con qué datos, para reducir riesgos relevantes sin duplicar la implementación ni inflar la suite.

Al usar esta skill:

1. Lee [prompt.full.md](prompt.full.md) para el procedimiento específico.
2. Interpreta el contexto con [input.schema.md](input.schema.md) y conserva el contrato de [output.schema.md](output.schema.md), ajustando profundidad al pedido.
3. Lee [references/evidence-contract.md](references/evidence-contract.md) para distinguir procedencia, comprobación y aplicabilidad. Reutiliza evidencia pertinente ya obtenida, revalidando lo sensible a cambios.

Funciona por sí sola y puede recibir una tarea de otro flujo. Investiga fuentes en proporción al riesgo; usa `oreilly-research` cuando aporte y esté descubierta. No exige O'Reilly ni herramientas Expert. No llama de regreso al coordinador. Conserva el alcance del usuario y sus autorizaciones.

Los [casos](evals/cases.md), [criterios de evaluación](evals/checklist.md) y [ejemplo](examples/sample-output.md) sirven para mantener la skill; no son hechos sobre el proyecto del usuario.

