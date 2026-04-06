# Start Here

Use this page first when the skill is triggered.

## Route in four steps

1. Choose exactly one task recipe.
2. Open [providers/index.md](providers/index.md) and click the exact provider file.
3. Open one comparison file only when needed.
4. Run [routing-checklist.md](routing-checklist.md) before coding.

If the task boundary is still fuzzy, open [recipes/choose-the-right-recipe.md](recipes/choose-the-right-recipe.md) before picking a recipe.

## Choose one task

| User need | Recipe |
|-----------|--------|
| make one provider work from scratch | [recipes/integrate-one-provider.md](recipes/integrate-one-provider.md) |
| port one provider integration to another | [recipes/migrate-between-providers.md](recipes/migrate-between-providers.md) |
| add incremental output | [recipes/add-streaming.md](recipes/add-streaming.md) |
| let the model call functions or tools | [recipes/add-tool-calling.md](recipes/add-tool-calling.md) |
| return machine-parseable output | [recipes/add-structured-output.md](recipes/add-structured-output.md) |
| fix a failing provider request | [recipes/debug-failed-request.md](recipes/debug-failed-request.md) |
| handle `429`, `5xx`, backoff, or retry policy | [recipes/handle-rate-limits-and-errors.md](recipes/handle-rate-limits-and-errors.md) |

Do not open multiple recipes unless the current recipe explicitly requires a comparison file.

## Fast split for common failures

- `400 / 401 / 403 / 404 / 415 / 422` -> [recipes/debug-failed-request.md](recipes/debug-failed-request.md)
- `429 / intermittent 5xx / retry / backoff / Retry-After` -> [recipes/handle-rate-limits-and-errors.md](recipes/handle-rate-limits-and-errors.md)
- "just make provider X work" -> [recipes/integrate-one-provider.md](recipes/integrate-one-provider.md)
- "port from provider A to provider B" -> [recipes/migrate-between-providers.md](recipes/migrate-between-providers.md)

## Resolve provider path

Open [providers/index.md](providers/index.md). Do not guess slugs such as:

- `moonshot` vs `kimi-moonshot`
- `ark` vs `doubao-volcengine-ark`
- `glm` vs `zhipu-glm`

## Load comparison only when needed

| Need | File |
|------|------|
| request or response shape differences | [comparisons/request-shape-differences.md](comparisons/request-shape-differences.md) |
| streaming differences | [comparisons/streaming-differences.md](comparisons/streaming-differences.md) |
| tool-calling differences | [comparisons/tool-calling-differences.md](comparisons/tool-calling-differences.md) |
| structured-output differences | [comparisons/structured-output-differences.md](comparisons/structured-output-differences.md) |
