# Conjunto de investigación e ingeniería

Versión del conjunto: 0.1.0, experimental. Contiene 18 skills principales y 2 integraciones existentes, 20 paquetes en research-suite.json. Las restantes skills del repositorio se conservan fuera de este conjunto.

## Uso cotidiano

Describe tu tarea normalmente o invoca la especialidad por su nombre. Por ejemplo:

- `$evidence-guided-development Implementa este cambio conservando los contratos y verifica el comportamiento.`
- `$oreilly-research Contrasta esta afirmación; usa Answers para orientar y verifica los pasajes decisivos.`
- `$review-code-change Revisa este PR y entrega hallazgos accionables, sin modificar el código.`
- `$design-data-change Diseña la transición de este campo y cómo comprobar integridad y compatibilidad.`
- `$investigate-technical-incident Investiga estas observaciones y distingue hipótesis de causa comprobada.`

La selección implícita depende del cliente. Estas instrucciones no crean un mecanismo automático de ejecución entre procesos. Cada especialista puede usarse directamente y conserva un entregable propio.

## Módulos y conexiones

Consultar [flujo y catálogo](../workflows/engineering-research.md) y el [contrato común](../references/evidence-contract.md). EGD coordina; los especialistas no vuelven a invocarlo. Solo cargar las referencias pertinentes.

Las reglas de evidencia se mantienen en una fuente canónica y se distribuyen dentro de cada paquete. Así los paquetes son autocontenidos. Tras editar el contrato, ejecutar desde la raíz:

```text
python scripts/manage_research_suite.py sync
python scripts/manage_research_suite.py check
```

## Llevarlo a otro equipo

1. Copiar el ZIP del conjunto y descomprimirlo en una carpeta propia. También puede utilizarse el repositorio cuando estos cambios estén publicados; un clon remoto anterior no contiene esta versión.
2. Con Python 3.10 o superior, ejecutar desde la carpeta descomprimida:

```text
python scripts/manage_research_suite.py check
python scripts/manage_research_suite.py install --dry-run
python scripts/manage_research_suite.py install
```

El instalador usa CODEX_HOME/skills cuando existe CODEX_HOME, o .codex/skills dentro de la carpeta personal. `--dest` permite elegir otro directorio. Las comprobaciones e instalación del paquete utilizan solo la biblioteca estándar de Python.

Las copias idénticas se conservan sin cambios. Si hay una skill distinta con el mismo nombre, el instalador se detiene antes de copiar cualquier paquete; revisar el conflicto y usar `--replace nombre-de-skill` para autorizar cada reemplazo. Guarda la versión anterior y un recibo con hashes. `--backup-root` debe estar fuera del directorio de descubrimiento y, para el movimiento de carpetas, en el mismo volumen que el destino. Una falla durante los movimientos intenta restaurar el estado anterior.

Alternativa manual: copiar las veinte carpetas completas de skills/ al directorio de skills del cliente, conservando antes cualquier copia previa. No copiar solo SKILL.md.

Las nuevas skills estarán disponibles en el siguiente turno cuando el cliente recargue el catálogo. Si no aparecen, comprobar ubicación, configuración y errores de descubrimiento del cliente.

## Misma cuenta u otra cuenta

La distribución contiene instrucciones y ejemplos, no autenticación. En cada equipo o cuenta deben comprobarse por separado:
- descubrimiento de skills por el cliente;
- conexión y autorización de Search MCP;
- sesión de O'Reilly en el navegador;
- disponibilidad de Answers y de las herramientas de navegación.

No se garantiza sincronización automática de carpetas locales entre equipos. Una cuenta distinta necesita sus propios accesos o los que legítimamente le correspondan. No copiar tokens, cookies, perfiles del navegador ni secretos junto con las skills.

Expert es opcional y requiere sus herramientas y licencia reales. Nuestro flujo aproxima tareas de investigación mediante fuentes disponibles; no afirma equivalencia de cobertura, calidad, velocidad o funciones empresariales.

## Mantenimiento y pruebas

EGD pasa a 1.1.0 y las integraciones de requisitos/issues a 0.3.0 conservando salidas. Las 17 nuevas skills empiezan en 0.1.0 experimental. No se declara madurez estable por pasar un validador.

Para mantenimiento del repositorio completo:
```text
python -m pip install -r requirements-dev.txt
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

Los ejemplos/casos son sintéticos salvo indicación explícita. Validación estática, evaluación de agente, autenticación MCP y lectura real son comprobaciones distintas. Las evidencias y resultados de un proyecto no se guardan en el catálogo.

## Origen

Instrucciones nuevas redactadas para este conjunto. Los once casos profesionales se contrastaron con el [catálogo oficial O'Reilly](https://github.com/oreillymedia/expert-intelligence-skills) el 2026-09-29; no se copiaron sus prompts. Sus paquetes consultan Expert. Este repositorio conserva su LICENSE.md existente, que no define una licencia formal; no se le atribuye MIT, Apache u otra licencia no verificada.
