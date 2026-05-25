# Ejemplo: quality gates por stack

Este archivo muestra validaciones candidatas según tecnología. No todas deben aplicarse siempre.

## .NET

Validaciones candidatas:

- Formato: `dotnet format`, `.editorconfig`.
- Lint/analyzers: Roslyn analyzers, StyleCop.Analyzers, SonarAnalyzer si aplica.
- Pruebas: MSTest, xUnit o NUnit.
- Arquitectura: NetArchTest o ArchUnitNET.
- Seguridad: revisión de dependencias, secretos y configuración.

Stages sugeridos:

- `pre-commit`: formato rápido.
- `pre-push`: unit tests rápidos.
- CI: build, tests, coverage, arquitectura y análisis estático.

## Java

Validaciones candidatas:

- Formato/lint: Checkstyle, Spotless, PMD.
- Bugs: SpotBugs.
- Pruebas: JUnit.
- Arquitectura: ArchUnit.
- Seguridad: dependencias y secretos.

Stages sugeridos:

- `pre-commit`: formato y estilo rápido.
- `pre-push`: unit tests rápidos.
- CI: build completo, tests, arquitectura y seguridad.

## Python / Django

Validaciones candidatas:

- Formato: Black.
- Lint/imports: Ruff, isort.
- Typing: mypy, si aplica.
- Pruebas: pytest, unittest, Django TestCase.
- Framework: Django system checks y validación de migraciones.

Stages sugeridos:

- `pre-commit`: ruff, black, isort.
- `pre-push`: tests rápidos.
- CI: tests completos, migraciones, checks y coverage.

## JavaScript / TypeScript / Angular / React

Validaciones candidatas:

- Formato: Prettier.
- Lint: ESLint.
- Typing: `tsc --noEmit`.
- Pruebas: Vitest, Jest, Testing Library.
- E2E: Playwright o Cypress cuando aplique.
- Hooks: Husky y lint-staged si el proyecto usa ecosistema Node.

Stages sugeridos:

- `pre-commit`: prettier, eslint sobre archivos cambiados.
- `pre-push`: typecheck y unit tests rápidos.
- CI: build, tests completos, E2E críticos y coverage.

## Repos de documentación, prompts o skills

Validaciones candidatas:

- Markdown lint.
- Link checking.
- Validación de estructura.
- Validación de registry.
- Validación de ejemplos de entrada/salida.
- Checklist manual o semiautomático.

Stages sugeridos:

- `pre-commit`: formato Markdown básico.
- CI: validar estructura, registry y ejemplos.
