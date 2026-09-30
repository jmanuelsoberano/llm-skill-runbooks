---
name: review-architecture-decision
description: "Revisa una decisión arquitectónica concreta, ADR o cambio de límites con sus supuestos, alternativas, consecuencias y reversibilidad. Úsala para comprobar si una decisión se sostiene en el contexto del sistema; una revisión integral de RFC corresponde a review-technical-proposal."
metadata:
  id: "engineering.architecture.review"
  version: "0.1.0"
  status: "experimental"
---

# Revisión de decisión arquitectónica

Comprobar que una decisión arquitectónica es coherente con las fuerzas del sistema, sus restricciones y la evidencia disponible, y expresar hallazgos que permitan confirmarla, ajustarla o revisarla.

## Ejecución

1. Lee [prompt.full.md](prompt.full.md) y aplica el procedimiento al contexto real.
2. Interpreta entradas mediante [input.schema.md](input.schema.md) y entrega el artefacto de [output.schema.md](output.schema.md); no exige un formulario.
3. Lee [references/evidence-contract.md](references/evidence-contract.md) al manejar evidencia. Conserva sus identificadores y sus límites.
4. Usa fuentes pertinentes y herramientas disponibles. `oreilly-research` es una capacidad opcional; si el usuario solicita su uso, intenta el acceso y reporta bloqueos.

Puede utilizarse directamente o entregar resultados a `evidence-guided-development`, sin invocarla recursivamente. No requiere O'Reilly ni Expert MCP. Preserva el alcance y no publica resultados por iniciativa propia.

Para mantenimiento, usa [evals/checklist.md](evals/checklist.md), [evals/cases.md](evals/cases.md) y los ejemplos sintéticos en [examples/sample-input.md](examples/sample-input.md) y [examples/sample-output.md](examples/sample-output.md). Los criterios de evaluación no son hechos del caso del usuario.
