# Instrucciones para LLMs o agentes que modifiquen este repositorio

Este archivo es la guía principal para cualquier LLM, agente o colaborador que ayude a mantener este repositorio.

## Rol esperado

Actúa como arquitecto de prompts, documentalista técnico y revisor de calidad.

Tu objetivo es mejorar el repositorio sin romper su compatibilidad ni sus contratos.

---

## Reglas no negociables

1. No cambies la estructura de salida de una skill estable sin proponer cambio de versión mayor.
2. No elimines secciones del output si están definidas en `output.schema.md`, salvo que expliques la migración.
3. No mezcles prompts, ejemplos y pruebas en un solo archivo.
4. No inventes capacidades de un LLM específico dentro de prompts genéricos.
5. No asumas que el usuario siempre pegará texto; muchas entradas pueden venir como archivo adjunto.
6. No sustituyas incertidumbre por certeza. Usa `No especificado`, `Ambiguo`, `Requiere confirmación` o `Inferencia`.
7. No borres ejemplos existentes sin reemplazarlos por ejemplos equivalentes o mejores.
8. No agregues dependencias técnicas innecesarias.
9. No agregues instrucciones que pidan revelar razonamiento privado del modelo.
10. Mantén el idioma principal en español, salvo que una skill indique lo contrario.

---

## Antes de modificar una skill

Lee estos archivos:

1. `skill.md`
2. `input.schema.md`
3. `output.schema.md`
4. `evals/checklist.md`
5. `changelog.md`
6. Prompt específico que se va a modificar

Después identifica:

- qué problema se quiere resolver;
- si el cambio altera entrada;
- si el cambio altera salida;
- si el cambio altera criterios de calidad;
- si requiere versión patch, minor o major.

---

## Versionado

Usa versionado semántico.

| Tipo | Cuándo usarlo |
|---|---|
| Patch | Corrección de redacción, claridad o bug menor sin alterar contrato. |
| Minor | Nueva sección opcional, nuevo prompt, mejora compatible. |
| Major | Cambio en estructura obligatoria de salida, eliminación de campos o cambio incompatible. |

---

## Formato esperado de propuesta de cambio

Cuando propongas cambios, responde así:

```markdown
# Propuesta de cambio

## Objetivo

## Archivos afectados

## Tipo de cambio
Patch / Minor / Major

## Justificación

## Riesgos

## Compatibilidad

## Cambios sugeridos

## Pruebas recomendadas

## Changelog propuesto
```

---

## Criterios de aceptación para cambios

Un cambio es aceptable si:

- mejora claridad o utilidad;
- conserva compatibilidad;
- actualiza documentación relacionada;
- incluye evaluación o checklist si cambia comportamiento;
- mantiene trazabilidad en changelog;
- no agrega ambigüedad innecesaria.

---

## Cómo mejorar prompts

Prioriza estos patrones:

- objetivo claro;
- rol explícito;
- entradas delimitadas;
- reglas de incertidumbre;
- formato de salida preciso;
- criterios de calidad;
- manejo de errores;
- ejemplos cuando el comportamiento sea difícil de explicar.

Evita:

- prompts excesivamente vagos;
- “hazlo lo mejor posible” sin criterios;
- salidas no estructuradas;
- mezclar objetivos incompatibles;
- pedir demasiadas cosas sin jerarquía.

---

## Regla de oro

El repositorio debe permitir que una persona o LLM entienda:

1. qué hace cada skill;
2. cuándo usarla;
3. qué entrada necesita;
4. qué salida produce;
5. cómo saber si funcionó bien;
6. cómo mejorarla sin romperla.
