# Doubao / Volcengine Ark API

## Summary

Use Volcengine Ark when integrating Doubao-family models or other foundation models through Volcengine's official platform. Ark is slightly more complex than some other providers because the platform exposes both:

- OpenAI-compatible access for easier migration
- Ark-native platform concepts such as endpoint management and Responses-based workflows

For application development, treat it as an official provider with dual entry styles.

## Auth and Base URL

For runtime model calls, Volcengine's public docs show API-key-based access through Ark runtime endpoints such as:

- `https://ark.cn-beijing.volces.com/api/v3`

Auth header:

- `Authorization: Bearer $ARK_API_KEY`

Content type:

- `application/json`

Regional and deployment-specific endpoint IDs matter in Ark. The platform commonly expects you to create or use a healthy inference endpoint first, then call models through that environment.

## Primary generation endpoints

Two important access patterns are visible in current public docs:

- Responses-style:
  - `POST /responses`
- OpenAI-compatible chat style through compatible SDK usage and examples

Combined runtime base:

- `https://ark.cn-beijing.volces.com/api/v3`

## Minimal request

Responses-style example:

```bash
curl https://ark.cn-beijing.volces.com/api/v3/responses \
  -H "Authorization: Bearer $ARK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seed-1-6-251015",
    "input": "hello"
  }'
```

This public example matters because it shows Ark is not only an OpenAI-chat-compatible surface; it also exposes a Responses-style entry.

## Response shape

Response shape depends on which runtime entry you use:

- Responses API returns a Responses-style structure
- Compatible chat access returns an OpenAI-like `choices` response

That means your client code should not assume one single response envelope for all Ark integrations.

## Streaming notes

Volcengine's public compatibility notes indicate OpenAI-compatible SDK usage is supported. For streaming behavior:

- verify whether your chosen access mode is Responses-based or chat-compatible
- parse SSE accordingly
- do not mix OpenAI chat delta assumptions into a Responses flow

## Tool-calling notes

Ark's public docs show Responses-based tool usage for features such as web search. For classic function-calling style, behavior can differ depending on whether you are using:

- OpenAI-compatible access
- Responses-based access
- platform-specific plugin or app tooling

When building tool integrations, choose one runtime style first and keep the client code aligned with that style.

## Structured-output notes

Because Ark exposes a Responses-style path and OpenAI-compatible access, structured-output strategy should match the chosen runtime:

- Responses-style integrations should follow the Responses-shaped constraints and output parsing
- compatible chat flows should follow the compatible mode used by the chosen SDK or endpoint

Do not assume that every Ark deployment supports the exact same structured-output surface without checking the current model and endpoint capabilities.

## Multimodal notes

Ark supports a broad set of model families and applications. Multimodal support is endpoint-specific and model-specific. Do not generalize from one Doubao endpoint to all Ark endpoints.

## Endpoint notes

Ark is strongly endpoint-oriented:

- create or identify an endpoint
- wait until it is healthy
- use the correct endpoint/runtime base

This makes it different from providers where a single global API base is enough for most tasks.

## Common pitfalls

- Treating Ark as only an OpenAI-compatible relay and ignoring the Responses-style runtime
- Assuming one response envelope across all Ark access modes
- Forgetting that endpoint state and deployment mode affect what can be called
- Mixing plugin/app tool docs with plain model-runtime docs
- Hard-coding one region or one endpoint style for all future use

## Sources

- Volcengine Ark docs root: <https://www.volcengine.com/docs/82379>
- SDK install and compatibility note: <https://www.volcengine.com/docs/82379/1541595>
- Regular online inference example: <https://www.volcengine.com/docs/82379/2121998>
- Responses API example and query docs: <https://www.volcengine.com/docs/82379/1783709>
- Web search with Responses API: <https://www.volcengine.com/docs/82379/1338552>
- Endpoint management overview: <https://www.volcengine.com/docs/82379/1182403>
