# GitHub Copilot / Copilot SDK

## Summary

Use this reference when the task involves GitHub Copilot, the Copilot SDK, or Copilot's BYOK model-provider integration. GitHub Copilot is not a plain model vendor endpoint in the same sense as OpenAI or Anthropic. It combines:

- Copilot subscription-backed auth
- GitHub OAuth and token flows
- Copilot SDK client behavior
- optional BYOK support for external model providers

## Auth modes

GitHub's official docs describe several authentication modes for Copilot SDK:

- signed-in GitHub user
- OAuth GitHub App user token
- HMAC key
- direct Copilot API token
- environment variable token chain
- BYOK for external providers

This is fundamentally different from a single API-key-only provider.

## Primary development usage

For Copilot SDK work, the main entry point is the GitHub Copilot SDK client, not a single public `/chat/completions` URL that all apps should call directly.

Typical JavaScript shape from the docs:

```ts
import { CopilotClient } from "@github/copilot-sdk";

const client = new CopilotClient();
```

Or with an explicit GitHub user token:

```ts
import { CopilotClient } from "@github/copilot-sdk";

const client = new CopilotClient({
  githubToken: userAccessToken,
  useLoggedInUser: false,
});
```

## BYOK notes

GitHub explicitly documents Bring Your Own Key for these provider categories:

- Anthropic
- AWS Bedrock
- Google AI Studio
- Microsoft Foundry
- OpenAI
- OpenAI-compatible providers
- xAI

This means Copilot can act as a consumer of your existing provider keys, not just as a GitHub-only hosted model surface.

## Operational notes

- Copilot auth is deeply tied to GitHub identity and subscription state
- BYOK changes the model-provider path without turning Copilot into a generic direct vendor endpoint
- model availability can differ between Copilot product surfaces and Codex integrations

## Common pitfalls

- Treating GitHub Copilot like a normal API-key-based provider
- Forgetting the distinction between GitHub auth and BYOK provider auth
- Assuming one fixed wire API for all Copilot scenarios

## Sources

- GitHub Docs: OpenAI Codex: <https://docs.github.com/en/copilot/concepts/agents/openai-codex>
- Copilot SDK authentication: <https://docs.github.com/en/copilot/how-tos/copilot-sdk/authenticate-copilot-sdk/authenticate-copilot-sdk>
- Copilot SDK BYOK: <https://docs.github.com/en/copilot/how-tos/copilot-sdk/authenticate-copilot-sdk/bring-your-own-key>
- Using your LLM provider API keys with Copilot: <https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/use-your-own-api-keys>
