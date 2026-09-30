# Salida ilustrativa — datos sintéticos

**Recomendación:** probar un contrato de solicitud y una revisión conjunta breve para los cambios de esquema, preservando la administración productiva en Data.

**Evidencia y diagnóstico.** E1 contiene tiempos reportados de 8 solicitudes: la espera mediana supera la ejecución. E2 registra 6 sistemas operados por Data. Esto sustenta investigar priorización e interrupciones; no demuestra que sean la causa ni permite evaluar a personas.

| Responsabilidad | Situación reportada | Propuesta de piloto |
|---|---|---|
| Definición funcional | Checkout | Checkout aporta invariantes y aceptación. |
| Revisión de compatibilidad | No especificado | Acordar revisión conjunta y lista mínima de datos. |
| Administración productiva | Data | Conservarla según la restricción recibida. |

**Verificar.** Recoger para cada solicitud fecha de entrada, faltantes, bloqueos y finalización. Comparar la espera por tipo de cambio, sin sumar medianas como si describieran la misma solicitud.

**Riesgo.** Una ventana fija puede aumentar espera de urgencias; acordar tratamiento de incidentes. Periodo y responsables del piloto: requieren confirmación. No se modificó ningún equipo ni permiso.
