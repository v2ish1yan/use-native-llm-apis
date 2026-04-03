# Compshare / ModelVerse Gateway

## Summary

Use Compshare when the project needs a hosted multi-model API gateway with official OpenAI-compatible, Anthropic-compatible, and Gemini-compatible access paths. Compshare presents this capability through its ModelVerse API service rather than as a first-party model vendor.

## Auth and Base URL

Official OpenAI-compatible base URL:

- `https://api.modelverse.cn/v1`

Auth:

- `Authorization: Bearer {api_key}`

The official docs also describe additional protocol surfaces on the same platform, including:

- Anthropic-style `POST /v1/messages`
- Gemini-style `POST /v1beta/models/*`
- Responses-style `POST /v1/responses`

## Primary access pattern

For mainstream chat integrations, the official docs expose an OpenAI-compatible chat endpoint:

- `POST /v1/chat/completions`

Combined URL:

- `https://api.modelverse.cn/v1/chat/completions`

## Operational notes

Compshare's official docs describe the platform as a standardized model API service with:

- unified access to multiple model families
- support for text, image, audio, and video-related model APIs
- multiple compatibility layers, not just one OpenAI-style endpoint

This makes it useful as a relay layer when the application wants one account and one operational surface across several upstream model families.

## Protocol notes

- OpenAI-compatible chat is documented directly and includes streaming support.
- The OpenAPI expansion page also lists `POST /v1/responses`, so newer OpenAI-style Responses workflows may be possible on this platform.
- Anthropic Messages and Gemini-native style routes are listed as supported protocol entries, but you should still verify model-level capability before assuming every model is reachable through every protocol.

## Common pitfalls

- Treating Compshare as a native model provider instead of a managed gateway
- Assuming every upstream model supports every protocol listed by the platform
- Mixing OpenAI-compatible assumptions with platform-specific extension fields
- Forgetting that some extra fields only apply when using ModelVerse's own OpenAPI layer

## Sources

- Compshare docs root: <https://www.compshare.cn/docs>
- Compshare platform overview: <https://www.compshare.cn/docs/overview/platform/introduce>
- Compshare OpenAI-compatible chat docs: <https://www.compshare.cn/docs/modelverse/models/text_api/openai_compatible>
- Compshare OpenAPI extensions and protocol list: <https://www.compshare.cn/docs/modelverse/models/text_api/api-expand>
