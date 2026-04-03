# AICodeMirror Relay

## Summary

Use AICodeMirror when the project needs a hosted relay for Claude Code, Codex, Gemini, and related coding-tool scenarios. AICodeMirror is a relay platform, not a native model vendor API.

## Auth and Base URL

`cc-switch` presets point to AICodeMirror endpoints such as:

- `https://api.aicodemirror.com/api/claudecode`
- `https://api.aicodemirror.com/api/codex/backend-api/codex`
- `https://api.aicodemirror.com/api/gemini`

Auth:

- AICodeMirror platform API key

## Primary access pattern

Public documentation is tutorial-oriented rather than one consolidated API reference. The practical pattern is:

- choose the target coding client
- use the corresponding AICodeMirror endpoint path
- authenticate with the platform-issued key

## Operational notes

The public site also explains that the stable domain is intentional so existing API integrations and configuration paths do not break when branding or platform details evolve.

## Common pitfalls

- Assuming one single endpoint path across Claude, Codex, and Gemini access
- Treating AICodeMirror as a native provider instead of a relay
- Assuming public tutorials imply a fully uniform vendor-independent feature set

## Sources

- AICodeMirror docs page: <https://www.aicodemirror.com/docs>
- AICodeMirror domain stability note: <https://www.aicodemirror.com/why-aicodemirror>
