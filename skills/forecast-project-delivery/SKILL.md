---
name: forecast-project-delivery
description: "Evalúa escenarios de fechas o alcance de entrega usando flujo histórico, trabajo restante, dependencias e incertidumbre. Úsala para pronósticos y riesgos de planificación; no convierte estimaciones en compromisos ni calcula probabilidades sin datos y método explícitos."
metadata:
  id: "engineering.delivery.forecast"
  version: "0.1.0"
  status: "experimental"
---

# Pronóstico de entrega

Estimar escenarios de entrega que puedan actualizarse con nuevos datos, separando una fecha objetivo, un pronóstico sustentado y un compromiso acordado.

## Ejecución

1. Lee [prompt.full.md](prompt.full.md) y aplica el procedimiento al contexto real.
2. Interpreta entradas mediante [input.schema.md](input.schema.md) y entrega el artefacto de [output.schema.md](output.schema.md); no exige un formulario.
3. Lee [references/evidence-contract.md](references/evidence-contract.md) al manejar evidencia. Conserva sus identificadores y sus límites.
4. Usa fuentes pertinentes y herramientas disponibles. `oreilly-research` es una capacidad opcional; si el usuario solicita su uso, intenta el acceso y reporta bloqueos.

Puede utilizarse directamente o entregar resultados a `evidence-guided-development`, sin invocarla recursivamente. No requiere O'Reilly ni Expert MCP. Preserva el alcance y no publica resultados por iniciativa propia.

Para mantenimiento, usa [evals/checklist.md](evals/checklist.md), [evals/cases.md](evals/cases.md) y los ejemplos sintéticos en [examples/sample-input.md](examples/sample-input.md) y [examples/sample-output.md](examples/sample-output.md). Los criterios de evaluación no son hechos del caso del usuario.
