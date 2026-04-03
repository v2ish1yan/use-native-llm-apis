# PackyCode Gateway

## Summary

Use PackyCode when the project needs a managed multi-model gateway focused on coding tools such as Claude Code, Codex, Gemini CLI, and related developer workflows. PackyCode is a relay/gateway platform, not a native model vendor.

## Auth and Base URL

PackyCode's docs show multiple base URLs depending on the client and plan:

- general OpenAI-compatible examples: `https://www.packyapi.com/v1`
- some Codex-focused docs mention: `https://codex-api.packycode.com/v1`

Auth:

- provider-specific API token created in the Packy platform
- typically passed as a Bearer token or environment variable used by the configured client

## Primary access pattern

PackyCode is documented primarily through client setup guides rather than one generic provider API reference. The key idea is:

- choose the target client
- choose the model group
- use the PackyCode endpoint for that client

## Operational notes

PackyCode's docs explicitly organize usage by tool:

- Claude Code
- Codex
- Gemini CLI
- OpenCode

That means endpoint and model naming may differ slightly by tool path or account grouping.

## Common pitfalls

- Assuming one universal Packy base URL for every client
- Treating PackyCode as a native model provider instead of a relay layer
- Forgetting that model availability depends on the token group and plan

## Sources

- PackyAPI docs root: <https://docs.packyapi.com/>
- Packy CLI docs index: <https://docs.packyapi.com/docs/cli/>
- Packy Codex guide: <https://docs.packyapi.com/docs/cli/codex>
- Packy Claude guide: <https://docs.packyapi.com/docs/cli/claude>
