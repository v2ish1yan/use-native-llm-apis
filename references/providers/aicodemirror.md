# AICodeMirror Relay

## Summary

Use AICodeMirror when the project needs a hosted relay for Claude Code, Codex, Gemini, and related coding-tool scenarios. AICodeMirror is a relay platform, not a native model vendor API.

Treat it as a tool-specific relay with tutorial-heavy public docs.

## Auth and Base URL

`cc-switch` presets point to AICodeMirror endpoints such as:

- `https://api.aicodemirror.com/api/claudecode`
- `https://api.aicodemirror.com/api/codex/backend-api/codex`
- `https://api.aicodemirror.com/api/gemini`

Auth:

- AICodeMirror platform API key

## Primary access pattern

Public documentation is still tutorial-oriented rather than a consolidated API reference. The practical pattern is:

1. choose the target coding client
2. use the matching AICodeMirror endpoint path
3. authenticate with the platform-issued key

Supported client families visible in public materials:

- Claude Code
- Codex
- Gemini

## Practical guidance

Because the public docs are not a full protocol reference, treat AICodeMirror as a setup-oriented relay:

- use it when the project already knows which client path it needs
- verify request and response semantics against the client's expected protocol
- do not assume one uniform body shape across every AICodeMirror endpoint

## Operational notes

The public site also explains that the stable domain is intentional so existing API integrations and configuration paths do not break when branding or platform details evolve.

That makes the platform operationally useful, but it does not by itself prove that every endpoint family has equally rich public API docs.

## Common pitfalls

- Assuming one single endpoint path across Claude, Codex, and Gemini access
- Treating AICodeMirror as a native provider instead of a relay
- Assuming public tutorials imply a fully uniform vendor-independent feature set
- Over-trusting this file as an end-to-end protocol reference; the public docs are still thinner than the stronger relay entries in this repo

## Sources

- AICodeMirror docs page: <https://www.aicodemirror.com/docs>
- AICodeMirror domain stability note: <https://www.aicodemirror.com/why-aicodemirror>
