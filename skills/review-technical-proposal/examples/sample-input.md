# Entrada sintética

RFC-12 propone POST /exports. Sección 2: devuelve 202 inmediatamente con el archivo final. Sección 3: generar el archivo tarda 10 minutos. Sección 4: reintentar automáticamente cualquier fallo; cada intento ejecuta un cobro nuevo y no hay clave idempotente. Solo necesito revisión escrita.
