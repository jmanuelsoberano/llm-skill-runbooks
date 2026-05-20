# Adapter: ChatGPT

## Uso recomendado

- Para archivo adjunto, usa `prompt.file-input.md`.
- Para transcript largo, usa `prompt.chunked-long-transcript.md`.
- Para mejorar el prompt, proporciona también `skill.md`, `input.schema.md` y `output.schema.md`.

## Recomendación

Cuando uses archivos, escribe además:

```text
Analiza el archivo adjunto completo. Si no puedes leer alguna parte, indícalo explícitamente.
```

## Salida

Pide Markdown puro si lo vas a pegar en repositorios o generadores de documentación.
