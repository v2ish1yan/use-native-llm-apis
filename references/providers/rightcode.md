# Right Code Relay

## Summary

Use Right Code when the project needs a coding-tool-oriented relay for Codex, Claude, Gemini, and related agent workflows. Right Code is not a native model vendor API. It exposes multiple protocol surfaces behind one platform key.

Treat it as a relay layer with provider-specific routes.

## Auth and Base URL

Right Code's public curl docs show multiple route families:

- Codex / OpenAI-style Responses: `https://www.right.codes/codex/v1/responses`
- Codex / chat-completions compatibility: `https://www.right.codes/codex/v1/chat/completions`
- Claude-native style: `https://www.right.codes/claude/v1/messages`
- Gemini-native style: `https://right.codes/gemini/v1beta/models/{model}:streamGenerateContent?alt=sse`

Auth headers:

- Codex / OpenAI-style: `Authorization: Bearer $RIGHTCODE_API_KEY`
- Claude route: `x-api-key: $RIGHTCODE_API_KEY` or `Authorization`
- Gemini route: `x-goog-api-key: $RIGHTCODE_API_KEY`

## Protocol families

Right Code publicly demonstrates at least three protocol families:

1. OpenAI Responses
2. Anthropic Messages
3. Gemini `generateContent` / `streamGenerateContent`

That makes Right Code more than a thin "one endpoint" relay. The app still needs to choose the correct protocol family.

## Minimal Codex / Responses request

```bash
curl https://www.right.codes/codex/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $RIGHTCODE_API_KEY" \
  -d '{
    "model": "gpt-5.2",
    "input": [
      {
        "type": "message",
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "Hello"
          }
        ]
      }
    ],
    "stream": true
  }'
```

Common response fields:

- `id`
- `status`
- `output`
- `usage`

## Minimal Claude-style request

```bash
curl https://www.right.codes/claude/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $RIGHTCODE_API_KEY" \
  -d '{
    "model": "claude-sonnet-4-5-20250929",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Hello"
          }
        ]
      }
    ],
    "max_tokens": 32000,
    "stream": true
  }'
```

Text should be parsed with Anthropic-style content blocks, not OpenAI deltas.

## Minimal Gemini-style request

```bash
curl --location 'https://right.codes/gemini/v1beta/models/gemini-3-pro-preview:streamGenerateContent?alt=sse' \
  --header 'x-goog-api-key: '"$RIGHTCODE_API_KEY" \
  --header 'content-type: application/json' \
  --data '{
    "generationConfig": {
      "temperature": 1
    },
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Hello"
          }
        ]
      }
    ]
  }'
```

## Streaming notes

- Right Code publicly documents stream examples for all three protocol families
- the parser must match the selected route family
- do not reuse one parser across Codex, Claude, and Gemini routes

Practical rule:

- `/codex/v1/responses` -> Responses-style stream handling
- `/claude/v1/messages` -> Anthropic-style SSE lifecycle
- `/gemini/...:streamGenerateContent?alt=sse` -> Gemini stream handling

## Compatibility notes

Right Code also exposes:

- `/codex/v1/chat/completions`

But its own docs warn that this route is converted from `/v1/responses`, and some software or plugins may have compatibility issues.

One especially important note from the docs:

- system prompts sent to `/v1/chat/completions` may be replaced by Codex default instructions and become ineffective

So if the project can use Responses directly, prefer the Responses route.

## Tool-calling and structured-output notes

Tool-calling and structured-output behavior depend on the protocol family you choose:

- Codex route -> OpenAI / Responses-style expectations
- Claude route -> Anthropic-style expectations
- Gemini route -> Gemini-style expectations

Do not flatten these into one fake Right Code schema.

## Development guidance

When integrating Right Code:

1. choose the route family first
2. send one minimal request on that route
3. parse the response using that protocol's native semantics
4. only then add streaming, tools, or structured output

## Common pitfalls

- Treating Right Code as one uniform API instead of multiple protocol surfaces
- Using the Codex chat-completions compatibility route and assuming exact native OpenAI behavior
- Reusing the same auth header across Codex, Claude, and Gemini routes without checking the docs
- Parsing Claude or Gemini output with OpenAI-style code

## Sources

- Right Code docs home: <https://docs.right.codes/>
- Right Code intro: <https://docs.right.codes/docs/rc_quick_start/intro>
- Right Code curl examples: <https://docs.right.codes/docs/rc_extension/curl>
- Right Code OpenCode configuration: <https://docs.right.codes/docs/rc_extension/opencode>
