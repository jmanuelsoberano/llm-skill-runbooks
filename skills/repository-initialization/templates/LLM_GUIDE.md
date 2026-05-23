# Guía para LLMs

Este archivo define cómo debe colaborar un asistente o LLM dentro de este repositorio.

## Antes de proponer cambios

Revisar primero:

1. `PROJECT_CONTEXT.md`
2. `STRUCTURE.md`
3. `DECISIONS.md`
4. `TODO.md`
5. `CHANGELOG.md`

## Reglas de trabajo

- No inventar contexto del proyecto.
- No eliminar información existente sin confirmación humana.
- No cambiar la estructura sin actualizar `STRUCTURE.md`.
- No tomar decisiones importantes sin registrarlas en `DECISIONS.md`.
- No mezclar tareas pendientes con decisiones tomadas.
- No incluir secretos, tokens, contraseñas o datos sensibles.
- Marcar dudas como `Pendiente`, `Ambiguo` o `Requiere confirmación`.

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
- `CHANGELOG.md`, si el cambio afecta el uso del repositorio

## Checklist antes de terminar

- [ ] Leí el contexto del proyecto.
- [ ] Respeté la estructura actual.
- [ ] No inventé información.
- [ ] Actualicé documentación relacionada.
- [ ] Dejé pendientes visibles si faltó información.
- [ ] Sugerí un mensaje de commit claro.
