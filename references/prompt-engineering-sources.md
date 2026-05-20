# Fuentes y fundamentos

Última revisión: 2026-05-20

Este starter kit está inspirado en prácticas recomendadas ampliamente aceptadas para diseño de prompts y prompts reutilizables.

## Fuentes oficiales consultadas

- OpenAI Help Center: Best practices for prompt engineering with the OpenAI API  
  https://help.openai.com/en/articles/6654000-playground-and-prompt-engineering

- OpenAI Academy: Prompting fundamentals  
  https://openai.com/academy/prompting/

- Anthropic Documentation: Prompt engineering overview  
  https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview

- Google Cloud Vertex AI: Introduction to prompting  
  https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design

- Google Cloud Vertex AI: Overview of prompting strategies  
  https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies

- Google Cloud Vertex AI: Structure prompts  
  https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/structure-prompts

## Decisiones de diseño derivadas

1. Separar tarea, contexto, instrucciones y formato de salida.
2. Usar delimitadores claros para entradas largas.
3. Definir éxito y criterios de evaluación antes de optimizar.
4. Incluir ejemplos cuando el formato deseado sea complejo.
5. Versionar prompts y skills.
6. Diseñar prompts iterables y evaluables.
7. Evitar que el prompt dependa de un solo modelo cuando se busca portabilidad.
