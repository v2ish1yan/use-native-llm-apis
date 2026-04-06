# Handle Rate Limits and Errors

Use this recipe when a provider request is failing with `429`, intermittent `5xx`, or unclear error payloads and you need retry behavior that is safe enough for real code.

## Goal

Turn "it sometimes fails" into a small, explicit policy:

- retry only when the failure is likely transient
- honor provider hints such as `Retry-After`
- log enough detail to distinguish rate limits from auth or request-shape bugs
- fail loudly when the error is non-retryable

## What to open first

You should already have come through `references/start-here.md`.

1. `references/providers/index.md`
2. the target provider file linked from `references/providers/index.md`
3. `references/recipes/debug-failed-request.md` if you still are not sure the request itself is valid

If you have not yet confirmed the request shape, auth header, and endpoint path, do that before adding retries.

## Retry policy

Treat the response like this by default:

| Signal | Default action |
|------|------|
| `429` | retry |
| `500`, `502`, `503`, `504`, `529` | retry |
| network timeout / temporary DNS / connection reset | retry |
| `400`, `401`, `403`, `404`, `422` | do not retry |
| invalid JSON from your own client code | do not retry |

Do not retry forever. A small capped policy is usually enough:

- max attempts: `4`
- base delay: `500ms`
- cap delay: `8s`
- jitter: yes

## Retry-After rule

If the response includes `Retry-After`, honor it before your own exponential backoff.

Handle both common forms:

- delta seconds, such as `Retry-After: 2`
- HTTP date, such as `Retry-After: Wed, 21 Oct 2015 07:28:00 GMT`

If the parsed value is invalid or negative, fall back to your computed backoff delay.

## Error-envelope checklist

Before writing provider-specific parsing logic, log these fields when present:

- HTTP status
- response headers related to limits or request id
- top-level `error`
- `error.type`
- `error.code`
- `error.message`
- provider request id header or body field if documented

Why this matters:

- `401` with an error body is usually an auth bug, not a retry case
- `429` with a clear rate-limit message should back off, not re-shape the body
- `422` usually means the JSON is valid but the provider rejected the field contract

## Minimal TypeScript pattern

Adapt the status checks and body parsing after reading the provider file.

```ts
type RetryDecision = {
  retry: boolean;
  reason: string;
  delayMs: number;
};

function parseRetryAfter(headerValue: string | null): number | null {
  if (!headerValue) return null;

  const seconds = Number(headerValue);
  if (Number.isFinite(seconds) && seconds >= 0) {
    return seconds * 1000;
  }

  const at = Date.parse(headerValue);
  if (Number.isNaN(at)) return null;

  return Math.max(0, at - Date.now());
}

function computeBackoffDelay(attempt: number, baseMs = 500, capMs = 8000): number {
  const exponential = Math.min(capMs, baseMs * 2 ** (attempt - 1));
  const jitter = Math.floor(Math.random() * Math.max(250, exponential / 2));
  return Math.min(capMs, exponential + jitter);
}

function classifyRetry(status: number, retryAfterMs: number | null, attempt: number): RetryDecision {
  if (status === 429) {
    return {
      retry: true,
      reason: "rate_limit",
      delayMs: retryAfterMs ?? computeBackoffDelay(attempt),
    };
  }

  if ([500, 502, 503, 504, 529].includes(status)) {
    return {
      retry: true,
      reason: "transient_server_error",
      delayMs: retryAfterMs ?? computeBackoffDelay(attempt),
    };
  }

  return {
    retry: false,
    reason: "non_retryable",
    delayMs: 0,
  };
}

function summarizeErrorBody(payload: unknown): string {
  if (!payload || typeof payload !== "object") {
    return "No structured error body returned.";
  }

  const error = (payload as Record<string, unknown>).error;
  if (error && typeof error === "object") {
    const e = error as Record<string, unknown>;
    return JSON.stringify(
      {
        type: e.type ?? null,
        code: e.code ?? null,
        message: e.message ?? null,
      },
      null,
      2
    );
  }

  return JSON.stringify(payload, null, 2);
}

async function callProviderWithRetries(
  url: string,
  headers: Record<string, string>,
  body: unknown,
  maxAttempts = 4
): Promise<Response> {
  let lastError: unknown;

  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    try {
      const response = await fetch(url, {
        method: "POST",
        headers,
        body: JSON.stringify(body),
      });

      if (response.ok) {
        return response;
      }

      const responseText = await response.text();
      let parsedBody: unknown = null;

      try {
        parsedBody = responseText ? JSON.parse(responseText) : null;
      } catch {
        parsedBody = responseText;
      }

      const retryAfterMs = parseRetryAfter(response.headers.get("retry-after"));
      const decision = classifyRetry(response.status, retryAfterMs, attempt);

      console.error("Provider request failed", {
        attempt,
        status: response.status,
        retry: decision.retry,
        reason: decision.reason,
        retryAfterMs,
        requestId:
          response.headers.get("request-id") ??
          response.headers.get("x-request-id") ??
          response.headers.get("anthropic-request-id"),
        error: summarizeErrorBody(parsedBody),
      });

      if (!decision.retry || attempt === maxAttempts) {
        throw new Error(
          `Provider request failed with status ${response.status} after ${attempt} attempt(s).`
        );
      }

      await new Promise((resolve) => setTimeout(resolve, decision.delayMs));
    } catch (error) {
      lastError = error;

      if (attempt === maxAttempts) {
        break;
      }

      const delayMs = computeBackoffDelay(attempt);
      console.error("Transient network error while calling provider", {
        attempt,
        delayMs,
        message: error instanceof Error ? error.message : String(error),
      });
      await new Promise((resolve) => setTimeout(resolve, delayMs));
    }
  }

  throw lastError instanceof Error ? lastError : new Error(String(lastError));
}
```

## What not to do

- do not add retries before confirming the provider file and request shape
- do not retry `401`, `403`, or `422` as if they were transient
- do not swallow the final error and return an empty string or placeholder JSON
- do not use identical fixed sleeps for every retry
- do not hide provider request ids; they are often the fastest support handle

## Quick decision table

| Situation | Best next move |
|------|------|
| first request is returning `401` | stop retry work, fix auth first |
| request only fails under load with `429` | add capped retry with `Retry-After` support |
| request fails randomly with `502` or `503` | add transient retry policy |
| error body is opaque or inconsistent | log status, headers, and `error.*` fields before changing payload shape |
| migrated code is returning `422` | compare request body with the provider file before adding backoff |

## Exit criteria

This recipe is complete when:

- non-retryable errors fail loudly with enough context
- retryable errors back off with jitter and honor `Retry-After`
- logs make it obvious whether the next fix belongs in auth, request shape, or retry policy
