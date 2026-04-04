# Integrate One Provider

Use this recipe when the task is "make one provider work end to end" instead of building a universal abstraction.

## Goal

Get to one verified request path quickly:

1. authenticate correctly
2. send one minimal non-stream request
3. inspect the raw response shape
4. add streaming, tools, or structured output only after the base request works

## What to open first

1. the target file in `references/providers/`
2. `references/comparisons/request-shape-differences.md` if the code was copied from another provider

## Fast path

1. Copy the provider's documented base URL and auth header exactly.
2. Send the smallest possible text-generation request.
3. Log the raw JSON response before wrapping it in app-specific helpers.
4. Confirm which field your app should read for generated text.
5. Only then add retries, streaming, tools, or response schemas.

## What to extract from the provider file

- auth header format
- base URL
- primary endpoint
- minimal request body
- response fields that contain text
- provider-specific caveats about streaming, tools, or JSON mode

## Safe implementation pattern

- Keep the first implementation close to raw HTTP.
- Prefer `fetch` plus explicit headers over hiding the request behind a large SDK wrapper.
- Keep provider-specific field names visible in the code until the request is proven correct.

## Do not do this first

- Do not build a cross-provider adapter before one provider works.
- Do not assume OpenAI compatibility means behavioral compatibility.
- Do not combine first-request debugging with stream parsing.

## Exit criteria

This recipe is complete when you have:

- one successful non-stream request
- one verified text extraction path
- one short note in code or comments about where provider-specific behavior begins
