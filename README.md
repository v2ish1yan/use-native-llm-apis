# use-native-llm-apis

Provider-native LLM API integration skill for agentic coding tools.

This repository helps an agent answer questions like:

- what endpoint should I call
- which auth header does this provider need
- what request shape does this provider expect
- how do streaming, tool calling, or structured output differ here

It is not a universal SDK, and it is not 31 equally deep provider references.

## What this repo actually contains

- a strong routing skill for provider-native API implementation work
- a small set of deep core-provider references
- a wider provider registry with uneven depth

Some provider files are strong enough to drive end-to-end code generation. Some are only usable as starting notes. Some are still skeletons.

Always check [references/research/coverage-status.md](references/research/coverage-status.md) before relying on a provider file.

## Coverage honesty

This repo currently has three practical content tiers:

- `gold`: strong end-to-end references with request shape, response parsing, and advanced-feature guidance
- `usable`: enough detail for many integrations, but not yet a full native reference
- `skeleton`: basic auth/base-url/endpoint notes, not enough to promise reliable code generation by themselves

The skill architecture covers the full registry. The content depth does not.

## What makes the skill useful

- narrow trigger boundary: it focuses on provider-native API implementation work
- deterministic routing: the agent is told exactly how to move from trigger to recipe to provider file
- path safety: provider files are resolved through [references/providers/index.md](references/providers/index.md) instead of guessed from memory
- honest maintenance: routing, examples, and coverage depth now have separate source-of-truth files

## Start path

When this skill is triggered, the intended path is:

1. open [references/start-here.md](references/start-here.md)
2. choose exactly one task recipe
3. resolve the provider file through [references/providers/index.md](references/providers/index.md)
4. open one comparison file only when the task requires it
5. run [references/routing-checklist.md](references/routing-checklist.md)
6. then write code

## Task recipes

| You want to... | Start here |
|----------------|-----------|
| integrate one provider | [integrate-one-provider.md](references/recipes/integrate-one-provider.md) |
| migrate between providers | [migrate-between-providers.md](references/recipes/migrate-between-providers.md) |
| add streaming | [add-streaming.md](references/recipes/add-streaming.md) |
| add tool calling | [add-tool-calling.md](references/recipes/add-tool-calling.md) |
| add structured JSON output | [add-structured-output.md](references/recipes/add-structured-output.md) |
| debug a failed request | [debug-failed-request.md](references/recipes/debug-failed-request.md) |

## Comparison files

The comparison files are strongest for the core native providers they explicitly discuss.

Do not assume a comparison file fully covers every gateway or OpenAI-compatible relay in the registry. For those, prefer the provider file first and treat comparison docs as partial guidance.

## Example prompts

```text
Use $use-native-llm-apis to write an Anthropic streaming request in TypeScript.
```

```text
Convert this OpenAI request into Gemini native format.
```

```text
我要接入 DeepSeek API。
```

More trigger examples live in [references/recipes/prompt-patterns.md](references/recipes/prompt-patterns.md).

## Install

### Codex

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.codex\skills" | Out-Null
git clone https://github.com/v2ish1yan/use-native-llm-apis.git "$HOME\.codex\skills\use-native-llm-apis"
```

### Claude Code

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.claude\skills" | Out-Null
git clone https://github.com/v2ish1yan/use-native-llm-apis.git "$HOME\.claude\skills\use-native-llm-apis"
```

Folder name must stay `use-native-llm-apis`. Restart the tool after install.

## Repository structure

```text
use-native-llm-apis/
|-- SKILL.md
|-- CLAUDE.md
|-- README.md
`-- references/
    |-- start-here.md
    |-- routing-checklist.md
    |-- index.md
    |-- recipes/
    |-- providers/
    |-- comparisons/
    `-- research/
```

## Maintenance

If you are improving the skill itself, start with:

- [references/research/validation-and-maintenance.md](references/research/validation-and-maintenance.md)
- [references/research/skill-smoke-tests.md](references/research/skill-smoke-tests.md)

Coverage maturity and official source tracking live here:

- [references/research/coverage-status.md](references/research/coverage-status.md)
- [references/research/source-registry.md](references/research/source-registry.md)
