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

## Tool declaration shapes by provider

The three major tool declaration formats:

```jsonc
// OpenAI / DeepSeek / OpenAI-compatible providers
{
  "tools": [{
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get the weather for a city",
      "parameters": {          // ← note: "parameters"
        "type": "object",
        "properties": {
          "city": { "type": "string" }
        },
        "required": ["city"]
      }
    }
  }]
}

// Anthropic
{
  "tools": [{
    "name": "get_weather",
    "description": "Get the weather for a city",
    "input_schema": {          // ← note: "input_schema"
      "type": "object",
      "properties": {
        "city": { "type": "string" }
      },
      "required": ["city"]
    }
  }]
}

// Gemini
{
  "tools": [{
    "function_declarations": [{  // ← note: nested array
      "name": "get_weather",
      "description": "Get the weather for a city",
      "parameters": {
        "type": "object",
        "properties": {
          "city": { "type": "string" }
        },
        "required": ["city"]
      }
    }]
  }]
}
```

## Tool result continuation shapes

How to return a tool result back to the model:

```jsonc
// OpenAI / DeepSeek — role: "tool" message
{
  "messages": [
    { "role": "user", "content": "What's the weather in Tokyo?" },
    { "role": "assistant", "content": null,
      "tool_calls": [{ "id": "call_abc", "function": { "name": "get_weather", "arguments": "{\"city\":\"Tokyo\"}" } }] },
    { "role": "tool", "tool_call_id": "call_abc",
      "content": "{\"temperature_c\": 22}" }
  ]
}

// Anthropic — tool_result content block in a user message
{
  "messages": [
    { "role": "user", "content": "What's the weather in Tokyo?" },
    { "role": "assistant", "content": [
        { "type": "text", "text": "Let me check." },
        { "type": "tool_use", "id": "toolu_abc", "name": "get_weather", "input": { "city": "Tokyo" } }
    ]},
    { "role": "user", "content": [
        { "type": "tool_result", "tool_use_id": "toolu_abc",
          "content": "{\"temperature_c\": 22}" }
    ]}
  ]
}
```

## High-risk differences

- `parameters` vs `input_schema` — easy to miss, silent failure
- OpenAI `role: "tool"` continuation vs Anthropic `tool_result` content block
- Gemini `functionResponse` part vs function-call part
- Tool call IDs: `call_*` (OpenAI) vs `toolu_*` (Anthropic)

## Minimal success test

Use one deterministic tool, such as:

- `get_weather(city)` → returns `{ temperature_c: 22 }`
- `lookup_order(id)` → returns `{ status: "shipped" }`

The model should produce exactly one tool call and then answer using the tool result.

## Exit criteria

This recipe is complete when one full request → tool call → tool result → final answer loop works with the provider's native schema.
