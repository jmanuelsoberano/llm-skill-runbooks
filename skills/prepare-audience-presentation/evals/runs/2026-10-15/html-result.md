# Registro de la prueba local

## Solicitud

> Crea una presentación HTML que pueda abrir sin conexión para explicar en 5 minutos a ocho desarrolladores cómo preparar una revisión de código. Los puntos son: describir intención; aportar pruebas relevantes; señalar riesgos conocidos; responder comentarios. Quiero controles anterior/siguiente, navegación por teclado y notas breves para quien presenta. Usa solo estos datos; no inventes resultados ni estadísticas.

Restricciones de ejecución: escribir únicamente en la carpeta de esta prueba; no publicar, crear cuentas, instalar dependencias ni modificar el repositorio o las skills. Registrar solicitud, respuesta final y comprobaciones realizadas. No leer casos de evaluación ni ejemplos, ni autoevaluar con criterios externos.

## Artefacto

- Archivo entregable: `code-review-presentation.html`.
- Un único HTML con contenido, estilos y JavaScript integrados; utiliza fuentes del sistema.
- Seis diapositivas: apertura, los cuatro puntos solicitados y cierre.
- Notas breves por diapositiva. Reparto estimado de tiempo: 30 + 60 + 60 + 60 + 60 + 30 segundos.
- Controles anterior/siguiente, flechas, RePág/AvPág, Inicio/Fin y tecla N para notas.
- Las notas se abren en la misma pantalla; la interfaz lo indica.

## Recursos de ejecución leídos

De `prepare-audience-presentation`: `SKILL.md`, `input.schema.md`, `prompt.full.md`, `output.schema.md`, `references/presentation-guidance.md` y `references/sources.md`.

Para comprobar el archivo en un navegador local: skill `playwright` y rutas de dependencias incluidas en el entorno. No se instalaron paquetes. No se leyeron casos de evaluación, ejemplos ni listas de evaluación externas.

## Comprobaciones realmente realizadas

Ejecución local con Playwright disponible y Google Chrome 155.0.8059.79. Evidencia detallada: `browser-checks.json`. El script y las capturas se conservaron en el directorio temporal de la prueba; no se incluyen en este paquete.

1. Se abrió el archivo mediante `file://` en un contexto de navegador configurado sin conexión.
2. Se verificó el estado inicial: primera diapositiva visible, contador `1 / 6` y botón anterior desactivado.
3. Se pulsaron los botones siguiente y anterior, y se comprobó el cambio de diapositiva.
4. Se probaron flecha derecha, AvPág, flecha izquierda, RePág, Fin e Inicio; se comprobó que avanzar al final y retroceder al inicio no desbordan el rango.
5. Se abrieron notas con N, se comprobó `aria-expanded`, se cambió de diapositiva para verificar el tiempo y se cerraron con el botón.
6. Se recorrieron las seis diapositivas a 1280 × 800. Se comprobó una única diapositiva visible, ausencia de desbordamiento horizontal y contenido dentro del panel. El botón siguiente quedó desactivado en la última.
7. Se guardaron y revisaron visualmente las seis capturas `slide-1.png` a `slide-6.png`: títulos y contenido legibles, sin recortes visibles.
8. Se abrió la portada a 390 × 844 con notas. Se comprobó ausencia de desbordamiento horizontal y se revisó `mobile-notes.png`. Esta vista usa desplazamiento vertical para leer las notas.
9. No se registraron errores JavaScript ni solicitudes HTTP/HTTPS. La única solicitud de la página fue el propio archivo local.
10. Se inspeccionó el HTML: no contiene recursos externos de scripts, hojas de estilo, imágenes, marcos, audio o vídeo, ni importaciones o URLs CSS.

No se midió una exposición oral. Los cinco minutos son una distribución estimada que requiere ensayo de quien presenta. No se comprobó compatibilidad en otros navegadores ni se realizó una auditoría con lector de pantalla.

## Respuesta final

Creé la presentación HTML sin conexión en `code-review-presentation.html`.

Incluye seis diapositivas, controles, navegación por teclado y notas con una distribución estimada de cinco minutos. Verifiqué su apertura sin conexión, navegación, notas y las seis vistas en Chrome. El registro está en `html-result.md`.
