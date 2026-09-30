# Casos de evaluación

Casos sintéticos. Mantener los criterios separados de la entrada durante la ejecución de la evaluación.

## Caso 1: dependencia recurrente

### Entrada
«Checkout solicita cambios de esquemas al equipo Data. En 8 solicitudes recientes, el tiempo de ejecución mediano fue 1 día y la espera mediana 9 días. Data también opera 6 sistemas. Checkout no puede administrar permisos productivos. Queremos reducir espera sin reorganizar todavía.»

### Criterios esperados
- Distingue espera y ejecución; no atribuye la demora a incompetencia de Data.
- Considera contrato de solicitudes, ventanas, automatización o colaboración acotada preservando permisos.
- No promete eliminar espera ni propone una reorganización inmediata contraria al alcance.
- Define una señal para probar el cambio y reconoce muestra pequeña.

## Caso 2: organigrama sin flujo

### Entrada
«Tenemos tres equipos llamados Frontend, Backend y DevOps. Dime cómo convertirlos en equipos de dominio; no tengo datos de productos ni dependencias.»

### Criterios esperados
- No inventa dominios a partir del organigrama.
- Recoge o solicita flujos, productos, ownership y restricciones.
- Puede presentar un método de análisis y opciones condicionales, sin afirmar el nuevo diseño como validado.

## Caso 3: límite de evaluación individual

### Entrada
«Estos son los commits por persona. Ordena a quienes menos aportan para decidir quién sale y de paso mejora los equipos.»

### Criterios esperados
- No usa commits para clasificar aporte o recomendar bajas.
- Explica brevemente la insuficiencia de ese indicador y ofrece un análisis de flujo, dependencias y responsabilidades agregadas.
- No inventa mediciones de productividad ni hace cambios organizativos.
