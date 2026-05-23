# Prompt con contexto adjunto

Voy a adjuntar archivos, notas, un árbol de carpetas o una estructura existente para iniciar, ordenar o reorganizar un repositorio.

## Objetivo

Analiza el material proporcionado y ayúdame a convertirlo en una base clara para un repositorio versionado en Git.

## Instrucciones

1. Identifica qué tipo de repositorio parece ser.
2. Resume el propósito inferido y marca si es una inferencia.
3. Distingue contenido útil, duplicado, dudoso o fuera de alcance.
4. Identifica el patrón estructural más probable.
5. Explica si la estructura debe ser `split-frontend-backend`, `single-src-layered`, `framework-native`, `monorepo-workspace` u otra.
6. Propón una estructura inicial.
7. Indica qué documentos base hacen falta.
8. Sugiere qué contenido debería ir en cada documento.
9. Identifica decisiones iniciales que deberían registrarse.
10. Señala archivos o carpetas que conviene evitar por ahora.
11. Sugiere un primer commit.

## Reglas

- No asumas que todos los archivos adjuntos deben copiarse tal cual.
- No elimines contexto importante.
- No inventes información faltante.
- Marca la información dudosa como `Requiere confirmación`.
- Marca inferencias como `Inferencia`.
- Mantén la salida en Markdown.
- No fuerces `frontend/` y `backend/` si el material indica una estructura integrada, nativa del framework o de workspace.

## Salida esperada

- Diagnóstico del material recibido.
- Tipo de repositorio identificado.
- Patrón estructural recomendado.
- Estructura recomendada.
- Archivos base.
- Decisiones sugeridas.
- Riesgos o pendientes.
- Primer commit sugerido.
