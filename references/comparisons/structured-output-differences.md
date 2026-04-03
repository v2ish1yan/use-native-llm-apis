# Structured-Output Differences

Use this file when the output must be consumed by code instead of a human.

## Native structured-output style

- OpenAI: JSON schema via response text format
- Anthropic: most portable baseline is tool-mediated structured output or tightly constrained JSON patterns
- Gemini: `generationConfig.responseMimeType` plus `responseSchema`
- DeepSeek: provider-documented JSON mode or compatible schema controls where supported

## Reliability expectation

- OpenAI and Gemini expose explicit native schema-oriented controls
- Anthropic can produce reliable machine-readable output, but the path is not a copy of OpenAI's schema API
- DeepSeek behavior is close to OpenAI chat-completions style, but feature depth can differ by model

## Safe default

If strict output validity matters across multiple providers:

1. prefer native schema controls where the provider offers them
2. otherwise use tools/functions as the schema boundary
3. avoid relying only on "please return valid JSON"

## Portability warning

Do not assume that "JSON mode" and "JSON schema mode" mean the same thing across vendors. Some providers guarantee syntax, some guide the model, and some attach stronger semantics only to specific models or request paths.

## OpenAI to Gemini structured-output remap

When porting a schema-constrained OpenAI request to Gemini:

- move the schema from the OpenAI `text.format.schema` area into `generationConfig.responseSchema`
- set `generationConfig.responseMimeType` to `application/json`
- convert common JSON Schema type names to Gemini's uppercase style where required by the API shape you are using

Safe mental model:

- OpenAI says "format the response with this schema"
- Gemini says "generate content with this MIME type and this response schema"
