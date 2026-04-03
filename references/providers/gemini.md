# Gemini Native API

## Summary

Use Gemini's native Generative Language API when integrating Google Gemini directly. The main conceptual difference from OpenAI and Anthropic is that Gemini uses `contents` with nested `parts`, and many advanced behaviors live under `tools`, `toolConfig`, and `generationConfig`.

## Auth and Base URL

- Base URL: `https://generativelanguage.googleapis.com`
- Typical version prefix: `/v1beta`
- Auth:
  - query param `key=$GEMINI_API_KEY`, or
  - `x-goog-api-key: $GEMINI_API_KEY`

## Primary text-generation endpoint

- `POST /v1beta/models/{model}:generateContent`

## Minimal request

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          { "text": "Write a one-line hello in Python." }
        ]
      }
    ]
  }'
```

## Response shape

Common fields to read:

- `candidates`
- `candidates[0].content.parts`
- `usageMetadata`
- `promptFeedback`

Plain text usually appears in `candidates[0].content.parts[*].text`.

## Streaming notes

- Use `streamGenerateContent`
- The streamed variant is usually:
  - `POST /v1beta/models/{model}:streamGenerateContent?alt=sse`
- Gemini stream chunks return partial candidate content, not OpenAI-style delta envelopes and not Anthropic named event blocks

## Tool-calling notes

Gemini function tools are declared under `tools`, usually with `functionDeclarations`.

Minimal shape:

```json
{
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "lookup_weather",
          "description": "Get the weather for a city",
          "parameters": {
            "type": "OBJECT",
            "properties": {
              "city": { "type": "STRING" }
            },
            "required": ["city"]
          }
        }
      ]
    }
  ]
}
```

Use `toolConfig` when you need to influence function-calling behavior.

Minimal function-calling request:

```json
{
  "contents": [
    {
      "role": "user",
      "parts": [
        { "text": "What is the weather in Shanghai?" }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "lookup_weather",
          "description": "Get the weather for a city",
          "parameters": {
            "type": "OBJECT",
            "properties": {
              "city": { "type": "STRING" }
            },
            "required": ["city"]
          }
        }
      ]
    }
  ]
}
```

## Structured-output notes

Gemini's native structured-output pattern uses `generationConfig`:

- `responseMimeType: "application/json"`
- `responseSchema: { ... }`

This is the native Gemini way to request machine-readable JSON output.

## Multimodal notes

Gemini natively handles multimodal content through `parts`. Common part forms include:

- text parts
- `inline_data`
- `file_data`

Keep multimodal input inside `contents[].parts[]`.

## Embeddings notes

Gemini exposes embeddings separately from `generateContent`.

Look for:

- `embedContent`
- `batchEmbedContents`

## Common pitfalls

- Sending OpenAI-style `messages` instead of `contents`
- Forgetting that Gemini schema types are often uppercase (`OBJECT`, `STRING`)
- Expecting Anthropic-style stream events or OpenAI-style deltas
- Putting image input in the wrong top-level field instead of `parts`

## OpenAI-to-Gemini mental remap

When adapting OpenAI-style code:

- `messages` becomes `contents`
- `message.content[]` becomes `parts[]`
- OpenAI text items become Gemini text parts
- OpenAI JSON schema controls become `generationConfig.responseSchema`
- OpenAI function tools become `functionDeclarations`

Concrete OpenAI Responses to Gemini conversion:

OpenAI Responses request:

```json
{
  "model": "gpt-5.4",
  "input": [
    {
      "role": "user",
      "content": [
        { "type": "input_text", "text": "Extract the city and country from: Paris, France" }
      ]
    }
  ],
  "text": {
    "format": {
      "type": "json_schema",
      "schema": {
        "type": "object",
        "properties": {
          "city": { "type": "string" },
          "country": { "type": "string" }
        },
        "required": ["city", "country"]
      }
    }
  }
}
```

Gemini native equivalent:

```json
{
  "contents": [
    {
      "role": "user",
      "parts": [
        { "text": "Extract the city and country from: Paris, France" }
      ]
    }
  ],
  "generationConfig": {
    "responseMimeType": "application/json",
    "responseSchema": {
      "type": "OBJECT",
      "properties": {
        "city": { "type": "STRING" },
        "country": { "type": "STRING" }
      },
      "required": ["city", "country"]
    }
  }
}
```

Minimal TypeScript conversion example:

```ts
const openAiStylePrompt = "Extract the city and country from: Paris, France";

const geminiRequestBody = {
  contents: [
    {
      role: "user",
      parts: [{ text: openAiStylePrompt }],
    },
  ],
  generationConfig: {
    responseMimeType: "application/json",
    responseSchema: {
      type: "OBJECT",
      properties: {
        city: { type: "STRING" },
        country: { type: "STRING" },
      },
      required: ["city", "country"],
    },
  },
};
```

## Sources

- Gemini text generation docs: <https://ai.google.dev/gemini-api/docs/text-generation>
- Gemini function calling docs: <https://ai.google.dev/gemini-api/docs/function-calling>
- Gemini structured output docs: <https://ai.google.dev/gemini-api/docs/structured-output>
- Gemini embeddings docs: <https://ai.google.dev/gemini-api/docs/embeddings>
