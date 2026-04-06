# CrazyRouter Gateway

## Summary

Use CrazyRouter when the goal is to access a large multi-model catalog through one gateway. CrazyRouter positions itself as a unified AI API platform rather than a native model provider.

Treat it as a multi-protocol gateway with strong OpenAI-compatible access and broader platform-specific capability beyond chat.

## Auth and Base URL

OpenAI-compatible base URL:

- `https://crazyrouter.com/v1`

Auth:

- `Authorization: Bearer $CRAZYROUTER_API_KEY`

Required headers in the public request guide:

- `Authorization`
- `Content-Type: application/json`

## Supported API families

CrazyRouter publicly advertises support for:

- OpenAI-compatible access
- Anthropic-compatible access
- Gemini-compatible access
- image generation
- video generation
- audio processing
- embeddings
- reranking

The public quick-start and request docs are strongest for the OpenAI-compatible surface.

## Minimal OpenAI-style chat request

```bash
curl https://crazyrouter.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CRAZYROUTER_API_KEY" \
  -d '{
    "model": "gpt-5.2",
    "messages": [
      {
        "role": "user",
        "content": "Hello, how are you?"
      }
    ],
    "temperature": 0.7
  }'
```

Typical response field for text:

- `choices[0].message.content`

## Streaming notes

CrazyRouter's request guide documents SSE streaming on the OpenAI-compatible chat route:

- set `"stream": true`
- stream format uses `data: ...`
- stream ends with `data: [DONE]`

That means OpenAI-style chunk parsing is appropriate for the main `/v1/chat/completions` surface.

## Model and modality notes

CrazyRouter publicly lists support for 300+ models and multiple modalities:

- chat models
- image generation
- video generation
- audio processing
- embeddings
- reranking

Practical rule:

- do not assume every model supports every modality
- confirm the route and model together before coding

## Integration guidance

When integrating CrazyRouter:

1. start with the OpenAI-compatible surface unless the target app explicitly needs another protocol family
2. send one minimal chat request
3. verify model name and output parsing
4. add streaming only after the base request works
5. verify modality-specific routes separately for images, video, audio, embeddings, or reranking

## Compatibility notes

CrazyRouter's public materials strongly market OpenAI compatibility. That is useful for fast migrations, but you should still avoid assuming perfect upstream-native parity for Anthropic or Gemini behavior without testing the exact route you need.

So for non-OpenAI protocol work:

- prefer explicit CrazyRouter docs if available
- otherwise treat the gateway as partial guidance and test the route directly

## Common pitfalls

- Assuming upstream vendor-native behavior is preserved perfectly
- Treating CrazyRouter as if it were a first-party model provider
- Reusing one assumption across chat, image, video, audio, and embeddings routes
- Relying on a marketing claim before verifying the exact model and modality combination you need

## Sources

- CrazyRouter docs root: <https://docs.crazyrouter.com/>
- CrazyRouter introduction: <https://docs.crazyrouter.com/introduction>
- CrazyRouter request guide: <https://docs.crazyrouter.com/en/making-requests>
- CrazyRouter quick-start guide: <https://crazyrouter.com/zh/blog/crazyrouter-api-quickstart>
