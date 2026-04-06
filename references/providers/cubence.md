# Cubence Gateway

## Summary

Use Cubence when the project needs a hosted relay for coding-focused AI tools such as Claude Code, Codex, Gemini CLI, and related applications. Cubence is a gateway layer, not a native model vendor API.

Treat it as a tool-oriented relay with client-specific configuration surfaces.

## Auth and Base URL

Cubence public docs expose different bases by client family:

- Codex / OpenAI-style Responses: `https://api.cubence.com/v1`
- Claude Code: `https://api.cubence.com`
- Gemini CLI: `https://api-dmit.cubence.com`
- DROID custom model example: `https://api.cubence.com/droid`

Auth depends on the client:

- Codex: `OPENAI_API_KEY`
- Claude Code: `ANTHROPIC_AUTH_TOKEN`
- Gemini CLI: `GEMINI_API_KEY`

## Protocol families

Cubence publicly documents at least these client-facing families:

1. Codex using `wire_api = "responses"`
2. Claude Code using Anthropic-style base-url overrides
3. Gemini CLI using Gemini-style environment variables
4. DROID using Anthropic-style provider settings

That means the main question is which client or protocol family the project needs, not "what is the one Cubence schema."

## Codex / Responses-oriented usage

Cubence's Codex guide documents a concrete Codex configuration:

```toml
model_provider = "cubence"
model = "gpt-5"
model_reasoning_effort = "high"
disable_response_storage = true

[model_providers.cubence]
name = "cubence"
base_url = "https://api.cubence.com/v1"
wire_api = "responses"
requires_openai_auth = true
```

Auth file:

```json
{
  "OPENAI_API_KEY": "echo your-api-key-here"
}
```

Practical rule:

- for Codex-oriented integration, treat Cubence as a Responses-style relay
- parse output with Responses expectations, not classic chat-completions assumptions

## Claude Code usage

Cubence's Claude Code guide documents Anthropic-style environment overrides:

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "your-api-key-here",
    "ANTHROPIC_BASE_URL": "https://api.cubence.com",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1
  }
}
```

Practical rule:

- for Claude Code usage, keep Anthropic-style semantics in mind
- do not reuse Codex/OpenAI assumptions on the Claude route

## Gemini CLI usage

Cubence's Gemini CLI guide documents:

```dotenv
GOOGLE_GEMINI_BASE_URL=https://api-dmit.cubence.com
GEMINI_API_KEY=your-api-key-here
GEMINI_MODEL=gemini-3-pro-preview
```

That makes Cubence one of the clearer coding-tool relays for Gemini CLI setup.

## DROID note

The public DROID integration guide shows a custom model config with:

- `provider: "anthropic"`
- `base_url: "https://api.cubence.com/droid"`

This reinforces the idea that Cubence exposes multiple client-specific surfaces rather than one uniform HTTP contract.

## Streaming notes

Streaming behavior depends on the selected client path:

- Codex path -> Responses-style expectations
- Claude path -> Anthropic-style streaming expectations
- Gemini path -> Gemini CLI / Gemini-native expectations

Do not reuse one parser or one environment-variable scheme across all Cubence routes.

## Development guidance

When integrating Cubence:

1. choose the target client first
2. copy the exact Cubence base URL from that client's guide
3. configure the auth variables expected by that client
4. verify one minimal request or startup flow
5. only then add more advanced features

## Common pitfalls

- Assuming Cubence has one globally fixed endpoint shape for every tool
- Treating it like a native provider instead of an integration gateway
- Reusing Codex config on Claude Code or Gemini CLI without adjusting env vars and base URL
- Forgetting that some endpoint variants exist specifically for routing or client compatibility

## Sources

- Cubence docs root: <https://docs.cubence.com/>
- Cubence main site: <https://www.cubence.com/>
- Cubence quick start: <https://docs.cubence.com/en/docs/quick-start>
- Cubence Codex setup: <https://docs.cubence.com/en/docs/setup/codex>
- Cubence Claude Code setup: <https://docs.cubence.com/en/docs/setup/claude-code>
- Cubence Gemini CLI setup: <https://docs.cubence.com/en/docs/setup/gemini-cli>
- Cubence DROID integration: <https://docs.cubence.com/en/docs/setup/droid>
