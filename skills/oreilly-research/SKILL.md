---
name: oreilly-research
description: "Investiga y contrasta afirmaciones en O'Reilly mediante búsqueda, Answers y lectura de pasajes accesibles. Úsala al pedir fuentes de O'Reilly, verificar una cita o reunir evidencia técnica trazable; también puede apoyar a otras skills."
metadata:
  id: research.oreilly
  version: 0.1.0
  status: experimental
---

# Investigación con O'Reilly

1. Interpreta la pregunta con [input.schema.md](input.schema.md).
2. Sigue [prompt.full.md](prompt.full.md) y el [contrato de evidencia](references/evidence-contract.md).
3. Antes de usar servicios, consulta [capacidades y acceso](references/capabilities.md); no asumas una sesión activa ni herramientas Expert.
4. Entrega [output.schema.md](output.schema.md): hallazgos verificados, discrepancias y pendientes. Puede utilizarse directamente, sin otra skill.
5. Para mantenimiento: [casos](evals/cases.md) y [checklist](evals/checklist.md). Los ejemplos son sintéticos, no pruebas de acceso real.

No sustituye el motor de Expert ni promete su cobertura. La aplicación final al sistema corresponde al trabajo solicitado y a su evidencia local.
