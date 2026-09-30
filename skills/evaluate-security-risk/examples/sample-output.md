# Salida de ejemplo sintética

## Alcance
Lectura de documentos multi-tenant descrita por el usuario. No se inspeccionó una implementación real ni se ejecutaron solicitudes.

## SEC-01 — Autorización por tenant ausente en la consulta descrita
**Importante; evidencia reportada.** Un usuario autenticado que obtenga un identificador ajeno podría consultar un documento de otro tenant. El filtro visual no restringe solicitudes directas.

- **E1:** descripción de FindById(id), discovery_kind: project_artifact; access: read; claim_relation: supports. Se leyó el escenario, no código desplegado.
- **Aplicación:** si el flujo descrito no tiene otro control de pertenencia, existe exposición de datos. Comprobar filtros globales u otros controles antes de afirmar el alcance definitivo.
- **Tratamiento:** resolver el documento dentro del tenant autenticado y comprobar permisos adicionales que requiera el negocio. Usar el tenant confiable del servidor.
- **Verificación propuesta:** usuario del tenant A consulta documento de B y recibe el resultado de denegación previsto por el contrato, sin contenido; usuario autorizado de A conserva acceso a su documento.
- **Riesgo residual:** otros endpoints y permisos dentro de un mismo tenant están fuera del análisis.

No hay resultados de ejecución ni seguridad global acreditada.

