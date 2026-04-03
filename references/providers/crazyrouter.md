# CrazyRouter Gateway

## Summary

Use CrazyRouter when the goal is to access a large multi-model catalog through one OpenAI-compatible API. CrazyRouter positions itself as a unified API gateway rather than a native model provider.

## Auth and Base URL

Public site guidance indicates an OpenAI-compatible base URL:

- `https://crazyrouter.com/v1`

Auth:

- CrazyRouter API key

## Primary access pattern

CrazyRouter is documented as:

- one API
- many models
- OpenAI-compatible request format

That makes it appropriate for projects that want to swap model names without changing the client implementation.

## Operational notes

Public-facing guidance emphasizes:

- broad multi-model coverage
- OpenAI-compatible API format
- support for text, image, video, and audio model families

Because this is a gateway, model capability and pricing are platform-managed rather than guaranteed by one vendor-native contract.

## Common pitfalls

- Assuming upstream vendor-native behavior is preserved perfectly
- Treating CrazyRouter as if it were a first-party model provider
- Relying on marketing claims without testing the exact model and modality you need

## Sources

- CrazyRouter main site: <https://crazyrouter.com/>
- CrazyRouter pricing/API compatibility explanation: <https://crazyrouter.com/tools/pricing-calculator>
