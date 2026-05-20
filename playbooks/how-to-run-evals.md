# Cómo correr evaluaciones

## Nivel 1: Validación estructural

```bash
python scripts/validate_repo.py
```

## Nivel 2: Checklist manual

1. Ejecuta el prompt con un ejemplo.
2. Abre `evals/checklist.md`.
3. Marca cada punto.
4. Anota fallos.

## Nivel 3: Evaluación con LLM juez

Usa:

```text
skills/[skill]/evals/evaluator.prompt.md
```

Pega:

- entrada original;
- salida generada;
- checklist.

## Nivel 4: Comparación contra ejemplo esperado

Compara la salida real con `examples/sample-output.md`.

No se busca coincidencia textual exacta. Se busca consistencia semántica y estructural.
