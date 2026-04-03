# Alibaba Bailian / DashScope API

## Summary

Use Alibaba Bailian / DashScope when integrating Qwen-family models through Alibaba Cloud's official platform. Public documentation commonly exposes two access styles:

- OpenAI-compatible endpoints
- DashScope-native endpoints

For development speed and documentation stability, this reference starts with the official OpenAI-compatible layer because it is currently the most implementation-ready public path for mainstream chat integrations.

## Auth and Base URL

Mainland China compatible-mode base URL:

- `https://dashscope.aliyuncs.com/compatible-mode/v1`

Other documented regions include:

- Singapore: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
- US Virginia: `https://dashscope-us.aliyuncs.com/compatible-mode/v1`

Auth header:

- `Authorization: Bearer $DASHSCOPE_API_KEY`

## Primary text-generation endpoint

- `POST /chat/completions`

Combined mainland URL:

- `https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions`

## Minimal request

```bash
curl https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-plus",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

## Response shape

Common fields to read:

- `id`
- `model`
- `choices`
- `choices[0].message`
- `usage`

The compatible-mode response is intentionally OpenAI-chat-completions-like.

## Streaming notes

- Enable with `"stream": true`
- Expect an OpenAI-like SSE stream in compatible mode
- Incremental content is typically exposed through delta-style chunks

If streaming behavior differs unexpectedly, first verify that the target model supports streaming in the selected region and access mode.

## Tool-calling notes

Bailian's compatible mode supports tool-calling patterns for supported Qwen models. The request shape follows the OpenAI-style `tools` pattern closely enough to be familiar, but you should still validate:

- model support
- region support
- schema restrictions for the chosen model

## Structured-output notes

Compatible mode can be a practical way to request structured output on supported models. If the task requires the strongest provider-native guarantees, check whether the model's DashScope-native documentation offers a more explicit structured-output path.

## Multimodal notes

Alibaba documents multimodal and OCR-capable Qwen models through compatible-mode examples as well. Keep in mind that multimodal payload support is model-specific; do not generalize from one Qwen model to all Qwen models.

## Embeddings notes

DashScope offers broader API families beyond chat completions. Verify embeddings through the official model-specific or endpoint-specific docs instead of assuming chat-compatible conventions.

## Common pitfalls

- Mixing region-specific API keys and base URLs
- Assuming all Qwen-family models support the same access mode
- Assuming compatible mode and native DashScope mode have identical parameters
- Forgetting that some Alibaba docs are model-specific rather than platform-generic

## Sources

- Alibaba compatibility guide: <https://help.aliyun.com/zh/model-studio/compatibility-of-openai-with-dashscope>
- Alibaba OpenAI chat reference: <https://help.aliyun.com/zh/model-studio/qwen-api-via-openai-chat-completions>
- Alibaba regions guide: <https://help.aliyun.com/zh/model-studio/regions/>
