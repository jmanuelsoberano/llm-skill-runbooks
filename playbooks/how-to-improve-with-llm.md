# Cómo mejorar una skill con ayuda de otro LLM

## Prompt recomendado

```markdown
Actúa como arquitecto de prompts y revisor de calidad.

Lee estos archivos:

- AGENTS.md
- conventions/prompt-style-guide.md
- skills/[skill]/skill.md
- skills/[skill]/input.schema.md
- skills/[skill]/output.schema.md
- skills/[skill]/prompt.full.md
- skills/[skill]/evals/checklist.md

Objetivo:
[Describe la mejora que quiero]

Restricciones:
- No rompas el contrato de salida.
- Si propones romperlo, sugiere versión major.
- Mantén compatibilidad con LLMs genéricos.
- Actualiza changelog.
- Propón pruebas.

Devuelve:
1. Diagnóstico.
2. Cambios propuestos.
3. Prompt actualizado.
4. Riesgos.
5. Versión sugerida.
6. Pruebas recomendadas.
```

## Revisión humana

Antes de aceptar cambios:

- verifica que no invente reglas;
- verifica que no elimine secciones;
- verifica que mantenga los valores controlados;
- ejecuta al menos una prueba manual.
