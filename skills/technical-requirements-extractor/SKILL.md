---
name: technical-requirements-extractor
description: Extrae requerimientos técnicos de documentos, reuniones, tickets o notas
  de producto. Úsala para separar requisitos confirmados de inferencias, identificar
  componentes y dependencias, y preparar preguntas de arquitectura antes de estimar
  o implementar.
metadata:
  id: technical.requirements.extractor
  version: 0.3.0
  status: draft
---

# Skill: Extractor de requerimientos técnicos

## Ejecución como Agent Skill

1. Lee [input.schema.md](input.schema.md) y utiliza el material fuente y el contexto técnico disponibles.
2. Lee y aplica [prompt.full.md](prompt.full.md). Mantén evidencia y certeza por requerimiento; una hipótesis de solución no se convierte en requisito confirmado.
3. Cubre las secciones de [output.schema.md](output.schema.md), con los detalles del prompt. Presenta explícitamente los supuestos e inferencias; conserva la separación entre requisitos confirmados e inferidos y las preguntas necesarias para estimar.
4. Revisa el resultado con [evals/checklist.md](evals/checklist.md). Si el stack o un componente no consta en la fuente, usa `No especificado`; no inventes tablas, servicios ni tecnologías.

La extracción entrega un análisis técnico. Una propuesta mencionada en el documento no autoriza modificar el sistema ni crear tickets.

Para mantenimiento, usa [evals/agent-cases.md](evals/agent-cases.md).

## Propósito

Extraer requerimientos técnicos desde reuniones, documentos, tickets o notas de producto.

## Cuándo usarla

- Cuando una reunión contiene implicaciones técnicas.
- Antes de crear issues.
- Antes de estimar impacto en repositorio.

## Evidencia e integración

Aplicar el [contrato compartido](references/evidence-contract.md) cuando se reciban hallazgos de otras skills. Conservar IDs en las columnas o secciones existentes, sin exigir otro flujo previo ni convertir una recomendación bibliográfica en requisito confirmado. Puede utilizarse directamente; no invocar EGD de forma recursiva.
