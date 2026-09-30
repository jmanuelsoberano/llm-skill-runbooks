# Salida ilustrativa — datos sintéticos

**Propuesta condicionada:** introducir el dato de forma compatible y resolver el significado de los valores históricos desconocidos antes de exigirlo para todos los registros.

1. **Semántica.** E1 exige PERSON u ORGANIZATION para nuevas altas. E2 indica históricos sin clasificación posible. No asignar PERSON por defecto: afirmaría una propiedad no comprobada. La representación de desconocido requiere decisión de negocio.
2. **Compatibilidad.** Durante las 48 h reportadas [E3], lectores antiguos deben tolerar el cambio y las altas de escritores antiguos necesitan un tratamiento explícito. La validación nueva no puede darse por aplicada a esas rutas.
3. **Backfill propuesto.** Clasificar solo desde una fuente fiable, registrar los no determinables y permitir reanudar sin sobrescribir datos corregidos concurrentemente. La mecánica de lotes e índices depende del motor y volumen pendientes.
4. **Verificar.** Nuevas altas válidas e inválidas, lectura de históricos desconocidos, coexistencia de versiones y equivalencia entre clasificación y fuente de verdad. Comparar conteos por estado y casos individuales; los conteos solos son insuficientes.
5. **Recuperación.** Conservar temporalmente la compatibilidad con el esquema previo. Retirar esa compatibilidad requiere comprobar que ya no hay escritores antiguos y que la nueva obligatoriedad es válida.

**Límites:** las condiciones proceden de la solicitud sintética. No se inspeccionó una base ni documentación de un motor concreto. No se ejecutó migración ni se acredita ausencia de bloqueos.
