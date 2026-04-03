# NVIDIA NIM LLM API

## Summary

Use NVIDIA NIM when integrating through NVIDIA's official hosted LLM API or related self-hosted NIM deployments. NVIDIA's hosted LLM API exposes an OpenAI-chat-completions-style interface for a wide set of models under a single official endpoint.

## Auth and Base URL

- Base URL: `https://integrate.api.nvidia.com`
- Primary endpoint: `POST /v1/chat/completions`
- Auth header: `Authorization: Bearer $NVIDIA_API_KEY`

## Primary text-generation endpoint

- `POST /v1/chat/completions`

## Minimal request

```bash
curl https://integrate.api.nvidia.com/v1/chat/completions \
  -H "Authorization: Bearer $NVIDIA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "yi-large",
    "messages": [
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

## Response shape

NVIDIA's hosted LLM API uses an OpenAI-like chat-completions response envelope.

## Streaming notes

If streaming is enabled for the selected model, treat it as an OpenAI-style streaming interface unless the model-specific docs for that NIM deployment say otherwise.

## Tool-calling notes

OpenAI-style tool semantics are the right mental model for compatible hosted usage, but feature support can vary by model family. Verify per-model capabilities when building anything beyond basic chat generation.

## Structured-output notes

Because NVIDIA's hosted interface is chat-completions-style, structured-output strategy should follow the compatibility surface exposed for the specific model deployment. Do not assume feature parity across every model listed by NVIDIA.

## Common pitfalls

- Assuming all models in the catalog support the same features
- Treating hosted NIM and self-hosted localized NIM as identical operational environments
- Assuming compatibility details without checking the model-specific endpoint notes

## Sources

- NVIDIA NIM LLM APIs reference: <https://docs.api.nvidia.com/nim/reference/llm-apis>
