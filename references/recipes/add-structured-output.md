# Add Structured Output

Use this recipe when the response must be consumed by code rather than read by a human.

## Goal

Make the output reliably parseable without pretending all providers expose the same schema feature.

## What to open first

1. `references/index.md`
2. `references/providers/index.md`
3. the target provider file linked from `references/providers/index.md`
4. `references/comparisons/structured-output-differences.md`

## Decision rule

Use the strongest supported boundary in this order:

1. native schema controls (if the provider supports `response_format.json_schema` or equivalent)
2. tool or function calling as the schema boundary (declare a "response" tool with your schema)
3. tightly constrained JSON prompts (system instruction + explicit format examples)

## Structured output by provider

```jsonc
// ── OpenAI: response_format with json_schema ──
{
  "model": "gpt-4o",
  "messages": [{ "role": "user", "content": "Create a task" }],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "task",
      "strict": true,
      "schema": {
        "type": "object",
        "properties": {
          "title": { "type": "string" },
          "priority": { "type": "string", "enum": ["low", "medium", "high"] },
          "done": { "type": "boolean" }
        },
        "required": ["title", "priority", "done"],
        "additionalProperties": false
      }
    }
  }
}
// Response: choices[0].message.content is a JSON string matching the schema

// ── Anthropic: tool-mediated structured output ──
// No native json_schema support — use a tool as the schema boundary
{
  "model": "claude-sonnet-4-5",
  "max_tokens": 512,
  "tool_choice": { "type": "tool", "name": "task_output" },
  "tools": [{
    "name": "task_output",
    "description": "Return the task in structured form",
    "input_schema": {
      "type": "object",
      "properties": {
        "title": { "type": "string" },
        "priority": { "type": "string" },
        "done": { "type": "boolean" }
      },
      "required": ["title", "priority", "done"]
    }
  }],
  "messages": [{ "role": "user", "content": "Create a task" }]
}
// Response: content block with type: "tool_use", input field contains the parsed object

// ── Gemini: generationConfig responseMimeType ──
{
  "contents": [{ "role": "user", "parts": [{ "text": "Create a task" }] }],
  "generationConfig": {
    "responseMimeType": "application/json",
    "responseSchema": {
      "type": "object",
      "properties": {
        "title": { "type": "string" },
        "priority": { "type": "string" },
        "done": { "type": "boolean" }
      },
      "required": ["title", "priority", "done"]
    }
  }
}
// Response: candidates[0].content.parts[0].text is a JSON string
```

## Validation pattern

Never trust raw model output — always validate:

```ts
interface Task {
  title: string;
  priority: "low" | "medium" | "high";
  done: boolean;
}

function parseTaskOutput(raw: string): Task {
  let parsed: unknown;
  try {
    parsed = JSON.parse(raw);
  } catch {
    throw new Error(`Model output is not valid JSON: ${raw.slice(0, 100)}`);
  }

  if (typeof parsed !== "object" || parsed === null) {
    throw new Error("Expected a JSON object");
  }

  const obj = parsed as Record<string, unknown>;
  if (typeof obj.title !== "string") throw new Error("Missing or invalid 'title'");
  if (!["low", "medium", "high"].includes(obj.priority as string)) {
    throw new Error(`Invalid priority: ${obj.priority}`);
  }
  if (typeof obj.done !== "boolean") throw new Error("Missing or invalid 'done'");

  return { title: obj.title, priority: obj.priority as Task["priority"], done: obj.done };
}
```

## Safe order

1. Start with a tiny schema (3-4 fields).
2. Verify which native feature the provider actually supports.
3. Parse the result immediately after receipt.
4. Add validation in code.
5. Only then expand the schema.

## Common mistakes

- Assuming "JSON mode" means full schema enforcement — most providers only guarantee valid JSON, not schema conformance
- Reusing OpenAI `json_schema` fields in Gemini unchanged — Gemini uses `responseMimeType` + `responseSchema`
- Relying on prompt wording alone when strict parsing matters
- Skipping runtime validation because the provider "usually" returns valid JSON

## Exit criteria

This recipe is complete when:

- the provider returns machine-consumable output
- your code validates it
- failure cases are handled explicitly
