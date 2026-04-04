# Add Tool Calling

Use this recipe when the model must call local functions, services, or external tools.

## Goal

Get one full tool loop working:

1. declare tools
2. receive a tool call
3. execute the tool
4. send the tool result back in the provider's native continuation format

## What to open first

1. the target provider file
2. `references/comparisons/tool-calling-differences.md`

## Safe order

1. Start with one tiny tool and one required argument.
2. Validate the provider's tool declaration schema.
3. Log the raw tool-call payload from the model.
4. Execute the tool outside the model loop first if needed.
5. Return the result using the provider's native continuation shape.

## High-risk differences

- `parameters` vs `input_schema`
- OpenAI or DeepSeek `role: "tool"` continuation vs Anthropic `tool_result`
- Gemini function declarations and function-response flow

## Common mistakes

- Copying OpenAI tool schema directly into Anthropic
- Returning tool output in the wrong role or block type
- Letting the tool return large unbounded payloads
- Trying to debug tool declarations and tool continuation in the same step

## Minimal success test

Use one deterministic tool, such as:

- `get_weather(city)`
- `lookup_order(id)`
- `read_file(path)`

The model should produce exactly one tool call and then answer using the tool result.

## Exit criteria

This recipe is complete when one full request -> tool call -> tool result -> final answer loop works with the provider's native schema.
