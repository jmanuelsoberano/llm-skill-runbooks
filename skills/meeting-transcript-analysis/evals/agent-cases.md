# Casos de entrada nativa

Estos casos prueban selección y comportamiento. Ejecutarlos requiere un agente; el validador del catálogo solo comprueba estructura y referencias. Usa también la checklist del análisis.

| Caso | Entrada | Procedimiento esperado | Criterios observables |
|---|---|---|---|
| M1 | «Analiza completo: Ana propone revisar el exportador. Luis dice que falta confirmar al responsable y la fecha». | Completo | Conserva el formato completo. Separa propuesta de decisión; no asigna responsable ni fecha. |
| M2 | «Resumen rápido de esta reunión», con un archivo de texto accesible. | Rápido, leyendo el archivo | Usa la estructura breve y el contenido real; no pide pegarlo otra vez. |
| M3 | Dos transcripts: reunión A propone desplegar el viernes; reunión B descarta esa fecha. | Múltiples reuniones | Mantiene la procedencia y registra el cambio de criterio; no presenta ambas fechas como acuerdos vigentes. |
| M4 | «Parte 1/2: Ana revisará los logs». Después: «Parte 2/2: no hay fecha acordada. FIN DEL TRANSCRIPT». | Por partes | Tras la primera entrada confirma recepción sin documento final ni solicitud de la primera parte. Tras el cierre entrega el análisis completo con fecha no especificada. |
| M5 | «Analiza el archivo adjunto», pero el cliente no puede leerlo. | Archivo, con limitación explícita | No inventa contenido ni afirma haber leído el archivo; explica qué falta para analizarlo. |

Para registrar una ejecución, conserva entrada, salida, cliente/modelo, fecha, variante aplicada y resultado de la checklist. No publiques transcripts privados como fixtures.
