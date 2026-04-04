# Add Streaming

Use this recipe when a non-stream request already works and the next step is incremental output.

## Goal

Add streaming without breaking text assembly or finish detection.

## What to open first

1. the target provider file
2. `references/comparisons/streaming-differences.md`

## Safe order

1. Confirm the provider's stream toggle.
2. Verify whether the transport is SSE or another chunked format.
3. Log raw stream events before transforming them.
4. Write a provider-aware parser.
5. Add text assembly and stop handling.

## Provider-aware parser checklist

- How do chunks arrive?
- Which field contains incremental text?
- How is the final event signaled?
- Where should usage or finish metadata be read?

## Common mistakes

- Parsing OpenAI Responses as chat-completions deltas
- Treating Anthropic named events as anonymous JSON lines
- Assuming Gemini stream parts match Anthropic content blocks
- Using the non-stream response parser on stream chunks

## Minimal success test

You should be able to print:

1. the first incremental token or text fragment
2. the assembled final text
3. the finish signal or final stream close event

## Exit criteria

This recipe is complete when streamed output matches the non-stream result closely enough for the feature you are shipping.
