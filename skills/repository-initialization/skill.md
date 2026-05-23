---
id: repository.initialization
name: Inicialización de repositorios
version: 0.1.0
status: draft
category: repository-management
tags:
  - git
  - repositorios
  - inicializacion
  - documentacion
  - llm
  - templates
input_types:
  - text
  - markdown
  - file
output_formats:
  - markdown
llm_compatibility:
  - generic-llm
  - ChatGPT
  - Claude
  - Gemini
  - Copilot
---

# Skill: Inicialización de repositorios

## Propósito

Guiar la creación inicial de repositorios versionados en Git para que nazcan con propósito claro, estructura documentada, decisiones registradas, pendientes visibles y reglas de mantenimiento.

Esta skill ayuda a evitar repositorios que empiezan con archivos sueltos, documentación incompleta, decisiones no registradas o instrucciones ambiguas para futuros colaboradores humanos o LLMs.

## Cuándo usarla

Usa esta skill cuando:

- vayas a crear un repositorio desde cero;
- hayas clonado un repositorio vacío;
- tengas documentos o código inicial y necesites ordenarlos;
- quieras preparar un repositorio para trabajo asistido por LLMs;
- necesites una estructura mínima antes del primer commit relevante.

## Casos de uso

- Repositorios de código.
- Repositorios de documentación.
- Repositorios de seguimiento de actividades.
- Repositorios de aplicaciones.
- Repositorios de investigación.
- Repositorios de prompts o skills.
- Repositorios mixtos.

## Cuándo no usarla

No es la mejor opción cuando:

- el repositorio ya tiene una arquitectura madura y solo requiere una auditoría;
- se necesita migrar un monorepo complejo;
- el objetivo principal es revisar calidad de código;
- solo se necesita generar un README breve.

## Archivos relacionados

- `input.schema.md`
- `output.schema.md`
- `prompt.full.md`
- `prompt.quick.md`
- `prompt.file-input.md`
- `templates/`
- `templates/GITIGNORE.md`
- `examples/`
- `evals/checklist.md`
- `changelog.md`

## Flujo recomendado

1. Recolectar contexto mínimo del repositorio.
2. Clasificar el tipo de repositorio.
3. Detectar datos faltantes.
4. Proponer estructura inicial.
5. Seleccionar documentos base.
6. Sugerir `.gitignore` inicial cuando aplique.
7. Registrar decisiones iniciales.
8. Preparar checklist de arranque.
9. Sugerir primer commit.

## Resultado esperado

Al finalizar la aplicación de esta skill, el repositorio debe tener:

- propósito claro;
- estructura inicial entendible;
- documentos base sugeridos;
- decisiones iniciales registradas;
- pendientes visibles;
- reglas mínimas para colaboración con LLMs;
- sugerencia de `.gitignore` cuando aplique;
- mensaje de commit inicial recomendado.
