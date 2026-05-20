# Guía de evaluación

Las pruebas de prompts no buscan garantizar perfección absoluta. Buscan detectar regresiones y mantener consistencia.

## Tipos de evaluación

### 1. Checklist manual

Útil para revisión humana.

### 2. Evaluación con otro LLM

Un LLM actúa como juez usando rúbrica.

### 3. Golden examples

Se comparan salidas esperadas con salidas reales.

### 4. Pruebas estructurales

Verifican que la salida incluya secciones obligatorias.

## Criterios generales

Una buena salida debe:

- cumplir formato;
- no inventar;
- extraer acciones;
- separar hechos de inferencias;
- marcar ambigüedad;
- ser útil para alguien que no asistió;
- ser reutilizable por otra skill.

## Señales de regresión

- Faltan secciones obligatorias.
- Se inventan responsables.
- No hay evidencias.
- No distingue decisiones de propuestas.
- El resumen es demasiado superficial.
- El Markdown no se puede reutilizar.
