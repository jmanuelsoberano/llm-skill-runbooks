# Prompt con contexto adjunto

Voy a adjuntar archivos, notas, un árbol de carpetas o una estructura existente para iniciar, ordenar o reorganizar un repositorio.

## Objetivo

Analiza el material proporcionado y ayúdame a convertirlo en una base clara para un repositorio versionado en Git.

## Instrucciones

1. Identifica qué tipo de repositorio parece ser.
2. Resume el propósito inferido y marca si es una inferencia.
3. Distingue contenido útil, duplicado, dudoso o fuera de alcance.
4. Propón una estructura inicial.
5. Indica qué documentos base hacen falta.
6. Sugiere qué contenido debería ir en cada documento.
7. Identifica decisiones iniciales que deberían registrarse.
8. Señala archivos o carpetas que conviene evitar por ahora.
9. Sugiere un primer commit.

## Reglas

- No asumas que todos los archivos adjuntos deben copiarse tal cual.
- No elimines contexto importante.
- No inventes información faltante.
- Marca la información dudosa como `Requiere confirmación`.
- Marca inferencias como `Inferencia`.
- Mantén la salida en Markdown.

## Salida esperada

- Diagnóstico del material recibido.
- Tipo de repositorio identificado.
- Estructura recomendada.
- Archivos base.
- Decisiones sugeridas.
- Riesgos o pendientes.
- Primer commit sugerido.
