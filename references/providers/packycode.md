# PackyCode Gateway

## Summary

Use PackyCode when the project needs a managed multi-model gateway focused on coding tools such as Claude Code, Codex, Gemini CLI, and related developer workflows. PackyCode is a relay and gateway platform, not a native model vendor.

Treat it as a coding-tool relay with client-specific routes.

## Auth and Base URL

PackyCode docs show multiple bases depending on the client and plan:

- general OpenAI-compatible examples: `https://www.packyapi.com/v1`
- Codex-focused docs: `https://codex-api.packycode.com/v1`

Auth:

- PackyCode platform API key
- typically sent as `Authorization: Bearer $PACKYCODE_API_KEY`

The docs are organized around client setup rather than one unified API reference, so the exact base URL should be taken from the target client guide.

## Primary access pattern

PackyCode is best thought of as a client-oriented relay:

1. choose the target client
2. use the PackyCode endpoint recommended for that client
3. authenticate with the PackyCode-issued key
4. keep the request shape aligned with the selected protocol family

The public docs explicitly organize usage by tool:

- Claude Code
- Codex
- Gemini CLI
- OpenCode

## Codex / OpenAI-style usage

The Codex setup guide indicates a Codex-facing API base such as:

- `https://codex-api.packycode.com/v1`

For OpenAI-style or Codex-facing requests, a practical minimal pattern is:

```bash
curl https://codex-api.packycode.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $PACKYCODE_API_KEY" \
  -d '{
    "model": "gpt-4.1",
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

If the target client is Codex and the deployment expects Responses-style traffic instead of classic chat-completions, follow the Codex-specific Packy guide rather than assuming one universal OpenAI surface.

## Claude-oriented usage

PackyCode provides a Claude-specific setup path in its public docs.

Practical rule:

- if the app or tool is Claude Code oriented, use the Claude-specific Packy configuration flow
- keep Anthropic-style expectations for request and response semantics where the client expects them

That means you should not assume the Claude-facing Packy flow behaves exactly like an OpenAI-compatible route.

## Gemini and OpenCode notes

PackyCode also documents Gemini CLI and OpenCode setup.

This is a strong signal that PackyCode is a multi-client relay, not one single stable protocol surface. The right integration path depends on which coding client the project is actually using.

## Streaming notes

Streaming support depends on the selected client route and protocol family:

- OpenAI-style route -> OpenAI-style chunk parsing
- Claude-oriented route -> Anthropic-style streaming expectations when applicable
- Gemini-oriented route -> Gemini-style client behavior

Do not assume one stream parser works for every PackyCode client path.

## Development guidance

When integrating PackyCode:

1. choose the target client first
2. copy the exact PackyCode base URL from that client's setup guide
3. send one minimal request on that route
4. parse output using the protocol family that client expects
5. only then add streaming, tools, or structured output

## Common pitfalls

- Assuming one universal PackyCode base URL for every client
- Treating PackyCode as a native model provider instead of a relay layer
- Reusing one request parser across Codex, Claude, Gemini CLI, and OpenCode
- Forgetting that model availability depends on the token group, plan, and selected client path

## Sources

- PackyAPI docs root: <https://docs.packyapi.com/>
- Packy CLI docs index: <https://docs.packyapi.com/docs/cli/>
- Packy Codex guide: <https://docs.packyapi.com/docs/cli/codex>
- Packy Claude guide: <https://docs.packyapi.com/docs/cli/claude>
- Packy Gemini guide: <https://docs.packyapi.com/docs/cli/gemini>
- Packy OpenCode guide: <https://docs.packyapi.com/docs/cli/opencode>
