# CTok.ai Gateway

## Summary

Use CTok.ai when the project needs a hosted AI API gateway rather than a first-party model vendor. The public CTok.ai web app exposes an API front door and related endpoint configuration, but its detailed docs are currently less openly crawlable than some other relay platforms.

## Auth and Base URL

Public site configuration exposes:

- `https://api.ctok.ai`

Public API behavior confirms that `GET /v1/models` exists and requires an API key.

Verified unauthenticated error text shows the platform accepts API keys through:

- `Authorization: Bearer ...`
- `x-api-key`
- `x-goog-api-key`

## Primary access pattern

Conservative public conclusion:

- CTok.ai exposes a `/v1` API surface
- `GET /v1/models` is a real endpoint
- the platform positions itself as an AI API gateway, not a native model vendor

Because the detailed protocol docs are not fully accessible from a static crawl today, verify the exact wire shape you need from the current console or docs before assuming full OpenAI, Gemini, or Anthropic parity.

## Operational notes

The public `api.ctok.ai` app configuration also exposes custom endpoints such as:

- `https://imds.ai`
- `https://subcs.ctokai.com`

Treat those as platform-managed routing variants rather than as proof that every endpoint is interchangeable for every client.

## Common pitfalls

- Assuming CTok.ai is a first-party model provider
- Assuming the whole API contract from the existence of `/v1/models` alone
- Hard-coding one endpoint without checking the current platform configuration
- Treating alternate routing domains as guaranteed drop-in replacements

## Sources

- CTok.ai main site: <https://ctok.ai/>
- CTok.ai API app root: <https://api.ctok.ai/>
- Verified unauthenticated model-list endpoint: <https://api.ctok.ai/v1/models>
- CTok.ai docs domain: <https://docs.ctok.ai/>
