# Contratos de skills

Una skill tiene tres contratos:

1. Contrato de entrada.
2. Contrato de salida.
3. Contrato de calidad.

## Contrato de entrada

Define qué información acepta la skill.

Debe responder:

- ¿Qué formatos acepta?
- ¿Qué campos son obligatorios?
- ¿Qué campos son opcionales?
- ¿Qué hacer si falta información?
- ¿Qué hacer si la entrada viene como archivo?

## Contrato de salida

Define qué produce la skill.

Debe responder:

- ¿Markdown, JSON, YAML u otro?
- ¿Qué secciones son obligatorias?
- ¿Qué tablas debe incluir?
- ¿Qué valores permitidos existen?
- ¿Cómo se marca incertidumbre?

## Contrato de calidad

Define cómo evaluar la salida.

Debe responder:

- ¿Qué se considera correcto?
- ¿Qué se considera error?
- ¿Qué evidencia debe incluirse?
- ¿Cómo detectar invenciones?
- ¿Cómo verificar que es reutilizable?

## Regla de compatibilidad

Una skill estable no debe cambiar su contrato de salida sin subir versión mayor.
