# use-native-llm-apis

Provider-native LLM API integration skill for agentic coding tools.

This is not a universal SDK, and it is not 31 equally deep provider references. Its main value is different:

- agents often have to rediscover auth headers, base URLs, and request shapes
- provider APIs look similar enough to confuse migrations, but different enough to break them
- agents tend to guess provider paths, compatibility, or streaming behavior too early

This skill turns that into a more reliable path:

1. decide whether the request should trigger the skill
2. choose the right task recipe
3. resolve the exact provider file through the provider index
4. check comparisons only when needed
5. write code after routing is complete

[中文 README](README.md)

## Why use this skill

It is most useful when you need to:

- integrate a specific provider's native API
- migrate OpenAI-shaped code to Gemini, Anthropic, DeepSeek, or another native format
- add streaming, tool calling, or structured output to an existing request path
- debug 400 / 401 / 422 request failures
- work with gateways or relays such as OpenRouter, SiliconFlow, NewAPI, or DMXAPI

Its value is not only the references themselves, but also the routing discipline around them.

## What the repo contains

- a skill with a narrow trigger boundary
- a deterministic routing flow
- high-value task recipes
- a provider registry covering 31 provider / gateway / relay entries
- maintenance docs, coverage tracking, and a source registry

## Coverage honesty

Depth is intentionally uneven. The active tiers are:

- `gold`: strong enough for deeper end-to-end generation
- `usable`: enough detail for many practical integrations
- `partial`: publicly verified, but not strong enough to promise reliable end-to-end generation

Older maintenance language may still mention `skeleton` as a reserved or historical label, but the live snapshot is tracked in [coverage-status.md](references/research/coverage-status.md).

Do not confuse "31 entries" with "31 equally complete references."

## Trigger boundary

This skill should trigger when both are true:

1. the user names a provider, or clearly implies a provider-native API
2. the user is asking for implementation work in code

Examples:

```text
I need to integrate the DeepSeek API.
```

```text
Convert this OpenAI request into Gemini native format.
```

```text
Use $use-native-llm-apis to write an Anthropic streaming request in TypeScript.
```

```text
Debug why this Claude request is returning 401.
```

For more trigger examples and few-shot routing, see [prompt-patterns.md](references/recipes/prompt-patterns.md).

## Recommended path

When the skill is triggered, use this order:

1. open [start-here.md](references/start-here.md)
2. choose exactly one task recipe
3. resolve the provider path through [providers/index.md](references/providers/index.md)
4. open the exact provider file
5. open one comparison file only if needed
6. run [routing-checklist.md](references/routing-checklist.md)
7. then write or patch code

## High-value recipes

| Task | Entry |
|---|---|
| integrate one provider | [integrate-one-provider.md](references/recipes/integrate-one-provider.md) |
| migrate between providers | [migrate-between-providers.md](references/recipes/migrate-between-providers.md) |
| add streaming | [add-streaming.md](references/recipes/add-streaming.md) |
| add tool calling | [add-tool-calling.md](references/recipes/add-tool-calling.md) |
| add structured JSON output | [add-structured-output.md](references/recipes/add-structured-output.md) |
| debug a failed request | [debug-failed-request.md](references/recipes/debug-failed-request.md) |

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

Update:

```powershell
git -C "$HOME\.codex\skills\use-native-llm-apis" pull
git -C "$HOME\.claude\skills\use-native-llm-apis" pull
```

The folder name must remain `use-native-llm-apis`. Restart the agent after install or update.

## Repository structure

```text
use-native-llm-apis/
|-- SKILL.md
|-- CLAUDE.md
|-- README.md
|-- README-EN.md
`-- references/
    |-- start-here.md
    |-- routing-checklist.md
    |-- providers/
    |-- recipes/
    |-- comparisons/
    `-- research/
```

## If you maintain this skill

Start with:

- [validation-and-maintenance.md](references/research/validation-and-maintenance.md)
- [skill-smoke-tests.md](references/research/skill-smoke-tests.md)
- [coverage-status.md](references/research/coverage-status.md)
- [source-registry.md](references/research/source-registry.md)

In one sentence:

This skill is a routing layer plus reference library for provider-native API work, designed to help agents guess less, route faster, and write fewer wrong requests.
