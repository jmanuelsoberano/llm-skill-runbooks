# Cómo correr evaluaciones

## 1. Estructura del catálogo

En un entorno con Python 3.10 o superior:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

Se validan YAML sin claves duplicadas, esquemas de frontmatter y registro, correspondencia de ID/versión/estado, nombres exactos, archivos requeridos y enlaces convencionales desde cada `SKILL.md`.

El validador debe rechazar archivos vacíos, procedimientos sin enlace, rutas inexistentes o dependencias fuera del paquete. Los tests usan repositorios temporales y no llaman a MCP ni a un modelo.

`schemas/agent-skill.schema.json` describe la entrada nativa con requisitos adicionales del catálogo. `schemas/skill.schema.json` describe cada entrada de `registry.yaml`. El esquema de casos de prueba existente se conserva para evaluaciones que utilicen ese formato; este comando no ejecuta esos casos.

## 2. Descubrimiento en el cliente

Copia la carpeta completa a una ubicación reconocida por el cliente de pruebas y verifica nombre, descripción, habilitación y errores de carga. Si hay una instalación personal de la misma skill, evita confundirla con la copia evaluada: comprueba también la ruta.

El descubrimiento demuestra que el cliente puede cargar la entrada. No demuestra selección implícita correcta ni ejecución del procedimiento.

## 3. Comportamiento

Usa `evals/agent-cases.md` en las cuatro skills migradas, o `evals/cases.md` en desarrollo con evidencia, además de los casos históricos que tenga cada skill.

1. Da al agente la solicitud y el material fuente. No entregues la respuesta esperada como parte de las instrucciones.
2. Ejecuta las acciones locales en un directorio temporal; usa herramientas simuladas para efectos externos salvo autorización específica.
3. Conserva la entrada, salida, fecha, cliente/modelo, variante usada y archivos producidos.
4. Revisa el contrato y la checklist: evidencia, incertidumbre, cobertura y límites del pedido. Evita puntuar por coincidencia literal.
5. Registra si el evaluador fue el mismo agente o un revisor independiente.

Un caso no ejecutado debe permanecer como pendiente. No presentes una checklist redactada como prueba aprobada.

## 4. Evaluación independiente, cuando aporte valor

Si la skill dispone de `evals/evaluator.prompt.md`, úsalo con la entrada, la salida real y su checklist. También puede revisar una persona u otro agente autorizado. No todas las skills del catálogo tienen un prompt de juez.

Compara semántica y estructura con los ejemplos pertinentes. Si una variante rápida tiene un formato propio, usa su contrato específico y no la penalices por no producir el análisis completo.
