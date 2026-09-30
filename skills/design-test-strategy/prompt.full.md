# Procedimiento

## Contexto y riesgos
Lee cambio/requisitos, contratos, reglas de negocio, arquitectura y pruebas existentes. Identifica comportamiento observable, invariantes, consumidores, estados y datos afectados. Separa requisito confirmado, comportamiento actual e inferencia. Una prueba que congela un bug o una regla ambigua no resuelve la definición del negocio.

Prioriza por impacto, probabilidad razonada de regresión, detectabilidad y costo de recuperación. Ajusta profundidad al cambio: una corrección reversible de presentación puede requerir una comprobación breve; dinero, permisos, concurrencia, compatibilidad o migración suelen necesitar casos específicos. No impongas porcentajes de cobertura o pirámides numéricas sin justificación del proyecto.

## Casos y niveles
Deriva escenarios de comportamiento: caso esperado, límites, errores, permisos, estados/transiciones, idempotencia, concurrencia y compatibilidad solo cuando corresponda. Para cada riesgo identifica precondiciones, acción, resultado observable/oráculo y nivel más bajo que pueda comprobarlo de manera fiable.

Usa unitarias para reglas aisladas; integración para semántica real de persistencia/adaptadores; contrato para acuerdos entre consumidores/proveedores; extremo a extremo para recorridos críticos que no quedan cubiertos de forma suficiente. Las categorías orientan la elección, no obligan a añadir todas. No simules precisamente el comportamiento externo cuya semántica necesitas validar.

Pruebas basadas en propiedades, fuzzing, carga o fallos son opciones cuando resuelven un riesgo real; explicita límites y entorno. Reutiliza suite/herramientas existentes. Evita assertions que reproduzcan la implementación, exceso de mocks o snapshot sin una propiedad observable útil.

## Datos y ejecución
Define fixtures sintéticos o anonimizados autorizados, límites temporales, zona horaria, aleatoriedad reproducible cuando aplique y aislamiento/limpieza para efectos persistentes. No copie datos privados a herramientas externas. Para concurrencia describe intercalación o condición observada y evita depender solo de sleeps frágiles.

Ubica pruebas en desarrollo/CI/entorno autorizado según dependencias, tiempo y fidelidad. Define resultados que permiten aceptar el cambio y tratamiento de fallas; si hay flakiness, diagnostica causa y no conviertas reintentos en éxito silencioso. Distingue fallo de producto, prueba y entorno.

## Entrega y verificación
Si se pide estrategia, entrega selección y justificación; si se autoriza implementación, materializa casos prioritarios y ejecuta lo viable. Registra comandos/entorno solo cuando ayuden a reproducir; nunca declara ejecución por tener archivos o un plan.

Aplica references/evidence-contract.md. Consulta documentación oficial actual para garantías relevantes del framework/runtime. O'Reilly mediante oreilly-research disponible puede aportar técnicas sin ser requisito. No llama recursivamente a evidence-guided-development ni crea abstracciones de test sin variación concreta.

