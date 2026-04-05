# use-native-llm-apis

Provider-native LLM API integration reference for agentic coding tools.

This repository is meant to help an agent answer questions like:

- what endpoint should I call
- which auth header does this provider need
- what request shape does this provider expect
- how do streaming, tool calling, or structured output differ here

It is not a universal SDK. It is a skill plus a set of provider-native references.

## What makes this skill useful

- narrow trigger boundary: it focuses on provider-native API implementation work
- deterministic routing: the agent is told exactly how to move from trigger to recipe to provider file
- path safety: provider files are resolved through [references/providers/index.md](references/providers/index.md) instead of guessed from memory
- maintainable docs: trigger rules, start flow, few-shot examples, and coverage status have clear owners

## Start path

When this skill is triggered, the intended path is:

1. open [references/start-here.md](references/start-here.md)
2. choose exactly one task recipe
3. resolve the provider file through [references/providers/index.md](references/providers/index.md)
4. open one comparison file only when the task requires it
5. then write code

## Task recipes

| You want to... | Start here |
|----------------|-----------|
| integrate one provider | [integrate-one-provider.md](references/recipes/integrate-one-provider.md) |
| migrate between providers | [migrate-between-providers.md](references/recipes/migrate-between-providers.md) |
| add streaming | [add-streaming.md](references/recipes/add-streaming.md) |
| add tool calling | [add-tool-calling.md](references/recipes/add-tool-calling.md) |
| add structured JSON output | [add-structured-output.md](references/recipes/add-structured-output.md) |
| debug a failed request | [debug-failed-request.md](references/recipes/debug-failed-request.md) |

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
