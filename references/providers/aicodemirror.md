# AICodeMirror Relay

## Summary

Use AICodeMirror when the project needs a hosted relay for Claude Code, Codex, Gemini, and related coding-tool scenarios. AICodeMirror is a relay platform, not a native model vendor API.

Treat it as a setup-oriented relay with partially verified public evidence, not as a full protocol reference.

## What is publicly verified

From the public docs plus `cc-switch` presets, the following signals are real:

- AICodeMirror has public setup/tutorial docs
- the platform intentionally keeps a stable API domain
- public endpoint patterns exist for multiple coding clients
- supported client families include Claude Code, Codex, and Gemini

That is enough to say the platform is real and practically usable for setup. It is not enough to promise one fully documented wire protocol across every route.

## Auth and Base URL

`cc-switch` presets point to AICodeMirror endpoints such as:

- `https://api.aicodemirror.com/api/claudecode`
- `https://api.aicodemirror.com/api/codex/backend-api/codex`
- `https://api.aicodemirror.com/api/gemini`

Auth:

- AICodeMirror platform API key

Practical rule:

- choose the exact client path first
- do not assume one endpoint pattern covers every client family

## Primary access pattern

Public documentation is still tutorial-oriented rather than a consolidated API reference. The practical pattern is:

1. choose the target coding client
2. use the matching AICodeMirror endpoint path
3. authenticate with the platform-issued key
4. keep request and response handling aligned with that client's expected protocol

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

The public site explains that the stable domain is intentional so existing API integrations and configuration paths do not break when branding or platform details evolve.

That matters operationally because it suggests:

- endpoint continuity is part of the platform promise
- old integrations may keep working across branding or product changes

Useful operational signal, but still not equal to protocol-depth docs.

## Why this file is `partial`, not `usable`

This file is stronger than a bare skeleton because:

- public setup docs exist
- multiple client families are visible
- endpoint patterns are externally observable

This file is still not `usable` because:

- public docs are tutorial-heavy
- protocol-level request and response contracts are still thin
- there is not yet enough evidence here to promise reliable end-to-end code generation

## Common pitfalls

- Assuming one single endpoint path across Claude, Codex, and Gemini access
- Treating AICodeMirror as a native provider instead of a relay
- Assuming public tutorials imply a fully uniform vendor-independent feature set
- Over-trusting this file as an end-to-end protocol reference

## Sources

- AICodeMirror docs page: <https://www.aicodemirror.com/docs>
- AICodeMirror domain stability note: <https://www.aicodemirror.com/why-aicodemirror>
