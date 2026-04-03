# Ai Go Code Relay

## Summary

Use Ai Go Code when the project needs a managed relay for coding-oriented tools such as Codex, Claude Code, Gemini CLI, and OpenCode. Ai Go Code is a hosted relay and configuration platform, not a native model vendor.

## Auth and Base URLs

Ai Go Code's public docs organize usage by client and model family.

Documented endpoint patterns include:

- OpenAI-compatible families: `https://api.aigocode.com/v1`
- Gemini-family setup examples: `https://api.aigocode.com/v1beta`

Auth:

- Ai Go Code API key from the platform console

## Primary access pattern

Ai Go Code's docs are integration-first:

- choose the client
- choose the model family
- use the matching endpoint suffix

This means the same platform may expose slightly different base URLs for different SDK families.

## Operational notes

The public docs explicitly describe:

- Codex configuration
- OpenCode configuration
- Claude and Gemini tool setup

That makes Ai Go Code more of a developer relay platform than a single protocol surface.

## Common pitfalls

- Using `/v1` for Gemini when the docs require `/v1beta`
- Treating Ai Go Code as a native provider instead of a relay
- Assuming one endpoint suffix works for every client family

## Sources

- Ai Go Code docs center: <https://www.aigocode.com/docs>
- Ai Go Code Codex guide: <https://www.aigocode.com/docs/getting-started/codex>
- Ai Go Code OpenCode guide: <https://www.aigocode.com/docs/advanced/opencode>
