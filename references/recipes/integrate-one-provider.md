# Integrate One Provider

Use this recipe when the task is "make one provider work end to end" instead of building a universal abstraction.

## Goal

Get to one verified request path quickly:

1. authenticate correctly
2. send one minimal non-stream request
3. inspect the raw response shape
4. add streaming, tools, or structured output only after the base request works

## What to open first

You should already have come through `references/start-here.md`.

1. `references/providers/index.md`
2. the exact target file linked from `references/providers/index.md`
3. `references/comparisons/request-shape-differences.md` if the code was copied from another provider

If you know the provider name but not the file path, use `references/providers/index.md` instead of guessing.

## Fast path

1. Copy the provider's documented base URL and auth header exactly.
2. Send the smallest possible text-generation request.
3. Log the raw JSON response before wrapping it in app-specific helpers.
4. Confirm which field your app should read for generated text.
5. Only then add retries, streaming, tools, or response schemas.

## Minimal integration pattern (TypeScript)

This skeleton works for any provider - swap the auth header, base URL, and body shape according to the provider file.

```ts
async function callProvider(prompt: string): Promise<string> {
  const response = await fetch("https://PROVIDER_BASE_URL/ENDPOINT_PATH", {
    method: "POST",
    headers: {
      // Fill these from the provider file
      "authorization": "Bearer $PROVIDER_API_KEY", // or x-api-key, or api-key
      "content-type": "application/json",
      // Some providers require version headers - check the provider file
    },
    body: JSON.stringify({
      // Fill the request shape from the provider file
      model: "MODEL_NAME",
      messages: [{ role: "user", content: prompt }],
      // Some providers use: input, contents, prompt - check the provider file
    }),
  });

  if (!response.ok) {
    const errorBody = await response.text();
    console.error("Request failed:", response.status, errorBody);
    throw new Error(`Provider returned ${response.status}`);
  }

  const data = await response.json();
  // Extract text - check the provider file for the correct field path:
  //   OpenAI-style:   data.choices[0].message.content
  //   Anthropic-style: data.content.find(b => b.type === "text")?.text
  //   Gemini-style:   data.candidates[0].content.parts[0].text
  const text =
    data.choices?.[0]?.message?.content ??
    data.content?.find?.((b: { type?: string; text?: string }) => b.type === "text")?.text ??
    data.candidates?.[0]?.content?.parts?.[0]?.text;

  if (typeof text !== "string" || text.length === 0) {
    throw new Error(
      "Text extraction path is not configured for this provider yet. Check the provider file and update the response parser."
    );
  }

  return text;
}
```

## What to extract from the provider file

- auth header format and any required version headers
- base URL and endpoint path
- minimal request body shape (top-level keys, message format)
- response field that contains generated text
- provider-specific caveats about streaming, tools, or JSON mode

## Do not do this first

- Do not build a cross-provider adapter before one provider works.
- Do not assume OpenAI compatibility means behavioral compatibility.
- Do not combine first-request debugging with stream parsing.

## Exit criteria

This recipe is complete when you have:

- one successful non-stream request
- one verified text extraction path
- one short note in code or comments about where provider-specific behavior begins
