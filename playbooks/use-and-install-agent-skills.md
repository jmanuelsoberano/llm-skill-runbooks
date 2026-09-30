# Usar e instalar una skill

## Carpeta, instalación y distribución

Una skill nativa es una carpeta con `SKILL.md`, frontmatter YAML con `name` y `description`, y los recursos que sus instrucciones necesitan. El nombre de la carpeta coincide con `name`, en minúsculas y kebab-case.

«Instalar» una skill local significa colocar o enlazar la carpeta completa donde el cliente la descubre. No exige compilarla, publicarla en una tienda, pagar otra API ni crear un servidor. El cliente necesita soportar Agent Skills; un chat genérico puede utilizar los archivos como instrucciones adjuntas, sin descubrimiento automático.

El repositorio conserva la fuente y su historial. La ubicación reconocida por el cliente contiene la copia que se usa. Las copias no se actualizan automáticamente al modificar GitHub; hay que actualizarlas o gestionar un enlace a la fuente. Para empezar, una copia explícita es suficiente.

## Codex

La documentación actual indica `.agents/skills/<skill-name>/` dentro del proyecto y `~/.agents/skills/<skill-name>/` para uso personal. La instalación de Codex verificada durante la creación de esta skill también carga `~/.codex/skills/`, que usa su creador local. Comprueba el cliente y evita duplicar la misma skill en varias ubicaciones.

En un repositorio de aplicación, la ubicación sería:

```text
application-repository/
  .agents/
    skills/
      evidence-guided-development/
        SKILL.md
        prompt.full.md
        ...recursos restantes
```

El nombre `skills/` en la raíz de Skillbook es una convención del catálogo, no una ubicación de descubrimiento por sí misma. Todas las skills del catálogo tienen entrada nativa; la migración incluye frontmatter compatible y enlaces a sus instrucciones.

Para una copia manual en Windows, ejecuta desde la raíz de Skillbook:

```powershell
$skillName = 'evidence-guided-development'
$skillSource = Join-Path (Get-Location).Path ('skills\' + $skillName)
$skillRoot = Join-Path $env:USERPROFILE '.agents\skills'
$skillDestination = Join-Path $skillRoot $skillName
if (-not (Test-Path -LiteralPath (Join-Path $skillSource 'SKILL.md') -PathType Leaf)) {
    throw 'Run this command from the Skillbook repository containing the native skill.'
}
if (Test-Path -LiteralPath $skillDestination) {
    throw 'The destination already exists. Compare the versions before updating it.'
}
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillDestination -Recurse
```

Usa la ubicación personal reconocida por tu versión. Para instalar solo en un proyecto, cambia `$skillRoot` a su `.agents\skills`. Una skill de proyecto viaja con el repositorio; una copia personal debe instalarse en cada equipo.

Después de copiarla, comprueba que el selector de skills la muestre; abre una conversación nueva o reinicia Codex si no aparece. La invocación explícita es:

```text
$evidence-guided-development Analiza la migración de este sistema a Azure App Service usando el contexto del proyecto.
```

La descripción permite selección implícita al describir una tarea pertinente de análisis, implementación, refactor, reglas, datos, HU o documentación. No equivale a ejecución determinista. Si un proyecto necesita reforzar ese uso, puede añadir a su `AGENTS.md` una regla acotada:

```text
Para el trabajo de desarrollo de este sistema, usa evidence-guided-development y consulta primero el contexto existente. Adapta la profundidad a la tarea: los cambios triviales siguen una vía breve; las decisiones sustantivas requieren evidencia pertinente.
```

## Otro equipo y otros LLMs

La versión `1.0.0` experimental de `evidence-guided-development` sustituye a `applied-architecture-review`. Si ya instalaste la anterior, conserva una copia fuera de los directorios de descubrimiento, instala la nueva y actualiza las invocaciones. No mantengas ambas activas para el mismo flujo. El contrato ahora entrega código, pruebas, HU, documentación o análisis según el pedido.

Puedes transferir la carpeta por ZIP o desde GitHub. No necesitas un plugin. Si la versión ya está publicada en el repositorio, puedes pedir a Codex:

```text
Usa skill-installer para instalar la skill evidence-guided-development desde jmanuelsoberano/llm-skill-runbooks, ruta skills/evidence-guided-development. Comprueba primero si ya existe y verifica que Codex la descubra. Conserva y retira del descubrimiento la antigua applied-architecture-review si está instalada. Añade a mis instrucciones personales una regla breve para aplicar evidence-guided-development al trabajo de software con profundidad proporcional, preservando las instrucciones existentes. Configura O'Reilly Search por separado solo si falta y completa su autenticación local sin copiar credenciales de otro equipo.
```

Ese prompt requiere que la carpeta exista en la revisión remota seleccionada; crear una copia local no publica cambios en GitHub.

En un LLM sin soporte de skills, adjunta `prompt.full.md`, los contratos y el contexto, y pide el análisis. En otro agente compatible, conserva la carpeta completa y usa la ubicación de descubrimiento documentada por ese cliente. Las capacidades de navegación, MCP y archivos deben comprobarse por separado.

## Autenticación y contexto

La skill no contiene credenciales ni concede acceso a O'Reilly. Search, Expert y la lectura del navegador requieren las capacidades y autorizaciones correspondientes. Instalar la skill en otro equipo no transfiere esas sesiones.

Conserva `system-context.md` o su equivalente en el proyecto del sistema. No subas contexto privado ni informes internos al repositorio público de skills.

## Validación y límites

`python scripts/validate_repo.py` verifica todas las entradas del catálogo, sus metadatos, registro, archivos y referencias desde `SKILL.md`. Requiere instalar primero `requirements-dev.txt`. No valida el comportamiento del agente ni autenticación. Cada skill tiene checklist y casos; consulta [cómo evaluar](how-to-run-evals.md).

Un plugin es una opción posterior para distribuir skills y conexiones como paquete. No es un requisito para compartir carpetas con usuarios que configuren sus propios clientes.

Fuente oficial consultada: [crear y descubrir skills en Codex](https://learn.chatgpt.com/docs/build-skills).
