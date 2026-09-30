# Entrada sintética

Tenemos una base relacional con transacciones. Al aceptar un pedido debemos asegurar que el trabajo de notificación pueda recuperarse. Compara guardar y luego publicar al broker contra una outbox transaccional. El consumidor puede deduplicar por notificationId. Solo análisis, sin modificar archivos.
