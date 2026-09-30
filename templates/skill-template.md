---
name: domain-skill-name
description: "Describe la capacidad y las peticiones concretas que deben activarla. Sustituye este texto antes de incorporar la skill."
metadata:
  id: "domain.skill.name"
  version: "0.1.0"
  status: "draft"
---

# Nombre de la skill

Define el resultado y los límites específicos de esta capacidad.

## Procedimiento

1. Lee [input.schema.md](input.schema.md) y aprovecha el contexto ya proporcionado.
2. Lee y aplica [prompt.full.md](prompt.full.md). Añade otras variantes solo si resuelven necesidades distintas y explica aquí cuándo usarlas.
3. Entrega lo definido en [output.schema.md](output.schema.md).
4. Comprueba los criterios de [evals/checklist.md](evals/checklist.md).

Sustituye las instrucciones de plantilla por reglas concretas que ayuden al agente a decidir. Mantén los recursos dentro del paquete y no presupongas herramientas ausentes.

Para mantenimiento, consulta [changelog.md](changelog.md). Registra nombre visible, categoría, etiquetas y formatos en la entrada correspondiente de `registry.yaml`.
