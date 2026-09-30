# Skillbook

Catálogo para organizar, versionar y reutilizar skills de trabajo con LLMs. El repositorio de GitHub conserva su nombre: `llm-skill-runbooks`.

Las 22 carpetas de `skills/` incluyen una entrada estándar `SKILL.md` y sus recursos. Puedes instalar la carpeta completa en un agente compatible o utilizar sus prompts manualmente. El formato nativo sigue la [especificación de Agent Skills](https://agentskills.io/specification).

## Skills disponibles

| Skill | Versión | Estado | Uso |
|---|---|---|---|
| [evidence-guided-development](skills/evidence-guided-development/SKILL.md) | 1.1.0 | experimental | Desarrollo con evidencia |
| [meeting-transcript-analysis](skills/meeting-transcript-analysis/SKILL.md) | 1.1.0 | stable | Análisis de transcripts de reuniones |
| [repository-issue-generator](skills/repository-issue-generator/SKILL.md) | 0.3.0 | draft | Generador de issues para repositorio |
| [technical-requirements-extractor](skills/technical-requirements-extractor/SKILL.md) | 0.3.0 | draft | Extractor de requerimientos técnicos |
| [repository-initialization](skills/repository-initialization/SKILL.md) | 0.4.0 | draft | Inicialización de repositorios |
| [oreilly-research](skills/oreilly-research/SKILL.md) | 0.1.0 | experimental | Investigación en O'Reilly |
| [create-decision-brief](skills/create-decision-brief/SKILL.md) | 0.1.0 | experimental | Resumen de decisión técnica |
| [forecast-project-delivery](skills/forecast-project-delivery/SKILL.md) | 0.1.0 | experimental | Pronóstico de entrega |
| [assess-team-structure](skills/assess-team-structure/SKILL.md) | 0.1.0 | experimental | Estructura y coordinación de equipos |
| [compare-implementation-approaches](skills/compare-implementation-approaches/SKILL.md) | 0.1.0 | experimental | Comparación de implementaciones |
| [review-architecture-decision](skills/review-architecture-decision/SKILL.md) | 0.1.0 | experimental | Revisión de decisión arquitectónica |
| [review-technical-proposal](skills/review-technical-proposal/SKILL.md) | 0.1.0 | experimental | Revisión de propuesta técnica |
| [evaluate-security-risk](skills/evaluate-security-risk/SKILL.md) | 0.1.0 | experimental | Evaluación de riesgos de seguridad |
| [plan-service-reliability](skills/plan-service-reliability/SKILL.md) | 0.1.0 | experimental | Plan de confiabilidad del servicio |
| [plan-production-ready-ai](skills/plan-production-ready-ai/SKILL.md) | 0.1.0 | experimental | Plan para IA en producción |
| [plan-domain-rampup](skills/plan-domain-rampup/SKILL.md) | 0.1.0 | experimental | Incorporación a dominio y sistema |
| [create-learning-plan](skills/create-learning-plan/SKILL.md) | 0.1.0 | experimental | Plan de aprendizaje técnico |
| [review-code-change](skills/review-code-change/SKILL.md) | 0.1.0 | experimental | Revisión de cambios de código |
| [design-data-change](skills/design-data-change/SKILL.md) | 0.1.0 | experimental | Diseño de cambios de datos |
| [analyze-system-performance](skills/analyze-system-performance/SKILL.md) | 0.1.0 | experimental | Análisis de rendimiento |
| [investigate-technical-incident](skills/investigate-technical-incident/SKILL.md) | 0.1.0 | experimental | Investigación de incidente técnico |
| [design-test-strategy](skills/design-test-strategy/SKILL.md) | 0.1.0 | experimental | Estrategia de pruebas |

El estado refleja la madurez declarada del contenido; incorporar `SKILL.md` no demuestra que todas las salidas de un agente sean correctas.

## Conjunto de investigación e ingeniería

La [guía del conjunto](playbooks/research-suite.md) describe las 18 capacidades principales y 2 integraciones, instalación con respaldo, portabilidad a otro equipo/cuenta y pruebas. El [flujo modular](workflows/engineering-research.md) explica qué responsabilidad conserva cada una.

## Cómo empezar

1. Elige la skill según el resultado que necesitas.
2. Sigue la [guía de instalación y uso](playbooks/use-and-install-agent-skills.md) para copiar la carpeta completa a una ubicación reconocida por tu cliente.
3. Invócala por nombre o describe la tarea. La selección implícita depende del agente y de la descripción de la skill.
4. Revisa el resultado con su `evals/checklist.md`.

Ejemplo en Codex:

```text
$evidence-guided-development Implementa esta regla de negocio usando el contexto y las convenciones del proyecto.
```

`skills/` es el catálogo de fuentes. No es, por sí solo, una ubicación que Codex descubra automáticamente. `registry.yaml` indexa el catálogo; no instala skills ni configura MCP.

## Estructura

```text
llm-skill-runbooks/
  skills/          Capacidades instalables y prompts originales
  registry.yaml    Índice, versiones y clasificación
  templates/       Plantillas para mantener el catálogo
  conventions/     Reglas de contratos, nombres y versionado
  schemas/         Esquemas de metadatos
  scripts/         Validación del catálogo
  tests/           Regresiones del validador
  workflows/       Combinaciones de skills
  playbooks/       Instalación, mantenimiento y evaluación
  references/      Fuentes
```

Cada carpeta conserva el procedimiento en `prompt.full.md`, las variantes que necesita, los contratos de entrada/salida y la evaluación. `SKILL.md` contiene el nombre, una descripción para selección y las instrucciones para encontrar esos recursos.

El requisito mínimo de Agent Skills es `SKILL.md`. Los contratos, changelog y archivos de evaluación son convenciones adicionales de este catálogo. No es obligatorio que una skill incluya scripts.

## Uso manual

Abre `SKILL.md`, elige la variante indicada, y proporciona al LLM el prompt, sus contratos y el material del caso. Esta opción sigue disponible en clientes sin descubrimiento de skills. Un LLM solo puede leer archivos, navegar o usar MCP si su entorno ofrece esas capacidades.

Para transcripts puedes usar el [flujo de reunión a seguimiento](workflows/meeting-to-repository-followup.md): análisis de reunión, extracción técnica cuando corresponda y preparación de issues. No es obligatorio ejecutar toda la cadena para una tarea individual.

## Compatibilidad de la migración

Las cuatro entradas anteriores `skill.md` pasan a llamarse `SKILL.md`. Sus campos descriptivos se adaptaron al estándar; los IDs con puntos y las versiones están bajo `metadata`, y la clasificación permanece en el registro.

Los prompts, los contratos, los ejemplos y los adaptadores existentes se conservan. Los enlaces que apuntaban al nombre anterior deben actualizarse. La [guía de migración](playbooks/migrate-existing-skills.md) documenta diferencias de variantes y límites de compatibilidad.

## Mantenimiento

Lee [AGENTS.md](AGENTS.md) y [cómo agregar una skill](playbooks/how-to-add-new-skill.md) antes de modificar el catálogo.

- Separa instrucciones, contratos, ejemplos y evaluaciones.
- Conserva incertidumbre y evidencia; no inventes capacidades ni resultados.
- Mantén cambios compatibles y registra versiones. Cambiar un contrato estable de forma incompatible requiere versión mayor.
- Usa casos representativos para revisar comportamiento; la validación estática no lo sustituye.

## Validación

Requiere Python 3.10 o superior. En un entorno virtual, instala las dependencias del validador:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

PyYAML interpreta YAML; jsonschema comprueba los esquemas declarados. Estas dependencias sirven para mantener el repositorio; no son necesarias para usar los prompts.

El validador comprueba entradas nativas, nombres y tipos de metadatos, correspondencia con el registro, archivos obligatorios y enlaces locales desde `SKILL.md`, respetando mayúsculas incluso en Windows. No ejecuta prompts ni comprueba autenticación MCP, destinos web, fragmentos de enlaces o calidad semántica.

Consulta [cómo evaluar](playbooks/how-to-run-evals.md) para distinguir validación estática, descubrimiento y comportamiento.
