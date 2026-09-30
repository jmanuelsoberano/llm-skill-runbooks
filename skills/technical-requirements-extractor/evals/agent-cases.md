# Casos de entrada nativa

Evalúa con la checklist existente. La verificación estructural no certifica exactitud de extracción.

| Caso | Entrada | Criterios observables |
|---|---|---|
| T1 | «La exportación debe conservar los filtros. Podríamos usar una cola; aún no está decidido. No se documentó el stack». | Conservación de filtros confirmada; cola como propuesta o inferencia. Stack `No especificado`; no inventa Azure, SQL Server ni microservicios. |
| T2 | «Debe ser rápido y soportar muchos usuarios». | No inventa un SLO ni un volumen. Pregunta por latencia, concurrencia, carga y mediciones necesarias para estimar. |
| T3 | Un documento enumera responsabilidades de dos componentes, pero omite quién consume la API. | Mantiene los nombres suministrados; identifica dependencia y consumidor pendiente sin inventar un equipo. |
| T4 | «Extrae requisitos antes de estimar; no implementes». | Entrega las secciones del contrato, evidencia, certeza, supuestos explícitos e información para estimar. No modifica código ni crea tickets. |

Conserva entrada, salida, cliente/modelo, fecha y observaciones. No puntúes por coincidencia literal: comprueba contratos, evidencia y manejo de incertidumbre.
