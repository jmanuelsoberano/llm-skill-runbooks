---
name: repository-issue-generator
description: Convierte requerimientos, minutas o notas técnicas en un backlog de issues
  con criterios de aceptación, dependencias y preguntas pendientes. Úsala para preparar
  tickets de GitHub, GitLab o Jira, agrupar duplicados y separar trabajo accionable
  de propuestas todavía indefinidas.
metadata:
  id: repository.issue.generator
  version: 0.3.0
  status: draft
---

# Skill: Generador de issues para repositorio

## Ejecución como Agent Skill

1. Lee [input.schema.md](input.schema.md) y usa el documento o contexto proporcionado, sin exigir ejecutar antes otra skill.
2. Lee y aplica [prompt.full.md](prompt.full.md). Usa etiquetas, plantillas y prioridades del proyecto cuando estén disponibles; identifica como sugeridas las que propongas.
3. Cubre las seis secciones de [output.schema.md](output.schema.md), incluidas las preguntas globales antes de implementar, además de las preguntas por issue. Conserva el formato de cada issue y agrupa duplicados sin inventar requisitos.
4. Revisa el resultado con [evals/checklist.md](evals/checklist.md).

Genera el backlog solicitado en Markdown. Crear tickets en una herramienta externa depende de que la petición también lo autorice y de disponer de la conexión correspondiente; la skill no concede acceso ni autorización adicionales.

Para mantenimiento, usa [evals/agent-cases.md](evals/agent-cases.md).

## Propósito

Convertir un análisis de reunión, documento de requerimientos o nota técnica en issues listos para GitHub, GitLab, Jira u otra herramienta de seguimiento.

## Cuándo usarla

- Después de ejecutar `meeting-transcript-analysis`.
- Cuando tengas requerimientos desordenados.
- Cuando necesites pasar acuerdos a backlog técnico.

## Salida esperada

Issues con título, tipo, descripción, criterios de aceptación, prioridad, dependencias, etiquetas y preguntas pendientes.

## Evidencia e integración

Aplicar el [contrato compartido](references/evidence-contract.md) cuando se reciban hallazgos de otras skills. Conservar IDs en las columnas o secciones existentes, sin exigir otro flujo previo ni convertir una recomendación bibliográfica en requisito confirmado. Puede utilizarse directamente; no invocar EGD de forma recursiva.
