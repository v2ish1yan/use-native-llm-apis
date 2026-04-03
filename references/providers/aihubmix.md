# AiHubMix Gateway

## Summary

Use AiHubMix when you want one hosted gateway that normalizes access to multiple upstream providers such as OpenAI, Claude, Gemini, DeepSeek, and Qwen. AiHubMix is not a native model vendor; it is an official aggregation platform with a strong OpenAI-compatible development story and additional compatibility layers for Anthropic and Gemini.

## Auth and Base URL

Primary base URL patterns documented by AiHubMix:

- `https://aihubmix.com`
- `https://aihubmix.com/v1`
- `https://aihubmix.com/v1/chat/completions`

Alternate server:

- `https://api.aihubmix.com`

Auth header:

- `Authorization: Bearer $AIHUBMIX_API_KEY`

## Primary access pattern

AiHubMix's docs explicitly position OpenAI compatibility as the main development path:

- replace `https://api.openai.com` with `https://aihubmix.com`
- keep standard OpenAI-compatible client code

AiHubMix also documents:

- Claude compatibility (beta)
- Gemini native interface

## Minimal request

```bash
curl https://aihubmix.com/v1/chat/completions \
  -H "Authorization: Bearer $AIHUBMIX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5",
    "messages": [
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

## Response shape

For standard OpenAI-compatible calls, response shape is OpenAI-like chat completions. Other compatibility layers follow the conventions of the chosen interface.

## Compatibility notes

AiHubMix officially advertises support for:

- OpenAI-compatible requests
- Anthropic-compatible requests
- Gemini native interface

This makes it closer to a multi-protocol gateway than a single-format relay.

## Operational notes

- AiHubMix documents both primary and alternate server addresses for redundancy
- endpoint format can vary by client, so docs explicitly mention that some apps may need `/v1` or `/v1/chat/completions`

## Common pitfalls

- Treating AiHubMix as a native model provider instead of a gateway
- Assuming all upstream vendor-specific behaviors survive full normalization
- Forgetting to test both primary and alternate endpoints when reliability matters

## Sources

- AiHubMix docs root: <https://docs.aihubmix.com/en>
- AiHubMix intro and base URL notes: <https://docs.aihubmix.com/en/index>
- AiHubMix integration guide: <https://docs.aihubmix.com/en/api/Aihubmix-Integration>
