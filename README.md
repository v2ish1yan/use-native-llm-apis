<div align="center">

# use-native-llm-apis

**LLM API 原生集成参考库**

一次写入，31 家厂商原生 API 请求格式尽在掌握。

[Supported Providers](#supported-providers-31) · [Install](#install) · [Usage](#usage)

</div>

---

## Why this exists

每次接入一个新的 LLM API，你都在重复同一件事：翻文档、查 base URL、对 auth header、调试 request body 格式。不同厂商的接口长得不一样，却又不够不一样到让你一眼记住区别。

这个仓库把 33 家主流 LLM 厂商的原生 API 协议打包成结构化参考——auth、endpoint、request shape、response shape、streaming、tool calling、structured output，开箱即用。

它不是一个通用 SDK，而是一份**精确到字段级别的协议对照表**。

---

## Supported Providers (31)

### Native LLM Providers

| Provider | Docs | Reference |
|----------|------|-----------|
| OpenAI | [platform.openai.com](https://platform.openai.com/docs/) | [openai.md](references/providers/openai.md) |
| Anthropic (Claude) | [docs.anthropic.com](https://docs.anthropic.com/) | [anthropic.md](references/providers/anthropic.md) |
| Google Gemini | [ai.google.dev](https://ai.google.dev/gemini-api/docs) | [gemini.md](references/providers/gemini.md) |
| DeepSeek | [api-docs.deepseek.com](https://api-docs.deepseek.com/) | [deepseek.md](references/providers/deepseek.md) |
| Zhipu GLM / 智谱 | [docs.bigmodel.cn](https://docs.bigmodel.cn/) | [zhipu-glm.md](references/providers/zhipu-glm.md) |
| Alibaba Bailian / 阿里百炼 | [help.aliyun.com](https://help.aliyun.com/zh/model-studio/) | [alibaba-bailian.md](references/providers/alibaba-bailian.md) |
| Kimi / Moonshot / 月之暗面 | [platform.moonshot.cn](https://platform.moonshot.cn/docs/introduction) | [kimi-moonshot.md](references/providers/kimi-moonshot.md) |
| Doubao / 豆包 / 火山引擎 | [volcengine.com](https://www.volcengine.com/docs/82379) | [doubao-volcengine-ark.md](references/providers/doubao-volcengine-ark.md) |
| MiniMax | [platform.minimax.io](https://platform.minimax.io/docs/api-reference/api-overview) | [minimax.md](references/providers/minimax.md) |
| StepFun / 阶跃星辰 | [platform.stepfun.com](https://platform.stepfun.com/docs/api-reference/chat/chat-completion-create) | [stepfun.md](references/providers/stepfun.md) |
| Xiaomi MiMo / 小米 | [platform.xiaomimimo.com](https://platform.xiaomimimo.com/#/docs/welcome) | [xiaomi-mimo.md](references/providers/xiaomi-mimo.md) |

### Cloud & Managed Platforms

| Provider | Docs | Reference |
|----------|------|-----------|
| Azure OpenAI | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/work-with-code) | [azure-openai.md](references/providers/azure-openai.md) |
| AWS Bedrock | [docs.aws.amazon.com](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages.html) | [aws-bedrock.md](references/providers/aws-bedrock.md) |
| NVIDIA NIM | [docs.api.nvidia.com](https://docs.api.nvidia.com/nim/reference/llm-apis) | [nvidia-nim.md](references/providers/nvidia-nim.md) |
| ModelScope / 魔搭 | [modelscope.cn](https://modelscope.cn/docs/model-service/API-Inference/intro) | [modelscope.md](references/providers/modelscope.md) |
| GitHub Copilot / Copilot SDK | [docs.github.com](https://docs.github.com/en/copilot/concepts/agents/openai-codex) | [github-copilot.md](references/providers/github-copilot.md) |

### Gateway & Aggregation Layers

| Provider | Docs | Reference |
|----------|------|-----------|
| OpenRouter | [openrouter.ai](https://openrouter.ai/docs/api/reference/overview/) | [openrouter.md](references/providers/openrouter.md) |
| SiliconFlow / 硅基流动 | [docs.siliconflow.com](https://docs.siliconflow.com/en/api-reference/chat-completions/chat-completions) | [siliconflow.md](references/providers/siliconflow.md) |
| AiHubMix | [docs.aihubmix.com](https://docs.aihubmix.com/en) | [aihubmix.md](references/providers/aihubmix.md) |
| Novita AI | [novita.ai](https://novita.ai/docs/api-reference) | [novita-ai.md](references/providers/novita-ai.md) |
| NewAPI | [docs.newapi.pro](https://docs.newapi.pro/en/) | [newapi.md](references/providers/newapi.md) |

### Relay / Proxy Services

| Provider | Docs | Reference |
|----------|------|-----------|
| PackyCode | [docs.packyapi.com](https://docs.packyapi.com/) | [packycode.md](references/providers/packycode.md) |
| Cubence | [docs.cubence.com](https://docs.cubence.com/) | [cubence.md](references/providers/cubence.md) |
| CrazyRouter | [crazyrouter.com](https://crazyrouter.com/) | [crazyrouter.md](references/providers/crazyrouter.md) |
| Compshare | [compshare.cn](https://www.compshare.cn/docs) | [compshare.md](references/providers/compshare.md) |
| CTok.ai | [ctok.ai](https://ctok.ai/) | [ctok-ai.md](references/providers/ctok-ai.md) |
| Right Code | [docs.right.codes](https://docs.right.codes/) | [rightcode.md](references/providers/rightcode.md) |
| X-Code API | [docs.x-code.cc](https://docs.x-code.cc/) | [xcode-api.md](references/providers/xcode-api.md) |
| Ai Go Code | [aigocode.com](https://www.aigocode.com/docs) | [aigocode.md](references/providers/aigocode.md) |
| AICodeMirror | [aicodemirror.com](https://www.aicodemirror.com/docs) | [aicodemirror.md](references/providers/aicodemirror.md) |
| DMXAPI | [doc.dmxapi.com](https://doc.dmxapi.com/) | [dmxapi.md](references/providers/dmxapi.md) |

### Cross-Provider Comparisons

| Topic | Reference |
|-------|-----------|
| Request shape differences | [request-shape-differences.md](references/comparisons/request-shape-differences.md) |
| Streaming differences | [streaming-differences.md](references/comparisons/streaming-differences.md) |
| Tool-calling differences | [tool-calling-differences.md](references/comparisons/tool-calling-differences.md) |
| Structured-output differences | [structured-output-differences.md](references/comparisons/structured-output-differences.md) |

---

## Install

### Claude Code

```bash
# macOS / Linux
mkdir -p ~/.claude/skills
git clone https://github.com/v2ish1yan/use-native-llm-apis.git ~/.claude/skills/use-native-llm-apis

# Windows PowerShell
New-Item -ItemType Directory -Force -Path "$HOME\.claude\skills" | Out-Null
git clone https://github.com/v2ish1yan/use-native-llm-apis.git "$HOME\.claude\skills\use-native-llm-apis"
```

Update:

```bash
git -C ~/.claude/skills/use-native-llm-apis pull
```

### Codex

```bash
# macOS / Linux
mkdir -p ~/.codex/skills
git clone https://github.com/v2ish1yan/use-native-llm-apis.git ~/.codex/skills/use-native-llm-apis

# Windows PowerShell
New-Item -ItemType Directory -Force -Path "$HOME\.codex\skills" | Out-Null
git clone https://github.com/v2ish1yan/use-native-llm-apis.git "$HOME\.codex\skills\use-native-llm-apis"
```

Update:

```bash
git -C ~/.codex/skills/use-native-llm-apis pull
```

> **Note**: Folder name must be exactly `use-native-llm-apis`. Restart the agent after install.

---

## Usage

### Task Routing

| You want to... | Start here |
|----------------|-----------|
| Integrate one provider | [integrate-one-provider.md](references/recipes/integrate-one-provider.md) |
| Migrate between providers | [migrate-between-providers.md](references/recipes/migrate-between-providers.md) |
| Add streaming | [add-streaming.md](references/recipes/add-streaming.md) |
| Add tool calling | [add-tool-calling.md](references/recipes/add-tool-calling.md) |
| Add structured JSON output | [add-structured-output.md](references/recipes/add-structured-output.md) |
| Debug a failed request | [debug-failed-request.md](references/recipes/debug-failed-request.md) |

### Example Prompts

```
Use $use-native-llm-apis to write an Anthropic streaming request in TypeScript.
```

```
Use $use-native-llm-apis to convert an OpenAI request into Gemini native format.
```

```
Use $use-native-llm-apis to debug why this Gemini request returns 400.
```

### Chinese Trigger Phrases

以下中文表达会自动触发此 skill：

- "我要接入 DeepSeek 大模型 API"
- "帮我对接 Anthropic API"
- "把 OpenAI 改成 Gemini 原生格式"
- "给这个项目加上流式输出"
- "帮我加工具调用"
- "让模型返回结构化 JSON"
- "排查这个模型接口为什么 400/401"

---

## Repository Structure

```
use-native-llm-apis/
├── SKILL.md              # Skill definition & trigger rules
├── CLAUDE.md             # Claude Code specific guidance
├── agents/
│   └── openai.yaml       # Agent interface config
└── references/
    ├── index.md           # Entry point
    ├── recipes/           # Task workflow guides
    ├── providers/         # Per-provider API references (33)
    ├── comparisons/       # Cross-provider diff guides (4)
    └── research/          # Coverage status & source registry
```

---

<div align="center">

MIT License · [Coverage Status](references/research/coverage-status.md) · [Source Registry](references/research/source-registry.md)

</div>
