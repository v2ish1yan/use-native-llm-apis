# NewAPI Gateway

## Summary

Use NewAPI when the project needs a self-hosted or managed multi-provider gateway rather than a single vendor API. NewAPI is not a model provider by itself; it is an API management and routing layer that can expose OpenAI-compatible behavior across many upstream providers and tools.

## Auth and Base URL

Base URL depends on the deployment:

- self-hosted service URL
- managed NewAPI service URL

Auth:

- token generated in the NewAPI console

## Primary access pattern

NewAPI is best treated as a gateway abstraction:

- one API address
- one token format
- many upstream providers and models

The exact runtime endpoints depend on how the NewAPI deployment is configured.

## Development usage

For app integration, the main client-side concerns are usually:

- API address
- token
- model name

This is why `cc-switch` treats NewAPI as a universal provider and why the docs focus on supported app integrations rather than one single model-wire spec.

## Common pitfalls

- Treating NewAPI as if it were one vendor's native API
- Forgetting that capability depends on upstream provider configuration
- Assuming one deployment's enabled models and routes exist on another deployment

## Sources

- NewAPI docs root: <https://docs.newapi.pro/en/>
- NewAPI quick start: <https://docs.newapi.pro/zh/docs>
- NewAPI supported app integrations: <https://docs.newapi.pro/en/docs/apps>
