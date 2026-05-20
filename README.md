# Prompt Skills Starter Kit

Repositorio base para crear, organizar, versionar, probar y reutilizar **skills de prompts** en distintos LLMs.

Una **skill** no es solo un prompt. Es una capacidad reutilizable con:

- propósito claro;
- contrato de entrada;
- contrato de salida;
- prompt principal;
- variantes del prompt;
- ejemplos;
- pruebas o criterios de evaluación;
- adaptadores para distintos LLMs;
- historial de cambios.

Este repositorio está pensado para que puedas usarlo con ChatGPT, Claude, Gemini, Copilot u otros LLMs, sin quedar atado a un proveedor específico.

---

## Cómo empezar

1. Lee este archivo completo.
2. Revisa `AGENTS.md` si vas a pedirle a un LLM que mejore este repositorio.
3. Abre `skills/meeting-transcript-analysis/`.
4. Usa `prompt.file-input.md` cuando tengas un transcript como archivo adjunto.
5. Usa `prompt.full.md` cuando pegues el transcript como texto o quieras el análisis más completo.
6. Usa `workflows/meeting-to-repository-followup.md` si quieres convertir el resultado en issues o tareas para un repositorio.

---

## Estructura general

```text
prompt-skills-starter-kit/
  README.md
  AGENTS.md
  registry.yaml
  conventions/
  templates/
  schemas/
  skills/
  workflows/
  playbooks/
  scripts/
  references/
```

### Carpetas importantes

| Carpeta | Propósito |
|---|---|
| `skills/` | Contiene las skills reutilizables. |
| `templates/` | Plantillas para crear nuevas skills. |
| `conventions/` | Reglas internas del repositorio. |
| `schemas/` | Contratos técnicos de metadatos y pruebas. |
| `workflows/` | Cómo combinar varias skills. |
| `playbooks/` | Guías prácticas para mantener y mejorar el repo. |
| `scripts/` | Validaciones básicas del repositorio. |
| `references/` | Fuentes y fundamentos usados para diseñar el sistema. |

---

## Skill inicial incluida

Este starter kit incluye una skill completa:

```text
skills/meeting-transcript-analysis/
```

Su objetivo es convertir transcripts de Microsoft Teams en documentos Markdown estructurados, accionables y reutilizables.

Sirve para extraer:

- resumen ejecutivo;
- contexto;
- participantes;
- temas principales;
- decisiones;
- compromisos;
- responsables;
- riesgos;
- dependencias;
- requerimientos;
- posibles issues;
- implicaciones técnicas;
- próximos pasos.

---

## Flujo recomendado para transcripts

```text
Transcript de Teams
  ↓
meeting-transcript-analysis
  ↓
Documento Markdown estructurado
  ↓
repository-issue-generator
  ↓
Issues / tickets / tareas técnicas
  ↓
Seguimiento en repositorio o herramienta de gestión
```

---

## Principios del repositorio

### 1. Separar prompt, contrato y pruebas

Cada skill debe separar:

- qué hace;
- qué entrada espera;
- qué salida promete;
- cómo se evalúa;
- qué variantes existen.

### 2. No romper contratos sin versionar

Si cambias la estructura de salida de una skill, cambia la versión mayor.

Ejemplo:

```text
1.2.0 → 2.0.0
```

### 3. Diseñar para varios LLMs

Los prompts deben evitar depender de capacidades exclusivas de un solo modelo, salvo que estén dentro de `adapters/`.

### 4. Marcar incertidumbre

Las skills deben enseñar al LLM a decir:

- `No especificado`;
- `Ambiguo`;
- `Requiere confirmación`;
- `Inferencia`.

Esto reduce invenciones y mejora la utilidad del resultado.

### 5. Mantener ejemplos y pruebas

Cada skill debe tener al menos:

- un ejemplo de entrada;
- un ejemplo de salida;
- una checklist de calidad;
- casos de prueba manuales o semiautomáticos.

---

## Cómo usar una skill manualmente

1. Abre la carpeta de la skill.
2. Lee `skill.md`.
3. Escoge el prompt adecuado:
   - `prompt.full.md`
   - `prompt.quick.md`
   - `prompt.file-input.md`
   - otro prompt específico.
4. Copia el prompt en tu LLM.
5. Adjunta o pega la entrada.
6. Revisa la salida usando `evals/checklist.md`.

---

## Cómo pedirle a un LLM que mejore una skill

Usa este patrón:

```markdown
Lee `AGENTS.md`, `conventions/prompt-style-guide.md` y la carpeta de la skill que quiero mejorar.

Objetivo:
[describe qué quieres mejorar]

Restricciones:
- No rompas el contrato de salida salvo que propongas una versión mayor.
- Conserva compatibilidad con LLMs genéricos.
- Actualiza changelog.
- Actualiza ejemplos o evaluaciones si cambia el comportamiento esperado.

Devuélveme:
1. Cambios propuestos.
2. Justificación.
3. Archivos a modificar.
4. Versión sugerida.
5. Riesgos de compatibilidad.
```

---

## Qué significa que una skill está “bien hecha”

Una skill está lista para usarse cuando cumple:

- se entiende sin explicación verbal;
- tiene entrada y salida claras;
- no depende de un solo LLM;
- tiene ejemplos;
- tiene pruebas/checklist;
- tiene changelog;
- dice qué hacer cuando falta información;
- diferencia hechos, inferencias y supuestos;
- produce una salida reutilizable por otras skills.

---

## Roadmap sugerido

Después de la skill inicial, conviene crear o mejorar:

1. `repository-issue-generator`
2. `requirements-extractor`
3. `technical-impact-analysis`
4. `executive-summary-generator`
5. `decision-log-generator`
6. `roadmap-generator`
7. `documentation-generator`

---

## Validación rápida

Ejecuta:

```bash
python scripts/validate_repo.py
```

Esto revisa que cada skill tenga los archivos mínimos esperados.

---

## Fecha de creación

2026-05-20
