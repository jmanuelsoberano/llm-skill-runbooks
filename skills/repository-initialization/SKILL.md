---
name: repository-initialization
description: Prepara la estructura inicial de un repositorio Git, su documentación
  y una estrategia de pruebas proporcional. Úsala al comenzar un proyecto, organizar
  código o documentos iniciales, o preparar un repositorio vacío para colaboración.
  Respeta la estructura del framework y las restricciones existentes.
metadata:
  id: repository.initialization
  version: 0.4.0
  status: draft
---

# Skill: Inicialización de repositorios

## Ejecución como Agent Skill

1. Lee [input.schema.md](input.schema.md) y el contexto ya disponible. Inspecciona la estructura existente cuando tengas acceso.
2. Si hay archivos, notas o un árbol que analizar, lee [prompt.file-input.md](prompt.file-input.md). Si solo se pide una propuesta breve, lee [prompt.quick.md](prompt.quick.md). En otro caso, lee [prompt.full.md](prompt.full.md). Cuando se combinan archivos y brevedad, analiza el material y presenta el resultado compacto.
3. Aplica el procedimiento elegido y cubre las secciones de [output.schema.md](output.schema.md). El diagnóstico del material adjunto complementa ese contrato. Ajusta estructura y pruebas al propósito; no asumas que existen frontend y backend separados.
4. Consulta únicamente las [plantillas](templates/) y los [ejemplos](examples/) que correspondan al patrón elegido. Comprueba el resultado con [evals/checklist.md](evals/checklist.md).

La salida predeterminada es una propuesta. Si la petición incluye crear archivos, concreta los cambios locales correspondientes y conserva el contenido existente. El bloque de primer commit es una sugerencia: no constituye por sí mismo autorización para hacer commit o publicar. Respeta la autorización que el usuario ya haya dado para esas acciones.

Para mantenimiento, usa [evals/agent-cases.md](evals/agent-cases.md).

## Propósito

Guiar la creación inicial de repositorios versionados en Git para que nazcan con propósito claro, estructura documentada, estrategia de pruebas definida, decisiones registradas, pendientes visibles y reglas de mantenimiento.

Esta skill ayuda a evitar repositorios que empiezan con archivos sueltos, documentación incompleta, decisiones no registradas, pruebas improvisadas o instrucciones ambiguas para futuros colaboradores humanos o LLMs.

## Cuándo usarla

Usa esta skill cuando:

- vayas a crear un repositorio desde cero;
- hayas clonado un repositorio vacío;
- tengas documentos o código inicial y necesites ordenarlos;
- quieras preparar un repositorio para trabajo asistido por LLMs;
- necesites una estructura mínima antes del primer commit relevante;
- quieras dejar una estrategia inicial de pruebas antes de crear código de pruebas.

## Casos de uso

- Repositorios de código.
- Repositorios de documentación.
- Repositorios de seguimiento de actividades.
- Repositorios de aplicaciones.
- Repositorios de investigación.
- Repositorios de prompts o skills.
- Repositorios mixtos.

## Patrones de estructura soportados

Antes de proponer carpetas, clasifica el repositorio en uno de estos patrones:

| Patrón | Cuándo aplica |
|---|---|
| `docs-only` | El valor principal son documentos, guías, runbooks o referencias. |
| `code-library` | Librería, paquete, utilidad o servicio pequeño con código fuente y pruebas. |
| `split-frontend-backend` | Frontend y backend son proyectos separados con dependencias, builds o despliegues distintos. |
| `single-src-layered` | Todo vive bajo una carpeta principal como `src/`, con capas internas: dominio, aplicación, infraestructura, web, UI o presentación. |
| `framework-native` | Conviene respetar la estructura generada o recomendada por un framework como Django, Angular, React, Next.js o .NET. |
| `monorepo-workspace` | Hay varias apps, paquetes o librerías en un mismo repositorio. |
| `prompt-skill-repo` | El repositorio almacena prompts, skills, runbooks o plantillas para LLMs. |
| `mixed` | Combina varios patrones y requiere explicación explícita. |

## Perfiles de pruebas soportados

Después de clasificar el patrón estructural, define un perfil inicial de pruebas:

| Perfil | Cuándo aplica |
|---|---|
| `no-code-validation` | Repositorios sin código productivo: documentación, prompts, skills, runbooks o referencias. |
| `unit-only` | Librerías pequeñas, utilidades o lógica aislada. |
| `unit-plus-integration` | Código con dependencias externas moderadas: base de datos, archivos, servicios o framework web. |
| `layered-testing` | Aplicaciones con capas: dominio, aplicación, infraestructura, presentación, API o UI. |
| `frontend-component-testing` | Aplicaciones con UI importante: componentes, rutas, servicios cliente, hooks o interacción. |
| `api-contract-testing` | APIs consumidas por otros sistemas, integraciones o clientes externos. |
| `e2e-critical-flows` | Productos con flujos críticos de usuario que deben validarse punta a punta. |
| `full-quality-gate` | Sistemas productivos o críticos que requieren varias capas de pruebas y validaciones en CI. |
| `custom` | Caso mixto que requiere justificar una combinación propia. |

## Cuándo no usarla

No es la mejor opción cuando:

- el repositorio ya tiene una arquitectura madura y solo requiere una auditoría;
- se necesita migrar un monorepo complejo;
- el objetivo principal es revisar calidad de código;
- solo se necesita generar un README breve.

## Archivos relacionados

- [input.schema.md](input.schema.md)
- [output.schema.md](output.schema.md)
- [prompt.full.md](prompt.full.md)
- [prompt.quick.md](prompt.quick.md)
- [prompt.file-input.md](prompt.file-input.md)
- [templates/](templates/)
- [templates/GITIGNORE.md](templates/GITIGNORE.md)
- [templates/TEST_STRATEGY.md](templates/TEST_STRATEGY.md)
- [examples/](examples/)
- [evals/checklist.md](evals/checklist.md)
- [changelog.md](changelog.md)

## Flujo recomendado

1. Recolectar contexto mínimo del repositorio.
2. Clasificar el tipo de repositorio.
3. Clasificar el patrón estructural más adecuado.
4. Clasificar el perfil inicial de pruebas.
5. Detectar datos faltantes.
6. Proponer estructura inicial proporcional al patrón elegido.
7. Seleccionar documentos base.
8. Sugerir `TEST_STRATEGY.md` cuando aplique.
9. Sugerir `.gitignore` inicial cuando aplique.
10. Registrar decisiones iniciales.
11. Preparar checklist de arranque.
12. Sugerir primer commit.

## Resultado esperado

Al finalizar la aplicación de esta skill, el repositorio debe tener:

- propósito claro;
- patrón estructural identificado;
- perfil de pruebas identificado;
- estructura inicial entendible;
- documentos base sugeridos;
- estrategia de pruebas inicial sugerida;
- decisiones iniciales registradas;
- pendientes visibles;
- reglas mínimas para colaboración con LLMs;
- sugerencia de `.gitignore` cuando aplique;
- mensaje de commit inicial recomendado.
