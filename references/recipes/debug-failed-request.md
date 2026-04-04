# Debug Failed Request

Use this recipe when a provider request is failing with 400-class errors or unexpected output.

## Goal

Find the first wrong assumption in the request path.

## What to open first

1. the target provider file
2. the relevant comparison file if the code came from another provider

## Debug order

1. auth header
2. base URL
3. endpoint path
4. required version or feature headers
5. top-level request keys
6. nested content shape
7. advanced features such as streaming, tools, or schemas

## Status-code guide

- `400`: request shape is likely wrong
- `401`: auth token or auth header is wrong
- `403`: token exists but lacks permission or the region/account is wrong
- `404`: base URL or path is wrong
- `415`: content type is wrong
- `422`: request is structurally valid JSON but semantically wrong for the provider

## Fast debugging pattern

- Log the exact outbound URL.
- Log headers with secrets redacted.
- Log the raw request body.
- Log the raw error body.
- Compare all of it against the provider file before changing code.

## Common mistakes

- Debugging three variables at once
- Assuming a provider is fully OpenAI-compatible because the path starts with `/v1`
- Forgetting region-specific endpoints
- Debugging stream parsing when the initial request is not yet valid

## Exit criteria

This recipe is complete when the failing request is reduced to one known mismatch and that mismatch is either fixed or documented.
