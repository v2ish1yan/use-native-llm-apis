# Add Streaming

Use this recipe when a non-stream request already works and the next step is incremental output.

## Goal

Add streaming without breaking text assembly or finish detection.

## What to open first

You should already have come through `references/start-here.md`.

1. `references/providers/index.md`
2. the target provider file linked from `references/providers/index.md`
3. `references/comparisons/streaming-differences.md`

## Safe order

1. Confirm the provider's stream toggle.
2. Verify whether the transport is SSE or another chunked format.
3. Log raw stream events before transforming them.
4. Write a provider-aware parser.
5. Add text assembly and stop handling.

## Generic SSE stream parser (TypeScript)

This parser handles the SSE wire format shared by most providers. The provider-specific part is **which event names and data fields to extract** — fill those from the provider file.

```ts
async function streamProvider(
  url: string,
  headers: Record<string, string>,
  body: Record<string, unknown>,
  // Provider-specific extractors — fill from the provider file
  extractors: {
    isTextEvent: (eventName: string, data: Record<string, unknown>) => boolean;
    getTextChunk: (data: Record<string, unknown>) => string;
    isDoneEvent: (eventName: string, data: Record<string, unknown>) => boolean;
  }
): Promise<string> {
  const response = await fetch(url, {
    method: "POST",
    headers,
    body: JSON.stringify({ ...body, stream: true }),
  });

  if (!response.ok || !response.body) {
    throw new Error(`Stream request failed: ${response.status}`);
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  let fullText = "";

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });

    while (buffer.includes("\n\n")) {
      const boundary = buffer.indexOf("\n\n");
      const rawEvent = buffer.slice(0, boundary);
      buffer = buffer.slice(boundary + 2);

      let eventName = "";
      const dataLines: string[] = [];

      for (const line of rawEvent.split("\n")) {
        if (line.startsWith("event:")) eventName = line.slice(6).trim();
        else if (line.startsWith("data:")) dataLines.push(line.slice(5).trim());
      }

      const dataText = dataLines.join("\n");
      if (!dataText || dataText === "[DONE]") continue;

      let parsed: Record<string, unknown>;
      try { parsed = JSON.parse(dataText); } catch { continue; }

      if (extractors.isTextEvent(eventName, parsed)) {
        const chunk = extractors.getTextChunk(parsed);
        if (chunk) {
          fullText += chunk;
          process.stdout.write(chunk);
        }
      }

      if (extractors.isDoneEvent(eventName, parsed)) {
        process.stdout.write("\n");
        return fullText;
      }
    }
  }

  return fullText;
}
```

### Provider-specific extractor examples

```ts
// OpenAI Chat Completions
const openaiExtractors = {
  isTextEvent: (_: string, d: any) => d.choices?.[0]?.delta?.content !== undefined,
  getTextChunk: (d: any) => d.choices[0].delta.content ?? "",
  isDoneEvent: (_: string, d: any) => d.choices?.[0]?.finish_reason !== null,
};

// Anthropic Messages
const anthropicExtractors = {
  isTextEvent: (name: string) => name === "content_block_delta",
  getTextChunk: (d: any) => d.delta?.text ?? "",
  isDoneEvent: (name: string) => name === "message_stop",
};
```

## Provider-aware parser checklist

- How do chunks arrive? (SSE events, JSON lines, or chunked JSON)
- Which field contains incremental text?
- How is the final event signaled? (finish_reason, message_stop, [DONE], etc.)
- Where should usage or finish metadata be read?

## Common mistakes

- Parsing OpenAI Responses as chat-completions deltas
- Treating Anthropic named events as anonymous JSON lines
- Assuming Gemini stream parts match Anthropic content blocks
- Using the non-stream response parser on stream chunks

## Exit criteria

This recipe is complete when streamed output matches the non-stream result closely enough for the feature you are shipping.
