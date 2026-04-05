# Debug Failed Request

Use this recipe when a provider request is failing with 400-class errors or unexpected output.

## Goal

Find the first wrong assumption in the request path.

## What to open first

1. `references/index.md`
2. `references/providers/index.md`
3. the target provider file linked from `references/providers/index.md`
4. the relevant comparison file if the code came from another provider

If the failing code does not clearly identify the provider yet, confirm the provider before assuming a file.

## Debug order

Check these in order — stop at the first mismatch:

1. **auth header** — correct header name? (`Authorization: Bearer` vs `x-api-key` vs `api-key`)
2. **base URL** — correct region? correct domain? no typo?
3. **endpoint path** — `/v1/chat/completions` vs `/v1/messages` vs `/v1/models/MODEL:generateContent`
4. **required headers** — version header? (`anthropic-version`, nothing for OpenAI)
5. **top-level request keys** — `messages` vs `input` vs `contents`?
6. **nested content shape** — string vs block array vs parts array?
7. **advanced features** — streaming toggle, tool schema names, JSON mode fields

## Status-code guide

| Code | Most likely cause |
|------|------------------|
| `400` | Request shape is wrong — missing required field, wrong nesting, invalid enum value |
| `401` | Auth token or auth header is wrong — check key, check header name |
| `403` | Token exists but lacks permission, wrong region, or model not enabled for account |
| `404` | Base URL or endpoint path is wrong |
| `415` | Content-Type header is wrong or missing |
| `422` | Structurally valid JSON but semantically wrong — wrong field names, invalid schema |

## Debug logging pattern

Before changing any code, log the exact outbound request:

```ts
async function debugRequest(url: string, headers: Record<string, string>, body: unknown) {
  // Log outbound (redact secrets)
  const safeHeaders = Object.fromEntries(
    Object.entries(headers).map(([k, v]) => [
      k,
      k.toLowerCase().includes("auth") || k.toLowerCase().includes("key") || k.toLowerCase().includes("api")
        ? `${v.slice(0, 8)}...`
        : v,
    ])
  );

  console.error("── Outbound Request ──");
  console.error("URL:", url);
  console.error("Headers:", JSON.stringify(safeHeaders, null, 2));
  console.error("Body:", JSON.stringify(body, null, 2));

  const response = await fetch(url, {
    method: "POST",
    headers,
    body: JSON.stringify(body),
  });

  // Log inbound
  const responseText = await response.text();
  console.error("── Response ──");
  console.error("Status:", response.status, response.statusText);
  console.error("Body:", responseText);

  // Compare against the provider file before changing code
  // Check: auth header format, base URL, endpoint path, request keys, content nesting
}
```

## Common mistakes

- Debugging three variables at once — fix one thing, test, repeat
- Assuming a provider is fully OpenAI-compatible because the path starts with `/v1`
- Forgetting region-specific endpoints (Azure, AWS, some Chinese providers)
- Debugging stream parsing when the initial non-stream request is not yet valid
- Changing the request body before confirming the auth header is correct

## Quick checklist for migrated code

If the code worked with one provider and breaks with another, check:

- [ ] Auth header name changed? (`Authorization` → `x-api-key` → `api-key`)
- [ ] Version header added or removed?
- [ ] Base URL and path both changed?
- [ ] System prompt moved? (message array → top-level field → config object)
- [ ] Tool schema field renamed? (`parameters` → `input_schema`)
- [ ] Response text field path changed? (`choices[0].message.content` → `content[0].text`)

## Exit criteria

This recipe is complete when the failing request is reduced to one known mismatch and that mismatch is either fixed or documented.
