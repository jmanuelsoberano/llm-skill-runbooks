# Checklist de evaluación

Usa este checklist para revisar si la salida de la skill sirve como base real para inicializar un repositorio.

## 1. Comprensión de entrada

- [ ] Identifica correctamente el tipo de repositorio.
- [ ] Usa el propósito indicado por el usuario.
- [ ] Distingue hechos, inferencias y datos faltantes.
- [ ] Marca información ambigua o pendiente.
- [ ] No inventa tecnologías, responsables ni restricciones.

## 2. Patrón estructural

- [ ] Clasifica el repositorio en un patrón estructural explícito.
- [ ] Justifica por qué el patrón aplica.
- [ ] No fuerza `frontend/` y `backend/` si el repo indica una estructura integrada.
- [ ] Respeta estructuras nativas de frameworks cuando corresponde.
- [ ] Usa `mixed` solo cuando realmente combina varios patrones.

## 3. Perfil y estrategia de pruebas

- [ ] Clasifica el perfil de pruebas inicial.
- [ ] Justifica por qué ese perfil aplica.
- [ ] No propone todos los tipos de pruebas por default.
- [ ] Ajusta la estrategia de pruebas al riesgo, stack, dependencias y patrón estructural.
- [ ] Incluye `TEST_STRATEGY.md` cuando el repositorio tendrá código, validaciones o reglas de calidad.
- [ ] Distingue pruebas necesarias ahora, pruebas futuras y pruebas que no aplican.
- [ ] Propone E2E solo para flujos críticos o cuando el riesgo lo justifica.
- [ ] Para repos sin código, propone validaciones documentales, ejemplos o checklists en lugar de pruebas de aplicación.

## 4. Estructura propuesta

- [ ] Propone una estructura proporcional al tamaño del proyecto.
- [ ] Evita complejidad innecesaria.
- [ ] Incluye carpetas solo cuando tienen una función clara.
- [ ] Explica para qué sirve cada archivo o carpeta importante.
- [ ] Sugiere qué carpetas conviene evitar por ahora, si aplica.

## 5. Documentación base

- [ ] Incluye `README.md`.
- [ ] Incluye `PROJECT_CONTEXT.md`.
- [ ] Incluye `STRUCTURE.md`.
- [ ] Incluye `DECISIONS.md`.
- [ ] Incluye `CHANGELOG.md`.
- [ ] Incluye `TODO.md`.
- [ ] Incluye `LLM_GUIDE.md` cuando el repositorio será trabajado con asistentes.
- [ ] Incluye `TEST_STRATEGY.md` cuando aplique.

## 6. Decisiones y trazabilidad

- [ ] Sugiere decisiones iniciales para registrar.
- [ ] Incluye decisiones de pruebas cuando se define una estrategia.
- [ ] No mezcla decisiones tomadas con decisiones sugeridas.
- [ ] Indica consecuencias o razones de las decisiones importantes.
- [ ] Propone cómo mantener el changelog.

## 7. Seguridad y cuidado

- [ ] No solicita ni expone secretos.
- [ ] Recomienda no versionar tokens, contraseñas o llaves.
- [ ] Señala si hay contenido sensible que debe excluirse.
- [ ] Considera pruebas o validaciones de seguridad si hay autenticación, permisos o datos sensibles.

## 8. Accionabilidad

- [ ] Incluye checklist de arranque.
- [ ] Sugiere un primer commit claro.
- [ ] Indica próximos pasos concretos.
- [ ] La salida puede copiarse o transformarse en archivos reales sin reinterpretar la intención.

## Resultado

- [ ] Aprobado.
- [ ] Aprobado con ajustes menores.
- [ ] Requiere corrección.
