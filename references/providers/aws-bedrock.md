# AWS Bedrock

## Summary

Use AWS Bedrock when the target environment runs Claude or other foundation models through AWS-managed infrastructure. For Anthropic models specifically, Bedrock supports Anthropic's Messages API semantics while invoking them through AWS runtime operations.

## Auth and Base URL

Bedrock is not a simple single API-key REST host. Typical auth uses:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`

Runtime host pattern:

- `https://bedrock-runtime.${AWS_REGION}.amazonaws.com`

## Primary access pattern

For Anthropic Claude on Bedrock, the important public pattern is:

- Anthropic Claude Messages API semantics
- invoked through Bedrock runtime operations such as `InvokeModel` or `InvokeModelWithResponseStream`

AWS also recommends the Converse API for a more unified messages experience across model providers.

## Minimal request shape

Anthropic Claude Messages on Bedrock uses fields such as:

```json
{
  "anthropic_version": "bedrock-2023-05-31",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": "Write a one-line hello in Python."
    }
  ]
}
```

## Response shape

Response shape depends on whether you use:

- Bedrock base inference operations
- Bedrock streaming inference operations
- Converse or ConverseStream

For Anthropic-model payloads, the message content structure remains Anthropic-like.

## Streaming notes

Use `InvokeModelWithResponseStream` or `ConverseStream` when streaming is required. Keep in mind that Bedrock transport and SDK handling differ from a plain vendor-hosted SSE endpoint even when the payload semantics are Anthropic-like.

## Tool-calling notes

AWS documents tool use under the Anthropic Claude Messages API section. Treat the message semantics as Anthropic-style, but the invocation layer remains AWS Bedrock, not Anthropic's direct public endpoint.

## Structured-output notes

AWS documents validated JSON output for Anthropic Claude Messages on Bedrock. If you need strong machine-readable output, use the Bedrock-specific guidance for the chosen Claude model and runtime operation.

## Multimodal notes

AWS explicitly documents multimodal prompts for Claude Messages on Bedrock using content arrays with image and text blocks.

## Common pitfalls

- Assuming Bedrock is just a drop-in direct Anthropic HTTPS endpoint
- Mixing AWS transport assumptions with vendor-hosted SSE assumptions
- Forgetting region and IAM configuration
- Confusing Claude Messages semantics with Bedrock's broader invocation APIs

## Sources

- AWS Anthropic Claude Messages API: <https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages.html>
- AWS supported Claude models: <https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-supported-models.html>
