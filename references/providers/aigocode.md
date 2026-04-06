# Ai Go Code Relay

## Summary

Use Ai Go Code when the project needs a managed relay for coding-oriented tools such as Codex, Claude Code, Gemini CLI, and OpenCode. Ai Go Code is a hosted relay and configuration platform, not a native model vendor.

Treat it as a multi-client relay with protocol-specific base URLs.

## Auth and Base URLs

Ai Go Code public docs expose different endpoint families by client and model family:

- OpenAI / Codex family: `https://api.aigocode.com`
- Anthropic / Claude family: `https://api.aigocode.com/v1`
- Gemini family: `https://api.aigocode.com/v1beta`

Auth:

- Ai Go Code API key from the platform console

The public OpenCode guide also makes an important point:

- Claude and GPT families use `/v1`
- Gemini families use `/v1beta`

Do not assume one suffix works for every client family.

## Protocol families

Ai Go Code publicly documents at least these client-facing families:

1. Codex using OpenAI-compatible auth and Responses-style wiring
2. Claude Code using Anthropic-style base-url overrides
3. OpenCode using Anthropic, OpenAI, and Gemini providers in one config
4. Gemini CLI using Gemini-style base URL and API key expectations

That means the key integration choice is the target client or protocol family, not one universal Ai Go Code request body.

## Codex / OpenAI-style usage

The Codex setup guide documents a concrete Codex configuration:

```toml
model_provider = "aigocode"
model = "gpt-5.3-codex"
model_reasoning_effort = "high"
disable_response_storage = true
preferred_auth_method = "apikey"

[model_providers.aigocode]
name = "aigocode"
base_url = "https://api.aigocode.com"
wire_api = "responses"
requires_openai_auth = true
```

Auth file:

```json
{
  "OPENAI_API_KEY": "YOUR_API_KEY"
}
```

Practical rule:

- for Codex-oriented integration, treat Ai Go Code as a Responses-style relay
- use Responses semantics, not classic chat-completions assumptions, unless the client explicitly uses chat-completions

## OpenCode usage

The OpenCode guide is the clearest public multi-provider document in the Ai Go Code docs.

It explicitly documents:

- Anthropic provider -> `baseURL: https://api.aigocode.com/v1`
- OpenAI provider -> `baseURL: https://api.aigocode.com/v1`
- Gemini provider -> `baseURL: https://api.aigocode.com/v1beta`

It also requires using the matching native SDK family:

- Anthropic -> `@ai-sdk/anthropic`
- OpenAI -> OpenCode built-in OpenAI provider
- Gemini -> `@ai-sdk/google`

That makes OpenCode a strong reference for Ai Go Code's protocol split.

## Claude Code and Gemini CLI notes

The docs home explicitly lists:

- Claude Code configuration
- Gemini CLI configuration

Practical rule:

- for Claude Code, keep Anthropic-style expectations
- for Gemini CLI, keep Gemini-native expectations
- do not reuse Codex/OpenAI assumptions on those client paths

## Streaming notes

Streaming behavior depends on the chosen client family:

- Codex path -> Responses-style expectations
- Claude path -> Anthropic-style streaming expectations
- Gemini path -> Gemini-native streaming expectations

Do not reuse one parser or one config pattern across all Ai Go Code routes.

## Development guidance

When integrating Ai Go Code:

1. choose the target client first
2. copy the exact base URL for that client family
3. configure the auth variable expected by that client
4. verify one minimal request or startup flow
5. only then add advanced features

## Common pitfalls

- Using `/v1` for Gemini when the docs require `/v1beta`
- Treating Ai Go Code as a native provider instead of a relay
- Assuming one endpoint suffix works for every client family
- Reusing one parser or provider SDK across Codex, Claude Code, Gemini CLI, and OpenCode

## Sources

- Ai Go Code docs center: <https://www.aigocode.com/docs>
- Ai Go Code Codex guide: <https://www.aigocode.com/docs/getting-started/codex>
- Ai Go Code OpenCode guide: <https://www.aigocode.com/docs/advanced/opencode>
