# Tool-Calling Differences

Use this file when you are exposing local functions, RPCs, or external tools to the model.

## Tool declaration schema

- OpenAI: `tools[].parameters`
- Anthropic: `tools[].input_schema`
- Gemini: `tools[].functionDeclarations[].parameters`
- DeepSeek: OpenAI-compatible tool declaration style

## Tool call output shape

- OpenAI: structured tool call output in response items
- Anthropic: `tool_use` content blocks
- Gemini: function-call parts in candidate content
- DeepSeek: usually OpenAI-style tool call payloads

## Returning tool results

- OpenAI: continue the response flow with tool results in the next request
- Anthropic: return `tool_result` blocks in the next user message
- Gemini: follow the native function-response pattern instead of Anthropic block semantics
- DeepSeek: follow the OpenAI-compatible continuation flow

## Continuation reminder by provider

- OpenAI and DeepSeek usually expect you to preserve the assistant tool-call turn and then append a `role: "tool"` message
- Anthropic expects `tool_result` content blocks, not an OpenAI-style `role: "tool"` message
- Gemini expects its own function-response flow, not OpenAI or Anthropic replay semantics

## Portability warning

The schema keywords may look similar, but they are not interchangeable. A tool object copied from OpenAI to Anthropic without renaming `parameters` to `input_schema` will fail.
