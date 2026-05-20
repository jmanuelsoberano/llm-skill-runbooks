# Guía de estilo para prompts

Esta guía define cómo escribir prompts reutilizables entre LLMs.

## Estructura recomendada

Usa esta estructura base:

```markdown
# Identity

# Objective

# Input

# Instructions

# Process

# Output format

# Quality rules

# Failure handling

# User input
```

## Principios

### 1. Instrucciones claras

Explica exactamente qué debe hacer el modelo.

Mal:

```text
Analiza esto.
```

Mejor:

```text
Analiza el transcript, extrae decisiones, compromisos, riesgos, requerimientos y próximos pasos.
```

### 2. Entrada delimitada

Usa delimitadores para separar instrucciones de datos.

```xml
<context>
...
</context>

<transcript>
...
</transcript>
```

### 3. Salida explícita

Define títulos, tablas y campos esperados.

### 4. Manejo de incertidumbre

Incluye instrucciones como:

```text
No inventes información. Si algo no está claro, marca “No especificado”, “Ambiguo” o “Requiere confirmación”.
```

### 5. Compatibilidad

Evita depender de funciones específicas, salvo en adaptadores.

### 6. Modularidad

Si una tarea es muy grande, divídela en skills o variantes.

---

## Plantilla corta

```markdown
Actúa como [rol].

Objetivo:
[objetivo]

Entrada:
[entrada esperada]

Instrucciones:
- [regla]
- [regla]

Salida:
[formato exacto]

Criterios de calidad:
- [criterio]
```

---

## Qué evitar

- Prompts sin formato de salida.
- Pedir “todo” sin jerarquía.
- Instrucciones contradictorias.
- Exigir certeza cuando la entrada es ambigua.
- Mezclar análisis, escritura creativa y decisiones técnicas sin delimitación.
- Poner datos variables dentro del prompt base sin marcadores.
