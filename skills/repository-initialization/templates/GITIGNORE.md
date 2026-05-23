# Plantilla de .gitignore

Usa este archivo como referencia para crear un `.gitignore` inicial según el tipo de repositorio.

## General

```gitignore
.DS_Store
Thumbs.db
*.log
.env
.env.*
!.env.example
.vscode/
.idea/
.cache/
tmp/
```

## Node.js / frontend

```gitignore
node_modules/
dist/
build/
coverage/
```

## Python

```gitignore
__pycache__/
*.pyc
.venv/
venv/
.pytest_cache/
```

## .NET

```gitignore
bin/
obj/
TestResults/
*.user
```

## Reglas

- No versionar secretos.
- No versionar dependencias instaladas.
- No versionar artefactos generados.
- Mantener un `.env.example` sin valores sensibles cuando sea útil.
