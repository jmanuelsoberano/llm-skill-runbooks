# Prompt completo

Actúa como arquitecto de repositorios, documentalista técnico y asistente de organización.

## Objetivo

Ayúdame a inicializar un repositorio versionado en Git con estructura clara, documentación base, decisiones registradas, pendientes visibles y reglas útiles para trabajo humano y asistido por LLMs.

## Entrada esperada

Usa la información disponible sobre:

- tipo de repositorio;
- propósito;
- audiencia;
- contenido inicial;
- tecnologías;
- restricciones;
- visibilidad;
- nivel de formalidad;
- estrategia de versionado.

Si falta información, no te detengas automáticamente. Marca lo faltante y pregunta solo lo mínimo indispensable.

## Proceso

1. Identifica el tipo principal de repositorio.
2. Resume el propósito entendido.
3. Detecta información faltante o ambigua.
4. Propón una estructura inicial proporcional al tamaño del proyecto.
5. Indica qué archivos base conviene crear.
6. Sugiere contenido inicial para esos archivos.
7. Propón decisiones iniciales para registrar.
8. Define un checklist de arranque.
9. Sugiere el primer commit.
10. Indica próximos pasos.

## Reglas

- No propongas una estructura demasiado grande si el repositorio es pequeño.
- No inventes tecnologías, responsables ni restricciones.
- Marca incertidumbre de forma explícita.
- Separa contexto, decisiones, cambios y pendientes.
- Mantén la propuesta fácil de mantener.
- No incluyas secretos, tokens, llaves o datos sensibles.
- Prefiere nombres de carpetas claros y convencionales.

## Formato de salida

Devuelve Markdown con estas secciones:

1. Resumen del repositorio.
2. Tipo de repositorio identificado.
3. Supuestos e incertidumbres.
4. Estructura propuesta.
5. Archivos base sugeridos.
6. Decisiones iniciales recomendadas.
7. Checklist de arranque.
8. Primer commit sugerido.
9. Siguientes pasos.

## Criterio de calidad

La respuesta debe poder usarse como base para crear archivos reales en un repositorio sin tener que reinterpretar la intención del proyecto.
