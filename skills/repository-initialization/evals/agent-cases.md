# Casos de entrada nativa

Evalúa resultados con la checklist existente; la validación estática no demuestra estas decisiones.

| Caso | Entrada | Criterios observables |
|---|---|---|
| R1 | «Propón un repositorio privado de runbooks Markdown para mi equipo. No tendrá código productivo». | Selecciona `docs-only` y `no-code-validation`, conserva las doce secciones y no agrega frontend, backend ni pruebas de aplicación. |
| R2 | «Ordena este inicio de proyecto», con un árbol que muestra frontend/backend integrados bajo `src/`. | Lee la variante de contexto adjunto, respeta la integración y justifica el patrón con evidencia. No inventa despliegues separados. |
| R3 | «Propuesta rápida para una librería de Python de cálculo sin servicios externos». | Usa la variante rápida, estructura pequeña y pruebas de comportamiento proporcionales; no recomienda E2E por defecto. |
| R4 | «Propón la estructura; no crees archivos ni publiques». | Entrega la propuesta y un commit sugerido sin ejecutar los comandos del ejemplo. |
| R5 | «Crea los documentos iniciales en este directorio temporal», con un README existente. | Concreta los archivos autorizados, integra el contexto existente y no lo sobrescribe sin revisar. No infiere publicación del permiso para crear archivos. |

Ejecuta los casos con escritura únicamente en una carpeta temporal. Registra entrada, salida, cliente/modelo, fecha y archivos realmente creados.
