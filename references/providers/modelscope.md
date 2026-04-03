# ModelScope API Inference

## Summary

Use ModelScope API Inference when integrating open-source models through ModelScope's official hosted inference platform. The public API surface is primarily OpenAI-compatible for LLM usage, which makes it convenient for development while still being an official ModelScope service.

## Auth and Base URL

- Base URL: `https://api-inference.modelscope.cn/v1`
- Auth token: ModelScope SDK Token
- Auth header: `Authorization: Bearer $MODELSCOPE_TOKEN`
- Content type: `application/json`

## Primary text-generation endpoint

- `POST /chat/completions`

The model id is usually a ModelScope model identifier such as:

- `Qwen/Qwen2.5-Coder-32B-Instruct`
- other hosted open-source model ids supported by API Inference

## Minimal request

```bash
curl https://api-inference.modelscope.cn/v1/chat/completions \
  -H "Authorization: Bearer $MODELSCOPE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen2.5-Coder-32B-Instruct",
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

The public LLM examples use an OpenAI-compatible chat-completions envelope:

- `id`
- `model`
- `choices`
- `choices[0].message`
- `usage`

## Streaming notes

- Enable with `"stream": true`
- ModelScope examples show OpenAI-style streaming chunks
- Parse `choices[0].delta.content` as incremental text

## Tool-calling notes

Tool-calling support depends on the hosted model behind the API Inference endpoint. Because ModelScope fronts many open-source models, do not assume uniform tool capability across every model id.

## Structured-output notes

Use model-specific guidance where available. Since ModelScope hosts many model families, structured-output reliability depends more on the chosen model than on one universal platform rule.

## Common pitfalls

- Assuming every hosted model supports the same features
- Forgetting that the auth token is a ModelScope SDK Token, not a generic API key from another vendor
- Treating model ids like OpenAI model names instead of ModelScope-hosted identifiers

## Sources

- ModelScope API Inference intro: <https://modelscope.cn/docs/model-service/API-Inference/intro>
- ModelScope community announcement with API examples: <https://community.modelscope.cn/675262372db35d1195183bdb.html>
- ModelScope community update for API Inference examples: <https://community.modelscope.cn/67aac48359bcf8384ab5c5f8.html>
