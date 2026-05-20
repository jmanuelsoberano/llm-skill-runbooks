---
id: repository.issue.generator
name: Generador de issues para repositorio
version: 0.1.0
status: draft
category: software
tags:
  - github
  - gitlab
  - issues
  - backlog
input_types:
  - markdown
  - text
output_formats:
  - markdown
  - yaml
llm_compatibility:
  - generic-llm
  - ChatGPT
  - Claude
  - Gemini
---

# Skill: Generador de issues para repositorio

## Propósito

Convertir un análisis de reunión, documento de requerimientos o nota técnica en issues listos para GitHub, GitLab, Jira u otra herramienta de seguimiento.

## Cuándo usarla

- Después de ejecutar `meeting-transcript-analysis`.
- Cuando tengas requerimientos desordenados.
- Cuando necesites pasar acuerdos a backlog técnico.

## Salida esperada

Issues con título, tipo, descripción, criterios de aceptación, prioridad, dependencias, etiquetas y preguntas pendientes.
