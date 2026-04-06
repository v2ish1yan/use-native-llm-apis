# X-Code API Relay

## Summary

Use X-Code API when the project needs a coding-agent relay for Claude Code, Codex, or OpenCode. X-Code API is a managed relay platform, not a native model provider.

Treat it as a coding-tool relay with stronger public evidence for Codex than for the other client paths.

## Auth and Base URL

Public docs show a standard OpenAI-compatible Codex-style configuration:

- base URL: `https://x-code.cc/v1`
- API key supplied by the X-Code platform

For Codex, the public docs explicitly show:

- `wire_api = "responses"`
- `requires_openai_auth = true`
- `OPENAI_BASE_URL="https://x-code.cc/v1"`
- `OPENAI_API_KEY="your-api-key"`

## Primary access pattern

X-Code's docs are organized by tool:

- Claude Code
- Codex
- OpenCode

But the currently strongest publicly verified guide in this repo is the Codex configuration page.

That means the practical evidence today is:

- strong for Codex setup
- weaker for end-to-end protocol detail on the other tool paths

## Codex / Responses-oriented usage

The verified Codex configuration page documents:

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

## Tool-path caution

The docs home clearly shows Claude Code and OpenCode sections, but this repo has not yet captured enough public detail from those pages to promise protocol-level guidance equal to the Codex path.

So for now:

- Codex path is the best-supported route in this file
- Claude Code and OpenCode are confirmed as supported setup targets
- exact per-route protocol details should still be verified in the current docs before shipping

## Common pitfalls

- Treating X-Code like a native model vendor
- Assuming the same configuration text applies identically to every supported tool
- Assuming classic OpenAI chat-completions semantics when the verified Codex guide says `wire_api = "responses"`
- Forgetting to validate model support and endpoint compatibility for the exact client in use

## Sources

- X-Code docs home: <https://docs.x-code.cc/>
- X-Code Codex guide: <https://docs.x-code.cc/codex>
