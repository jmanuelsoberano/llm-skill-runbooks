# Adapter: Claude

## Uso recomendado

Claude suele funcionar bien con delimitadores XML para separar instrucciones, contexto y datos.

## Wrapper sugerido

```xml
<instructions>
Pega aquí el prompt de la skill.
</instructions>

<context>
Contexto opcional.
</context>

<transcript>
Pega aquí el transcript o indica el archivo adjunto.
</transcript>
```

## Nota

Mantén instrucciones explícitas sobre no inventar y marcar inferencias.
