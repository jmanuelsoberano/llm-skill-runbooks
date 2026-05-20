# Reunión sobre integración del portal con reportes

## 1. Resumen ejecutivo

- Se revisó el estado de la integración del portal con el repositorio de reportes.
- Se identificó la necesidad de mostrar el estatus del reporte antes de permitir su descarga.
- Se detectaron posibles cambios en backend, API y base de datos.
- Se asignaron acciones a Pedro, Luis y Marta.
- La estimación queda pendiente hasta confirmar si la API ya devuelve el campo requerido.

## 2. Contexto general

La reunión trató sobre una integración entre un portal y un repositorio de reportes. El problema principal es que los usuarios necesitan ver el estatus del reporte antes de descargarlo para reducir tickets de soporte.

## 3. Participantes identificados

| Participante | Rol / Área / Equipo | Participación relevante | Nivel de certeza |
|---|---|---|---|
| Ana | No especificado | Coordina acuerdos y tareas | Media |
| Luis | Técnico / Backend o API | Revisa endpoint y factibilidad | Media |
| Marta | Negocio | Explica necesidad y validación con seguridad | Media |
| Pedro | Técnico / Datos | Revisará modelo de datos | Media |

## 4. Temas principales tratados

### Tema 1: Visualización del estatus del reporte

**Descripción:**  
Se necesita que el portal muestre el estatus del reporte antes de descargarlo.

**Puntos importantes:**

- Negocio lo solicita para reducir tickets de soporte.
- Puede requerir cambios en backend, API y base de datos.
- Hay duda sobre permisos por rol.

**Personas involucradas:**  
Ana, Luis, Marta, Pedro.

**Conclusión del tema:**  
Pendiente de validaciones técnicas y de seguridad.

## 5. Decisiones tomadas

| Decisión | Contexto | Responsable o área relacionada | Evidencia del transcript | Nivel de certeza |
|---|---|---|---|---|
| Mostrar el estatus del reporte en pantalla como requerimiento | Necesidad de negocio para reducir tickets | Negocio / Producto / Tecnología | “queda como requerimiento mostrar el estatus del reporte” | Alta |

## 6. Compromisos, tareas y acciones pendientes

| ID | Acción / Compromiso | Responsable | Fecha límite | Dependencias | Prioridad sugerida | Estado sugerido | Evidencia |
|---|---|---|---|---|---|---|---|
| A-001 | Revisar modelo de datos | Pedro | Mañana | Acceso a base de datos | Alta | Pendiente | “Yo puedo revisar el modelo de datos mañana” |
| A-002 | Revisar si el endpoint devuelve estatus y fecha de actualización | Luis | No especificado | API de reportes | Alta | Pendiente | “Luis revisa endpoint” |
| A-003 | Confirmar regla de visibilidad con seguridad | Marta | No especificado | Equipo de seguridad | Alta | Pendiente | “Marta confirma regla con seguridad” |

## 7. Preguntas abiertas y puntos por confirmar

| Pregunta o punto pendiente | Por qué importa | Quién debería aclararlo | Urgencia sugerida |
|---|---|---|---|
| ¿La API ya devuelve el campo de estatus? | Define esfuerzo técnico | Luis | Alta |
| ¿Existe columna de estatus en base de datos? | Define cambio de datos | Pedro | Alta |
| ¿Qué roles pueden ver el estatus? | Impacta seguridad y UX | Marta / Seguridad | Alta |

## 8. Riesgos, bloqueos y dependencias

| Riesgo / Bloqueo / Dependencia | Impacto potencial | Probabilidad estimada | Mitigación sugerida | Evidencia |
|---|---|---|---|---|
| La API no devuelve el campo requerido | Aumenta esfuerzo y requiere coordinación con integraciones | Media | Validar endpoint antes de estimar | “Si la API ya trae el campo...” |
| Restricción por roles no definida | Puede bloquear diseño funcional | Media | Confirmar regla con seguridad | “confirmar con seguridad...” |

## 9. Requerimientos identificados

### 9.1 Requerimientos funcionales

| Requerimiento | Descripción | Usuario / Área beneficiada | Prioridad sugerida | Nivel de certeza |
|---|---|---|---|---|
| Mostrar estatus del reporte | El portal debe mostrar el estatus antes de descargar | Usuarios / Soporte | Alta | Alta |

### 9.2 Requerimientos técnicos

| Requerimiento técnico | Sistema / Repositorio / Componente relacionado | Implicación técnica | Dependencias | Nivel de certeza |
|---|---|---|---|---|
| Exponer estatus y fecha de actualización | API de reportes | Revisar endpoint o agregar campos | Equipo de integraciones | Media |
| Verificar persistencia del estatus | Base de datos de reportes | Posible nueva columna | Modelo de datos | Media |

## 10. Posibles issues o tickets para repositorio

### Issue sugerido #1: Mostrar estatus del reporte en el portal

**Tipo:**  
Feature

**Descripción:**  
Agregar visualización del estatus del reporte antes de la descarga.

**Criterios de aceptación sugeridos:**

- El usuario puede ver el estatus del reporte.
- El estatus respeta reglas de visibilidad por rol.
- Se muestra la fecha de última actualización si está disponible.

**Responsable sugerido:**  
No especificado

**Prioridad sugerida:**  
Alta

**Dependencias:**  
Validación de API, base de datos y seguridad.

## 17. Resumen ultra breve

Se acordó avanzar con la visualización del estatus de reportes en el portal. Pedro revisará base de datos, Luis revisará el endpoint y Marta confirmará permisos con seguridad. La estimación queda pendiente hasta validar si la API ya trae los campos necesarios.
