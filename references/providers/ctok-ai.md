# CTok.ai Gateway

## Summary

Use CTok.ai when the project needs a hosted AI API gateway rather than a first-party model vendor. CTok.ai appears to expose a real `/v1` API surface, but its detailed protocol docs are still less openly accessible than the stronger relay entries in this repo.

Treat it as a partially verified gateway, not as a fully documented provider reference.

## What is publicly verified

The following signals are publicly verified:

- the main platform site exists
- `https://api.ctok.ai` is a real API front door
- `GET /v1/models` is a real endpoint
- the unauthenticated response indicates several accepted auth styles
- CTok.ai positions itself as an API gateway rather than a first-party model vendor

That is enough to justify a `partial` file. It is not enough to promise reliable end-to-end coding guidance.

## Auth and Base URL

Public site configuration exposes:

- `https://api.ctok.ai`

Public API behavior confirms that `GET /v1/models` exists and requires an API key.

Verified unauthenticated error text shows the platform accepts API keys through:

- `Authorization: Bearer ...`
- `x-api-key`
- `x-goog-api-key`

Practical rule:

- start with `Authorization: Bearer $CTOK_API_KEY`
- if a client expects another header style, verify it against the current platform docs or console first

## Primary access pattern

Conservative public conclusion:

- CTok.ai exposes a `/v1` API surface
- `GET /v1/models` is a real endpoint
- the platform behaves like an API gateway, not a native model vendor

Because the detailed protocol docs are not fully accessible from public crawlable pages today, you should verify the exact wire shape you need from the current console or docs before assuming full OpenAI, Gemini, or Anthropic parity.

## Operational notes

The public `api.ctok.ai` app configuration also exposes custom endpoints such as:

- `https://imds.ai`
- `https://subcs.ctokai.com`

Treat those as platform-managed routing variants rather than as proof that every endpoint is interchangeable for every client.

## Why this file is `partial`, not `usable`

This file is stronger than a skeleton because:

- the API root is real
- `/v1/models` is verified
- accepted auth header styles are externally observable

This file is still not `usable` because:

- protocol-level request and response docs are still too limited
- public evidence is not yet strong enough to promise a stable OpenAI-, Anthropic-, or Gemini-compatible contract
- there is not yet enough verified detail here to support end-to-end code generation confidently

## Common pitfalls

- Assuming CTok.ai is a first-party model provider
- Assuming the whole API contract from the existence of `/v1/models` alone
- Hard-coding one endpoint without checking the current platform configuration
- Treating alternate routing domains as guaranteed drop-in replacements
- Upgrading this file mentally from `partial` to `usable` without stronger public docs

## Sources

- CTok.ai main site: <https://ctok.ai/>
- CTok.ai API app root: <https://api.ctok.ai/>
- Verified unauthenticated model-list endpoint: <https://api.ctok.ai/v1/models>
- CTok.ai docs domain: <https://docs.ctok.ai/>
