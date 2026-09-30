# Migración de los runbooks a Agent Skills

La migración mantiene las capacidades en el mismo repositorio. El procedimiento sigue en los prompts; la nueva entrada permite descubrir la skill y encontrar sus recursos.

## Versiones

| Carpeta | Anterior | Nativa | Estado conservado |
|---|---|---|---|
| meeting-transcript-analysis | 1.0.0 | 1.1.0 | stable |
| repository-initialization | 0.3.0 | 0.4.0 | draft |
| repository-issue-generator | 0.1.0 | 0.2.0 | draft |
| technical-requirements-extractor | 0.1.0 | 0.2.0 | draft |

`evidence-guided-development` ya tiene entrada nativa, versión 1.0.0 experimental.

Las cuatro carpetas migradas conservan los archivos `prompt*.md`, `input.schema.md` y `output.schema.md`. Las versiones minor añaden descubrimiento y selección de procedimientos; no sustituyen los contratos manuales.

## Archivos y metadatos

- La entrada pasa de `skill.md` a `SKILL.md`; actualiza enlaces y scripts que usen el nombre anterior.
- `name` coincide con la carpeta. El nombre visible en español permanece en `registry.yaml`.
- `description` explica cuándo aplicar la skill.
- `id`, `version` y `status` pasan a `metadata` con valores de texto.
- Categoría, etiquetas, formatos y compatibilidad declarada se conservan en el registro. Esa declaración no prueba integración con cada cliente.

El registro conserva su estructura y los IDs anteriores. Los consumidores que extraían campos del encabezado antiguo deben leer `metadata` o el registro.

En Windows, registra el cambio de mayúsculas en Git usando un nombre intermedio:

```bash
git mv skills/example-skill/skill.md skills/example-skill/entry.tmp
git mv skills/example-skill/entry.tmp skills/example-skill/SKILL.md
```

## Diferencias existentes entre contratos y variantes

Las entradas nativas explicitan estas reglas sin reescribir los prompts:

- **Reuniones:** el contrato completo incluye título y dieciocho secciones. Las variantes rápida y consolidada mantienen sus formatos propios. El flujo por partes espera el marcador de cierre y no solicita de nuevo una primera parte ya recibida.
- **Inicialización:** el diagnóstico de archivos complementa las doce secciones del contrato. Un commit sugerido no ejecuta ni publica nada por sí mismo.
- **Issues:** se incluyen las preguntas globales exigidas por el contrato, además de las preguntas por issue del prompt.
- **Requisitos técnicos:** la salida presenta los supuestos e inferencias exigidos por el contrato, además de las tablas y la información para estimar del prompt.

Una futura unificación de formatos manuales debe tratarse como un cambio independiente con revisión y versionado propios.

## Validación e instalación

La [guía de evaluación](how-to-run-evals.md) distingue validación del catálogo, descubrimiento y comportamiento. El validador ahora exige entradas nativas; una carpeta manual nueva debe adaptarse antes de incorporarse.

Instala la carpeta completa siguiendo la [guía de uso](use-and-install-agent-skills.md). Actualizar la fuente no modifica automáticamente las instalaciones personales de otros equipos ni traslada credenciales.

Referencias: [formato Agent Skills](https://agentskills.io/specification) y [descubrimiento en Codex](https://learn.chatgpt.com/docs/build-skills).
