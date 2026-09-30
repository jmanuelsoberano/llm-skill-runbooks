# Procedimiento: revisión de cambios de código

## Intención y base de comparación

Identifica la intención, los archivos y la base real del cambio: diff, commit, rama o archivos recibidos. Comprueba si el cambio agrega comportamiento, corrige un defecto o pretende ser un refactor que conserve contratos. Lee instrucciones del repositorio y contexto suficiente de consumidores, contratos, pruebas y rutas afectadas. Un fragmento puede ser insuficiente para inferir el comportamiento de todo el sistema.

Distingue modificaciones previas del usuario de la revisión actual. No cambies código, staging, dependencias ni configuración cuando el encargo sea revisar. Preparar comentarios no autoriza publicarlos ni aprobar, rechazar o fusionar un PR.

## Revisión orientada a riesgos

1. Sigue las rutas afectadas desde entrada hasta efectos observables: validación, autorización, dominio, persistencia y respuestas o eventos. Examina errores, ausencia, límites y concurrencia relevantes, sin recorrer el repositorio completo por defecto.
2. Contrasta contrato anterior y nuevo. En un refactor revisa también errores, efectos secundarios, orden y compatibilidad de consumidores; no corrijas silenciosamente una conducta inesperada ni atribuyas toda diferencia al nuevo cambio.
3. Revisa reglas e invariantes en su ubicación real. Señala duplicación cuando permite divergencia concreta, no por contar líneas similares. Respeta los patrones existentes salvo un problema justificado.
4. Para datos, comprueba compatibilidad de lectura/escritura y efectos parciales. Para seguridad, examina límites de confianza, autorización, secretos y entradas en las rutas modificadas. Para rendimiento, evita pronosticar ganancias o degradaciones sin un mecanismo plausible; mide si el contexto autorizado lo permite.
5. Evalúa pruebas por escenarios y regresiones, no solo cobertura o presencia de archivos. Distingue una prueba ausente que deja un riesgo demostrado de una sugerencia de cobertura adicional. No escribas pruebas para repetir la implementación sin validar un contrato.
6. Ejecuta verificaciones relevantes y permitidas cuando aporten evidencia, preservando el alcance. Inspecciona antes scripts que podrían instalar, modificar entornos externos o tocar datos reales. No declares que compila o pasa pruebas si solo leíste el código; un error de entorno no equivale a un defecto del cambio.
7. Verifica detalles de API o versión en documentación oficial vigente accesible cuando determinen un hallazgo. Las fuentes explican mecanismos; el código y sus contratos sostienen el defecto concreto. Reutiliza evidencia existente en lugar de repetir investigaciones.

## Hallazgos

Un hallazgo útil permite identificar la condición que dispara el problema, su efecto y una corrección proporcional. Incluye archivo y línea verificados o símbolo cuando no haya líneas fiables. Evita rangos extensos y agrupa manifestaciones de una misma causa.

Usa severidades:
- **Crítico:** riesgo material acreditado de daño grave a seguridad, integridad o operación.
- **Importante:** incumplimiento de contrato, regresión o riesgo que requiere corrección antes de aceptar.
- **Sugerencia:** mejora con beneficio claro sin defecto bloqueante demostrado.

La incertidumbre cambia la redacción: formula una pregunta o verificación pendiente si faltan datos para acreditar el defecto. No llenes la revisión con problemas hipotéticos ni selecciones una severidad solo para llamar atención.

Si no encuentras defectos, indícalo con el alcance examinado y verificaciones pendientes; no equivale a certificar ausencia de errores. Si el usuario también solicita arreglos, conserva esa autorización y trata los cambios como una etapa explícita, con verificación pertinente; no transformes una revisión restringida en implementación.

## Evidencia y alcance

Aplica [el contrato común de evidencia](references/evidence-contract.md). Reutiliza hallazgos con identificadores y comprueba si su versión y contexto siguen siendo pertinentes. Distingue la afirmación de la fuente de su aplicación al proyecto; declara supuestos, objeciones y datos faltantes. Una referencia encontrada o una respuesta de Answers no equivale a haber leído su pasaje.

Selecciona fuentes en proporción a la decisión. Si `oreilly-research` está descubierta y aporta, puedes usarla para obtener evidencia; su ausencia no bloquea el trabajo. Si el usuario solicita una fuente o Answers expresamente, intenta ese acceso mediante herramientas disponibles y comunica cualquier bloqueo. No asumas herramientas Expert ni acceso por una suscripción distinta. Consulta documentación oficial vigente para detalles dependientes de versiones cuando sea necesario. Envía a consultas externas solo contexto técnico mínimo y autorizado.

Puedes trabajar de forma autónoma con el material accesible o devolver tu resultado a un coordinador. No invoques recursivamente `evidence-guided-development`. La elaboración o revisión de un documento no autoriza publicarlo, modificar sistemas, comprometer fechas ni comunicar decisiones a terceros. Respeta el entregable solicitado y distingue comprobaciones ejecutadas de propuestas.
