# Contrato de entrada

Acepta lenguaje natural, documentos, adjuntos, enlaces accesibles y artefactos del proyecto. No exige un formulario ni que el usuario conozca los nombres de las skills. Usa primero el contexto disponible; pregunta únicamente por omisiones que puedan cambiar sustancialmente el resultado. Marca `No especificado`, `Ambiguo`, `Requiere confirmación` o `Inferencia` según corresponda. Un dato reportado por el usuario no se convierte en una medición ejecutada por el asistente.

## Información útil

- Cambio solicitado y significado de los datos, reglas e invariantes.
- Esquema, motor/versión y contratos de productores/consumidores.
- Volumen, calidad, distribución y patrones de lectura/escritura.
- Disponibilidad requerida, coexistencia de versiones y restricciones operativas.
- Fuente para backfill, casos ambiguos, recuperación y entorno autorizado.

La entrada mínima es un cambio de datos y su intención. Si faltan significado, obligatoriedad o valor inicial para registros existentes, identifica la decisión pendiente sin rellenarla con un default arbitrario.
