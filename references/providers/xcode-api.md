# X-Code API Relay

## Summary

Use X-Code API when the project needs a coding-agent relay for Claude Code, Codex, or OpenCode. X-Code API is a managed relay platform, not a native model provider.

Treat it as a coding-tool relay with three publicly documented client paths.

## Auth and Base URLs

Public X-Code docs expose multiple client-facing bases:

- Claude Code: `https://x-code.cc`
- Codex: `https://x-code.cc/v1`
- OpenCode: `https://api-cn.x-code.cc/v1`

Auth depends on the client family:

- Claude Code: `ANTHROPIC_AUTH_TOKEN`
- Codex: `OPENAI_API_KEY`
- OpenCode: provider `apiKey` fields in `opencode.json`

## Protocol families

X-Code now has publicly verified setup guides for:

1. Claude Code using Anthropic-style base-url overrides
2. Codex using `wire_api = "responses"`
3. OpenCode using both Anthropic-style and OpenAI-style providers

That means X-Code is no longer just a Codex-only evidence point. It is a multi-client relay with different protocol expectations per route.

## Claude Code usage

The Claude Code guide documents:

```bash
export ANTHROPIC_BASE_URL="https://x-code.cc"
export ANTHROPIC_AUTH_TOKEN="your-api-key"
```

Practical rule:

- for Claude Code, keep Anthropic-style expectations
- do not reuse Codex/OpenAI assumptions on the Claude route

## Codex / Responses-oriented usage

The Codex guide documents:

```toml
model_provider = "xcode"
model = "gpt-5.2-codex"
model_reasoning_effort = "high"
disable_response_storage = true

[model_providers.xcode]
name = "xcode"
wire_api = "responses"
requires_openai_auth = true
base_url = "https://x-code.cc/v1"
```

Environment variables:

```bash
export OPENAI_BASE_URL="https://x-code.cc/v1"
export OPENAI_API_KEY="your-api-key"
```

Practical rule:

- for Codex-oriented integration, treat X-Code as a Responses-style relay
- use Responses expectations instead of classic chat-completions assumptions

## OpenCode usage

The OpenCode guide documents both Anthropic-style and OpenAI-style provider examples on X-Code:

Anthropic-family example:

```json
{
  "provider": {
    "xcodeapi": {
      "name": "X-Code API",
      "npm": "@ai-sdk/anthropic",
      "options": {
        "apiKey": "your-api-key",
        "baseURL": "https://api-cn.x-code.cc/v1"
      }
    }
  }
}
```

OpenAI-family example:

```json
{
  "provider": {
    "xcodeapi-openai": {
      "name": "X-Code API",
      "npm": "@ai-sdk/openai",
      "options": {
        "apiKey": "your-api-key",
        "baseURL": "https://api-cn.x-code.cc/v1"
      }
    }
  }
}
```

That makes OpenCode the clearest public proof that X-Code supports multiple protocol families, not one single OpenAI-like route.

## Streaming and parsing notes

Streaming and parsing should follow the selected client family:

- Claude Code path -> Anthropic-style expectations
- Codex path -> Responses-style expectations
- OpenCode with `@ai-sdk/anthropic` -> Anthropic-style expectations
- OpenCode with `@ai-sdk/openai` -> OpenAI-style expectations

Do not reuse one parser or one auth scheme across all X-Code routes.

## Development guidance

When integrating X-Code API:

1. choose the target client first
2. copy the exact base URL for that client family
3. configure the auth variables or provider fields expected by that client
4. verify one minimal startup flow or request path
5. only then add advanced features

## Common pitfalls

- Treating X-Code like a native model vendor
- Assuming one base URL applies identically to Claude Code, Codex, and OpenCode
- Assuming classic OpenAI chat-completions semantics when the verified Codex guide says `wire_api = "responses"`
- Forgetting that OpenCode can use both Anthropic-style and OpenAI-style providers on X-Code

## Sources

- X-Code docs home: <https://docs.x-code.cc/>
- X-Code Claude Code guide: <https://docs.x-code.cc/claude-code>
- X-Code Codex guide: <https://docs.x-code.cc/codex>
- X-Code OpenCode guide: <https://docs.x-code.cc/opencode>
