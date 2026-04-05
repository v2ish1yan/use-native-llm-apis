# Request Shape Differences

Use this file when porting requests between providers or designing an adapter layer.

This comparison is strongest for the core providers explicitly listed below. Do not assume it fully covers every gateway or OpenAI-compatible relay in the registry.

## Top-level request key

- OpenAI Responses: `input`
- Anthropic: `messages`
- Gemini: `contents`
- DeepSeek: `messages`

## User content nesting

- OpenAI Responses: `input[].content[]` with typed items like `input_text`
- Anthropic: `messages[].content` as text or block array
- Gemini: `contents[].parts[]`
- DeepSeek: `messages[].content` usually plain string or OpenAI-style multimodal array depending on endpoint support

## System prompt handling

- OpenAI Responses: can be modeled as a top-level instruction or structured input content depending on workflow
- Anthropic: dedicated top-level `system` field is common
- Gemini: usually modeled inside `contents` or related config, not a clone of Anthropic's top-level `system`
- DeepSeek: typically follows OpenAI chat style with `role: "system"`

## Multimodal placement

- OpenAI: typed content items like `input_image`
- Anthropic: content blocks in the message content array
- Gemini: `parts` entries such as `inline_data` or `file_data`
- DeepSeek: provider-specific and model-specific; do not assume parity

## Practical migration rule

When migrating, do not map field names mechanically. First map the provider's conceptual unit:

- OpenAI: typed input items
- Anthropic: content blocks
- Gemini: parts
- DeepSeek: OpenAI-like messages

## Side-by-side user prompt example

OpenAI Responses:

```json
{
  "input": [
    {
      "role": "user",
      "content": [
        { "type": "input_text", "text": "Say hello" }
      ]
    }
  ]
}
```

Anthropic:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Say hello"
    }
  ]
}
```

Gemini:

```json
{
  "contents": [
    {
      "role": "user",
      "parts": [
        { "text": "Say hello" }
      ]
    }
  ]
}
```

DeepSeek:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Say hello"
    }
  ]
}
```

## OpenAI Responses to Gemini quick mapping

Use this when converting a simple OpenAI Responses request into Gemini native format:

- `input` -> `contents`
- `input[].role` -> `contents[].role`
- `input[].content[]` -> `contents[].parts[]`
- `{ "type": "input_text", "text": "..." }` -> `{ "text": "..." }`
- `text.format.schema` -> `generationConfig.responseSchema`
- `text.format.type = "json_schema"` -> `generationConfig.responseMimeType = "application/json"`

One important detail: Gemini schema types are typically uppercase, so `object` and `string` become `OBJECT` and `STRING`.
