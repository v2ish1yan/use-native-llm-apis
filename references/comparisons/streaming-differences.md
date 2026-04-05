# Streaming Differences

Use this file when your code already works in non-stream mode but breaks in stream mode.

This comparison is strongest for the core providers explicitly listed below. Do not assume it fully covers every gateway or OpenAI-compatible relay in the registry.

## Transport

- OpenAI Responses: SSE event stream
- Anthropic: SSE event stream with named event lifecycle
- Gemini: streaming endpoint with SSE output
- DeepSeek: OpenAI-like SSE chunks

## What arrives incrementally

- OpenAI Responses: incremental response events
- Anthropic: content-block deltas and message lifecycle events
- Gemini: partial candidate content
- DeepSeek: `choices[].delta`

## Parser design

Your parser should be provider-aware:

- Anthropic needs event-type routing
- DeepSeek usually fits an OpenAI chat-style chunk parser
- OpenAI Responses should not be parsed as chat-completions deltas
- Gemini should be treated as candidate updates, not Anthropic event blocks

## Finish conditions

Do not reuse one provider's finish check everywhere:

- OpenAI Responses completes on final response events
- Anthropic ends with message stop semantics
- Gemini ends when the stream closes after final candidate data
- DeepSeek often mirrors OpenAI-style stop chunks
