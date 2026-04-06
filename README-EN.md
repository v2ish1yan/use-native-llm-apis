# use-native-llm-apis

A provider-native LLM API integration skill for coding assistants.

Its purpose is simple: when you need to connect a project to an LLM API, you should not have to keep re-searching auth headers, base URLs, request bodies, streaming formats, or migration differences from scratch every time.

[中文 README](README.md)

## What this skill helps with

This skill is built for common integration tasks such as:

- integrating a provider's native LLM API
- migrating OpenAI-shaped code to Gemini, Anthropic, DeepSeek, or another native format
- adding streaming to an existing request path
- adding tool calling
- returning structured JSON output
- debugging 400 / 401 / 422 request failures
- working with gateways and relays such as OpenRouter, SiliconFlow, NewAPI, and DMXAPI

In short, it solves a very practical problem:

provider APIs are similar enough to confuse you, but different enough to break your code in annoying ways.

## Why it is worth installing

If you regularly build with LLM APIs, this skill helps reduce repeated work:

- less searching: fewer trips back to provider docs for headers, endpoints, and body shape
- less guessing: fewer memory-based assumptions about request formats or compatibility
- less trial and error: easier migrations between providers
- less rework: fewer cases where the code looks done but fails because one field or auth convention is wrong

It is especially useful for requests like:

- "I need to integrate the DeepSeek API"
- "Convert this OpenAI request to Gemini native format"
- "Add streaming to our Claude request"
- "Debug why this request keeps returning 401"
- "Help me integrate an OpenAI-compatible platform, but I am not sure how compatible it really is"

## Coverage

The repository currently covers 31 provider / gateway / relay entries, including:

- native providers: OpenAI, Anthropic, Gemini, DeepSeek, Zhipu, Bailian, Kimi, Doubao, MiniMax, StepFun, Xiaomi MiMo
- cloud and managed platforms: Azure OpenAI, AWS Bedrock, NVIDIA NIM, ModelScope, GitHub Copilot SDK
- gateways and aggregation layers: OpenRouter, SiliconFlow, AiHubMix, Novita AI, NewAPI
- relays and proxy services: PackyCode, Cubence, CrazyRouter, Compshare, CTok.ai, Right Code, X-Code API, Ai Go Code, AICodeMirror, DMXAPI

But the important part is this:

this is not a 31-provider library with equal depth across all entries.

The active depth tiers are:

- `gold`: strong enough for deeper end-to-end work
- `usable`: enough detail for many real integrations
- `partial`: publicly verified, but still not deep enough for confident end-to-end generation

A practical way to use them:

- start with `gold` if you want the strongest direct coding support
- use `usable` when you are comfortable verifying while implementing
- treat `partial` as a starting point for research, not as a full integration contract

The latest status is tracked here:

- [coverage-status.md](references/research/coverage-status.md)

## How to use it

The most effective way to use this skill is not to browse the repo manually first.

Instead, describe the task directly in your coding request.

For example:

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
Debug why this Claude request keeps returning 401.
```

More examples live here:

- [prompt-patterns.md](references/recipes/prompt-patterns.md)

## What you get from it

What you get is not a universal SDK. You get a high-value reference set:

- provider request-shape references
- auth header, base URL, and endpoint guidance
- differences in streaming, tool calling, and structured output
- migration-oriented mapping hints
- debugging-oriented request checks

If you want to go deeper, start here:

- [providers/index.md](references/providers/index.md)
- [request-shape-differences.md](references/comparisons/request-shape-differences.md)
- [streaming-differences.md](references/comparisons/streaming-differences.md)
- [tool-calling-differences.md](references/comparisons/tool-calling-differences.md)
- [structured-output-differences.md](references/comparisons/structured-output-differences.md)

## FAQ

### If many platforms say they are OpenAI-compatible, why do I still need this skill?

Because path compatibility is not behavior compatibility.

Many platforms can accept a similar `/v1` request, but still differ in:

- auth headers
- streaming format
- tool-calling fields
- structured-output support
- response field paths

The real integration failures usually come from the parts that are "almost the same", not the parts that are obviously different.

### How is this different from a unified SDK or abstraction layer?

A unified SDK helps you call multiple providers through one interface.

This skill helps when you need to work with native provider details directly and want to reduce guesswork, rework, and protocol mistakes.

If your project depends on provider-native behavior, careful migrations, or request-level debugging, this skill is usually more direct than abstraction-layer docs.

### How should I interpret `gold`, `usable`, and `partial`?

- `gold`: strong enough to support more direct end-to-end implementation
- `usable`: enough for many real integrations, but best used with verification while coding
- `partial`: best treated as a starting point for research, not as a full production contract

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

The folder name must remain `use-native-llm-apis`. Restart the tool after install or update.

## Maintenance

If you maintain this skill, start with:

- [validation-and-maintenance.md](references/research/validation-and-maintenance.md)
- [skill-smoke-tests.md](references/research/skill-smoke-tests.md)
- [coverage-status.md](references/research/coverage-status.md)
- [source-registry.md](references/research/source-registry.md)

The best way to think about this project is:

it is a practical provider-native API reference and integration aid for real development work, not a heavy abstraction layer or universal SDK.
