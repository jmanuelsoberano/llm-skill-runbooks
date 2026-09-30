---
name: evidence-guided-development
description: "Apoya el desarrollo de software con contexto del proyecto y evidencia consultada. Úsala para analizar, planificar, implementar, refactorizar, revisar o documentar cambios, incluidas reglas de negocio, datos e historias de usuario. Ajusta la investigación al riesgo y entrega lo solicitado: código, pruebas, HU, documentación o análisis. En tareas triviales aplica una vía breve; no inicia una investigación extensa por defecto."
metadata:
  id: "development.evidence.guided"
  version: "1.1.0"
  status: "experimental"
---

# Evidence-Guided Development

Completa el trabajo de desarrollo solicitado, usando el contexto del sistema y fuentes pertinentes para resolver dudas que afecten a la solución. Esta skill aporta el método de trabajo; no reemplaza herramientas o skills especializadas que sean necesarias para ejecutar la tarea.

Al ejecutar la skill:

1. Lee [prompt.full.md](prompt.full.md), que contiene el procedimiento común.
2. Usa [input.schema.md](input.schema.md) para interpretar la entrada y [output.schema.md](output.schema.md) para entregar el resultado apropiado. No obligues al usuario a completar un formulario ni a escoger un modo.
3. Lee solo las referencias que afecten a la tarea: [código y reglas](references/code-changes.md), [datos y contratos](references/data-changes.md), [HU y documentación](references/requirements-and-docs.md), o [arquitectura, migración y rendimiento](references/architecture-and-performance.md).
4. Si vas a consultar O'Reilly, lee [references/oreilly.md](references/oreilly.md) para distinguir búsqueda, lectura y acceso Expert.
5. Si falta contexto persistente y conviene conservarlo, adapta [assets/system-context-template.md](assets/system-context-template.md) al proyecto. Reutiliza primero la documentación existente.

En tareas triviales, lee el procedimiento común y aplica la vía breve sin cargar referencias innecesarias. Los ejemplos y evaluaciones se usan para mantener la skill, no como instrucciones del caso del usuario. Reutiliza conexiones existentes; instalar herramientas o configurar cuentas requiere que la tarea lo incluya.

## Integración modular

Usa [selección de especialidades](references/specialists.md) cuando la tarea necesite un procedimiento específico y el [contrato común de evidencia](references/evidence-contract.md) para hallazgos sustantivos. Selecciona únicamente los módulos pertinentes; la ausencia de otra skill no bloquea la vía general.
