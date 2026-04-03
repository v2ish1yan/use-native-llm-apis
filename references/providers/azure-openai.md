# Azure OpenAI

## Summary

Use Azure OpenAI when the deployment runs through Microsoft Azure or Azure AI Foundry. Azure OpenAI now exposes a v1 API that is intentionally close to OpenAI's current API shape, but it still differs in operational details such as:

- resource-specific base URLs
- deployment names instead of raw model names
- Azure authentication and regional availability

## Auth and Base URL

Base URL pattern:

- `https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/`

Auth options:

- API key: `AZURE_OPENAI_API_KEY`
- Microsoft Entra ID for enterprise environments

## Primary generation endpoint

- Responses API through the Azure OpenAI v1 surface

Typical client setup:

- base URL points to `/openai/v1/`
- model argument usually uses the deployment name

## Minimal request

```bash
curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "YOUR_DEPLOYMENT_NAME",
    "input": "Write a one-line hello in Python."
  }'
```

## Response shape

Azure OpenAI v1 Responses is intentionally aligned with OpenAI Responses, but Azure's docs note that response objects can evolve over time. Parse only the fields your app actually needs.

## Streaming notes

- Responses API supports streaming
- keep your parser aligned with the Responses event model, not legacy chat deltas

## Tool-calling notes

When tool use is supported for the chosen deployment and region, follow the Responses-style tool model. The main Azure-specific concern is deployment support, not a radically different tool schema.

## Structured-output notes

Azure OpenAI's Responses API is the right baseline for modern structured output on Azure. The big Azure-specific rule is to use deployed model names and verify region support for the feature set you need.

## Common pitfalls

- Passing a raw OpenAI model id instead of an Azure deployment name
- Forgetting the `/openai/v1/` base path
- Mixing legacy preview-version examples with the current v1 API
- Assuming all regions support the same latest Responses features

## Sources

- Azure Responses API how-to: <https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/work-with-code>
- Azure v1 API lifecycle: <https://learn.microsoft.com/en-us/azure/foundry/openai/api-version-lifecycle>
- Switching endpoints guide: <https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/switching-endpoints>
- Azure v1 REST reference: <https://learn.microsoft.com/en-us/azure/ai-foundry/openai/latest>
