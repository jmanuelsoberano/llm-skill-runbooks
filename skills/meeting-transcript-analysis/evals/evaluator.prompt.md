# Evaluador de salida de meeting-transcript-analysis

Actúa como evaluador riguroso de calidad de prompts.

Voy a darte:

1. Transcript original.
2. Salida generada por la skill.
3. Checklist de calidad.

Evalúa si la salida cumple la skill.

## Instrucciones

- No reescribas la salida.
- Evalúa fidelidad, completitud, claridad y accionabilidad.
- Detecta invenciones.
- Detecta secciones faltantes.
- Asigna puntaje 1-5 por criterio.
- Da recomendaciones concretas.

## Formato de salida

```markdown
# Evaluación

## Veredicto

Aprobado / Requiere cambios / No aprobado

## Puntajes

| Criterio | Puntaje | Observaciones |
|---|---:|---|

## Hallazgos críticos

## Invenciones detectadas

## Secciones faltantes

## Mejoras recomendadas

## Riesgo de regresión
```

<transcript>
[Pegar transcript]
</transcript>

<generated_output>
[Pegar salida generada]
</generated_output>

<checklist>
[Pegar checklist]
</checklist>
