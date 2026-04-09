<div align="center">

# use-native-llm-apis

**Provider-native LLM API integration reference for coding assistants**

Stop re-searching auth headers, base URLs, request bodies, and streaming formats

[中文](README.md) · [Quick Start](#how-to-use-it) · [Install](#install) · [FAQ](#faq)

---

![38+ Providers](https://img.shields.io/badge/Providers-38%2B-blue)
![4 Gold References](https://img.shields.io/badge/Gold%20References-4-brightgreen)
![28 Usable References](https://img.shields.io/badge/Usable%20References-28-green)
![License MIT](https://img.shields.io/badge/License-MIT-lightgrey)

</div>

## What problem this solves

Provider APIs are similar enough to confuse you, but different enough to break your code in annoying ways. Path compatibility ≠ behavior compatibility.

This skill reduces repeated work when connecting to LLM APIs: less searching, less guessing, less trial and error, less rework.

## Coverage

| Category | Providers |
|:---|:---|
| **Native LLM Providers** | OpenAI · Anthropic · Gemini · DeepSeek · Zhipu · Bailian · Kimi · Doubao · MiniMax · StepFun · Xiaomi MiMo |
| **Cloud & Managed Platforms** | Azure OpenAI · AWS Bedrock · NVIDIA NIM · ModelScope · GitHub Copilot SDK |
| **Gateways & Aggregation** | OpenRouter · SiliconFlow · AiHubMix · Novita AI · NewAPI |
| **Relays & Proxy Services** | PackyCode · Cubence · CrazyRouter · Compshare · CTok.ai · Right Code · X-Code API · Ai Go Code · AICodeMirror · DMXAPI |

Depth tiers:

| Tier | Description |
|:---:|:---|
| `gold` | Strong end-to-end reference for direct implementation |
| `usable` | Enough for many real integrations; verify while coding |
| `partial` | Starting point for research, not a full production contract |

> See [coverage-status.md](references/research/coverage-status.md) for latest status

## How to use it

Don't browse the repo manually. Just describe your task directly:

```
I need to integrate the DeepSeek API
```
```
Convert this OpenAI request into Gemini native format
```
```
Add streaming to our Claude request in TypeScript
```
```
Debug why this request keeps returning 401
```

More examples → [prompt-patterns.md](references/recipes/prompt-patterns.md)

## Common Use Cases

| Scenario | What you get |
|:---|:---|
| Integrate native API | Auth headers, base URLs, endpoints aligned |
| Cross-provider migration | OpenAI → Gemini / Anthropic / DeepSeek mapping |
| Add streaming | SSE format differences across providers |
| Add tool calling | Field names, structure, invocation patterns |
| Structured JSON output | Provider support and limitations |
| Debug request errors | 400 / 401 / 422 / 429 / 5xx troubleshooting templates |
| Gateway/relay integration | OpenRouter, SiliconFlow compatibility notes |

## Reference Index

| Document | Content |
|:---|:---|
| [providers/index.md](references/providers/index.md) | Provider entry index |
| [request-shape-differences.md](references/comparisons/request-shape-differences.md) | Request body differences |
| [streaming-differences.md](references/comparisons/streaming-differences.md) | Streaming output differences |
| [tool-calling-differences.md](references/comparisons/tool-calling-differences.md) | Tool calling differences |
| [structured-output-differences.md](references/comparisons/structured-output-differences.md) | Structured output differences |

## Install

### Option 1: Claude Code Plugin (Recommended)

**Direct Install (GitHub)**

```
/plugin install use-native-llm-apis@github:v2ish1yan/use-native-llm-apis
```

Or add via Marketplace:

```
/plugin marketplace add v2ish1yan/use-native-llm-apis
/plugin install use-native-llm-apis@native-llm-apis-marketplace
```

### Option 2: Manual Clone

**Codex**

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.codex\skills" | Out-Null
git clone https://github.com/v2ish1yan/use-native-llm-apis.git "$HOME\.codex\skills\use-native-llm-apis"
```

**Claude Code**

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.claude\skills" | Out-Null
git clone https://github.com/v2ish1yan/use-native-llm-apis.git "$HOME\.claude\skills\use-native-llm-apis"
```

**Update**

```powershell
git -C "$HOME\.codex\skills\use-native-llm-apis" pull
git -C "$HOME\.claude\skills\use-native-llm-apis" pull
```

> The folder name must remain `use-native-llm-apis`. Restart the tool after install or update.

## FAQ

<details>
<summary><b>"Many platforms say they are OpenAI-compatible, why do I still need this?"</b></summary>

Because path compatibility is not behavior compatibility. Many platforms accept `/v1` requests but still differ in auth headers, streaming format, tool-calling fields, structured-output support, and response field paths. Real failures usually come from the parts that are "almost the same".

</details>

<details>
<summary><b>"How is this different from a unified SDK or abstraction layer?"</b></summary>

A unified SDK helps you call multiple providers through one interface. This skill helps when you need to work with native provider details directly and want to reduce guesswork, rework, and protocol mistakes. If your project depends on provider-native behavior, careful migrations, or request-level debugging, this skill is more direct.

</details>

<details>
<summary><b>"How should I interpret gold / usable / partial?"</b></summary>

- **gold** — Strong enough for direct end-to-end implementation
- **usable** — Enough for many real integrations; verify while coding
- **partial** — Starting point for research, not a full production contract

</details>

## Maintenance

Reference docs for maintainers:

- [validation-and-maintenance.md](references/research/validation-and-maintenance.md)
- [skill-smoke-tests.md](references/research/skill-smoke-tests.md)
- [coverage-status.md](references/research/coverage-status.md)
- [source-registry.md](references/research/source-registry.md)

---

<div align="center">

A practical provider-native API reference and integration aid for real development work

Not a heavy abstraction layer or universal SDK

</div>
