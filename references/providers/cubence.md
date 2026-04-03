# Cubence Gateway

## Summary

Use Cubence when the project needs a hosted relay for coding-focused AI tools such as Claude Code, Codex, Gemini CLI, and related applications. Cubence is a gateway layer, not a native model vendor API.

## Auth and Base URL

Cubence public docs and site emphasize:

- API key created on the Cubence platform
- OpenAI- or client-compatible configuration using a Cubence endpoint

Common base URL from `cc-switch` presets:

- `https://api.cubence.com/v1`

Alternate endpoints may also be available for routing and resilience.

## Primary access pattern

Cubence's documentation is organized around tool setup rather than one model-wire reference:

- configure the target client
- insert the Cubence API key
- point the client at the Cubence endpoint

## Operational notes

The public site describes Cubence as an AI API gateway with monitoring, flexible pricing, and support for multiple coding tools. Treat it as an operational gateway rather than a native provider surface.

## Common pitfalls

- Assuming Cubence has one globally fixed endpoint shape for every tool
- Treating it like a native provider instead of an integration gateway
- Forgetting that some endpoint variants may exist for routing or failover

## Sources

- Cubence docs root: <https://docs.cubence.com/>
- Cubence main site: <https://www.cubence.com/>
