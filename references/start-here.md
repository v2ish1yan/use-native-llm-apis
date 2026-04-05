# Start Here

Use this file first when the skill is triggered.

The point of this page is to keep routing mechanical. Do not jump straight from `SKILL.md` to a provider file or comparison file.

## Step 1: Decide whether the skill applies

Trigger only if both are true:

1. the request names a provider or clearly implies a provider-native API
2. the request asks for implementation work such as integrate, migrate, stream, tool calling, structured output, or debugging

If either part is missing, use the missing-info rules in [../SKILL.md](../SKILL.md).

## Step 2: Choose exactly one task

| If the user wants to... | Open this recipe |
|-------------------------|------------------|
| make one provider work from scratch | [recipes/integrate-one-provider.md](recipes/integrate-one-provider.md) |
| port working code from one provider to another | [recipes/migrate-between-providers.md](recipes/migrate-between-providers.md) |
| add incremental output after non-stream works | [recipes/add-streaming.md](recipes/add-streaming.md) |
| let the model call functions or tools | [recipes/add-tool-calling.md](recipes/add-tool-calling.md) |
| make output machine-parseable | [recipes/add-structured-output.md](recipes/add-structured-output.md) |
| fix a failing provider request | [recipes/debug-failed-request.md](recipes/debug-failed-request.md) |

Do not open multiple recipes unless the current recipe explicitly tells you to open a comparison file.

## Step 3: Resolve the provider path

Open [providers/index.md](providers/index.md), then click the exact provider file.

Do not guess slugs such as:

- `moonshot` vs `kimi-moonshot`
- `ark` vs `doubao-volcengine-ark`
- `glm` vs `zhipu-glm`

## Step 4: Load one comparison file only when needed

| Need | File |
|------|------|
| request body or response shape differences | [comparisons/request-shape-differences.md](comparisons/request-shape-differences.md) |
| streaming differences | [comparisons/streaming-differences.md](comparisons/streaming-differences.md) |
| tool-calling differences | [comparisons/tool-calling-differences.md](comparisons/tool-calling-differences.md) |
| structured-output differences | [comparisons/structured-output-differences.md](comparisons/structured-output-differences.md) |

## Step 5: Then code

Only after recipe + provider file + optional comparison file are open should you write or patch code.
