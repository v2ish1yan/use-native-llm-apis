# X-Code API Relay

## Summary

Use X-Code API when the project needs a coding-agent relay for Claude Code, Codex, or OpenCode. X-Code API is a managed relay platform, not a native model provider.

## Auth and Base URL

Public docs show a standard OpenAI-compatible Codex-style configuration:

- base URL: `https://x-code.cc/v1`
- API key supplied by the X-Code platform

## Primary access pattern

X-Code's docs are organized by tool:

- Claude Code
- Codex
- OpenCode

This suggests the platform is integration-first rather than exposing one elaborate public provider API manual.

## Practical notes

The Codex configuration page is enough to confirm:

- OpenAI-compatible base URL shape
- environment-variable-based auth
- coding-assistant-focused usage

## Common pitfalls

- Treating X-Code like a native model vendor
- Assuming the same configuration text applies identically to every supported tool
- Forgetting to validate model support and endpoint compatibility for the exact client in use

## Sources

- X-Code docs home: <https://docs.x-code.cc/>
- X-Code Codex guide: <https://docs.x-code.cc/codex>
