# Novita AI API

## Summary

Use Novita AI when integrating through Novita's official hosted platform. For LLM APIs, Novita explicitly documents OpenAI compatibility as the primary development path, while also exposing broader platform APIs for billing, account management, images, video, and instances.

## Auth and Base URL

Base URLs documented by Novita:

- General API base: `https://api.novita.ai`
- OpenAI-compatible base: `https://api.novita.ai/openai`

Auth header:

- `Authorization: Bearer $NOVITA_API_KEY`

## Primary LLM access pattern

For LLM integration, Novita explicitly says to use the OpenAI API standard. That means:

- OpenAI SDKs can often be reused
- the runtime path should be treated as OpenAI-compatible, not as a native vendor-specific schema

## Minimal request

```bash
curl https://api.novita.ai/openai/chat/completions \
  -H "Authorization: Bearer $NOVITA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek/deepseek-r1",
    "messages": [
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

## Response shape

For OpenAI-compatible LLM usage, response shape is OpenAI-like chat completions. Use model-specific feature expectations carefully because Novita fronts multiple upstream models.

## Operational notes

Novita's docs make it clear that the platform is broader than one chat endpoint:

- account and billing APIs
- image and video APIs
- compute and deployment APIs

This matters because the same platform key may be used across many API groups.

## Common pitfalls

- Treating Novita as a native model vendor instead of a hosted aggregation layer
- Assuming all upstream models behave identically just because the surface is OpenAI-compatible
- Mixing general base URLs and the OpenAI-compatible base without noticing which one your client expects

## Sources

- Novita API reference overview: <https://novita.ai/docs/api-reference>
- Novita authentication: <https://novita.ai/docs/api-reference/basic-authentication>
- Novita model APIs introduction: <https://novita.ai/docs/api-reference/model-apis-introduction>
- Novita OWL guide with OpenAI-compatible endpoint note: <https://novita.ai/docs/guides/owl>
