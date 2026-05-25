# Guía para LLMs

Este archivo define cómo debe colaborar un asistente o LLM dentro de este repositorio.

## Antes de proponer cambios

Revisar primero:

1. `PROJECT_CONTEXT.md`
2. `STRUCTURE.md`
3. `DECISIONS.md`
4. `TEST_STRATEGY.md`, si existe
5. `TODO.md`
6. `CHANGELOG.md`

## Reglas de trabajo

- No inventar contexto del proyecto.
- No eliminar información existente sin confirmación humana.
- No cambiar la estructura sin actualizar `STRUCTURE.md`.
- No tomar decisiones importantes sin registrarlas en `DECISIONS.md`.
- No mezclar tareas pendientes con decisiones tomadas.
- No incluir secretos, tokens, contraseñas o datos sensibles.
- Marcar dudas como `Pendiente`, `Ambiguo` o `Requiere confirmación`.

## Reglas para pruebas

- Antes de crear o modificar pruebas, revisar `TEST_STRATEGY.md` si existe.
- No agregar un nuevo tipo de prueba sin actualizar `TEST_STRATEGY.md`.
- No agregar herramientas nuevas de pruebas sin registrar la decisión.
- No crear pruebas E2E para todo por default; priorizar flujos críticos.
- Si la estrategia de pruebas no existe, sugerir crearla antes de generar pruebas.

## Cuando agregues contenido

Indica:

- qué agregaste;
- por qué era necesario;
- qué archivos cambiaste;
- qué queda pendiente.

## Cuando modifiques estructura

Actualizar también:

- `STRUCTURE.md`
- `DECISIONS.md`, si hubo una decisión relevante
- `TEST_STRATEGY.md`, si cambia la estrategia de pruebas
- `CHANGELOG.md`, si el cambio afecta el uso del repositorio

## Checklist antes de terminar

- [ ] Leí el contexto del proyecto.
- [ ] Respeté la estructura actual.
- [ ] Revisé `TEST_STRATEGY.md` si la tarea involucra pruebas.
- [ ] No inventé información.
- [ ] Actualicé documentación relacionada.
- [ ] Dejé pendientes visibles si faltó información.
- [ ] Sugerí un mensaje de commit claro.
