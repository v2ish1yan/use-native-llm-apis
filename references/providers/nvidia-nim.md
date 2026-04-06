# NVIDIA NIM LLM API

## Summary

Use NVIDIA NIM when integrating through NVIDIA's official hosted LLM API or related self-hosted NIM deployments. NVIDIA's hosted LLM API exposes an official OpenAI-chat-completions-style interface for a wide set of models under one endpoint.

Treat hosted NIM as an official compatibility surface with model-specific capability differences.

## Auth and Base URL

- Base URL: `https://integrate.api.nvidia.com`
- Primary endpoint: `POST /v1/chat/completions`
- Auth header: `Authorization: Bearer $NVIDIA_API_KEY`
- Content type: `application/json`

## Primary text-generation endpoint

- `POST /v1/chat/completions`

The official API reference explicitly describes this route as OpenAI-compatible chat completions.

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

Typical response field for text:

- `choices[0].message.content`

## Response and model behavior

NVIDIA's hosted LLM API uses an OpenAI-like chat-completions response envelope, but capabilities depend heavily on the selected model.

Practical rule:

- trust the transport shape
- verify advanced features per model page

## Streaming notes

If streaming is enabled for the selected model, treat it as an OpenAI-style streaming interface unless the model-specific docs say otherwise.

That means the safest parser expectation is:

- SSE
- OpenAI-style chunk accumulation
- finish conditions based on chat-completions semantics

## Tool-calling notes

NVIDIA model pages show that tool calling is model-dependent, not universally guaranteed.

For example, public model pages explicitly mention tool or function calling support for some models.

Practical rule:

- keep OpenAI-style tool semantics as the baseline
- verify tool support on the exact model page before shipping

## Structured-output notes

Structured output is also model-dependent.

Public model pages show examples where structured JSON output is supported, but not every hosted model page makes the same promise. So:

- start from OpenAI-compatible expectations
- confirm structured-output support on the target model page when strict parsing matters

## Hosted vs self-hosted NIM

Do not assume hosted NIM and self-hosted localized NIM are operationally identical.

The hosted API gives:

- one official OpenAI-compatible endpoint
- managed auth and routing

Self-hosted NIM may differ in:

- deployment topology
- model availability
- operational controls

## Development guidance

When integrating NVIDIA NIM:

1. choose the exact target model first
2. send one minimal chat-completions request
3. verify text parsing on the OpenAI-style response envelope
4. check the target model page before adding streaming, tools, or structured output

## Common pitfalls

- Assuming all models in the catalog support the same features
- Treating hosted NIM and self-hosted localized NIM as identical environments
- Assuming tool calling or JSON output without checking the model-specific page
- Mistaking model-card capability notes for a platform-wide guarantee

## Sources

- NVIDIA NIM LLM APIs reference: <https://docs.api.nvidia.com/nim/reference/llm-apis>
- NVIDIA chat-completions route example: <https://docs.api.nvidia.com/nim/reference/mistralai-mixtral-8x22b-instruct-infer>
- NVIDIA model page with structured output and tool-calling notes: <https://docs.api.nvidia.com/nim/reference/z-ai-glm5>
