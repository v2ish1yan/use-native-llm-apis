# Start Here

Use this page first when the skill is triggered.

## Route in four steps

1. Choose exactly one task recipe.
2. Open [providers/index.md](providers/index.md) and click the exact provider file.
3. Open one comparison file only when needed.
4. Run [routing-checklist.md](routing-checklist.md) before coding.

## Choose one task

| User need | Recipe |
|-----------|--------|
| make one provider work from scratch | [recipes/integrate-one-provider.md](recipes/integrate-one-provider.md) |
| port one provider integration to another | [recipes/migrate-between-providers.md](recipes/migrate-between-providers.md) |
| add incremental output | [recipes/add-streaming.md](recipes/add-streaming.md) |
| let the model call functions or tools | [recipes/add-tool-calling.md](recipes/add-tool-calling.md) |
| return machine-parseable output | [recipes/add-structured-output.md](recipes/add-structured-output.md) |
| fix a failing provider request | [recipes/debug-failed-request.md](recipes/debug-failed-request.md) |

Do not open multiple recipes unless the current recipe explicitly requires a comparison file.

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
