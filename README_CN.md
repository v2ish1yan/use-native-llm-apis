<div align="center">

# use-native-llm-apis

**LLM API 原生集成参考库**

Auth · Endpoint · Request Shape · Streaming · Tool Calling · Structured Output

31 家厂商，精确到字段级别的协议对照表——不是通用 SDK，是开箱即用的 wire-format 参考。

<p>
<a href="README.md">📝 English Docs</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="#安装">安装</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="#使用方法">使用方法</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="#支持的厂商-31">厂商列表</a>
</p>

[![GitHub stars](https://img.shields.io/github/stars/v2ish1yan/use-native-llm-apis?style=social)](https://github.com/v2ish1yan/use-native-llm-apis)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Providers](https://img.shields.io/badge/providers-31-green.svg)](#支持的厂商-31)

</div>

---

## 为什么做这个

每次接入一个新的 LLM API，你都在重复同一件事：翻文档、查 base URL、对 auth header、调试 request body。不同厂商的接口长得不一样，却又不够不一样到让你一眼记住区别。

这个仓库把 **31 家厂商的原生 API 协议**打包成结构化参考。打开对应的文件，拿到精确的请求格式，继续写代码。

---

## 支持的厂商 (31)

### 原生 LLM 厂商

| 厂商 | 官方文档 | 参考 |
|------|----------|------|
| OpenAI | [platform.openai.com](https://platform.openai.com/docs/) | [openai.md](references/providers/openai.md) |
| Anthropic (Claude) | [docs.anthropic.com](https://docs.anthropic.com/) | [anthropic.md](references/providers/anthropic.md) |
| Google Gemini | [ai.google.dev](https://ai.google.dev/gemini-api/docs) | [gemini.md](references/providers/gemini.md) |
| DeepSeek | [api-docs.deepseek.com](https://api-docs.deepseek.com/) | [deepseek.md](references/providers/deepseek.md) |
| 智谱 GLM | [docs.bigmodel.cn](https://docs.bigmodel.cn/) | [zhipu-glm.md](references/providers/zhipu-glm.md) |
| 阿里百炼 / DashScope | [help.aliyun.com](https://help.aliyun.com/zh/model-studio/) | [alibaba-bailian.md](references/providers/alibaba-bailian.md) |
| Kimi / 月之暗面 | [platform.moonshot.cn](https://platform.moonshot.cn/docs/introduction) | [kimi-moonshot.md](references/providers/kimi-moonshot.md) |
| 豆包 / 火山引擎 | [volcengine.com](https://www.volcengine.com/docs/82379) | [doubao-volcengine-ark.md](references/providers/doubao-volcengine-ark.md) |
| MiniMax | [platform.minimax.io](https://platform.minimax.io/docs/api-reference/api-overview) | [minimax.md](references/providers/minimax.md) |
| 阶跃星辰 | [platform.stepfun.com](https://platform.stepfun.com/docs/api-reference/chat/chat-completion-create) | [stepfun.md](references/providers/stepfun.md) |
| 小米 MiMo | [platform.xiaomimimo.com](https://platform.xiaomimimo.com/#/docs/welcome) | [xiaomi-mimo.md](references/providers/xiaomi-mimo.md) |

### 云平台 & 托管服务

| 厂商 | 官方文档 | 参考 |
|------|----------|------|
| Azure OpenAI | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/work-with-code) | [azure-openai.md](references/providers/azure-openai.md) |
| AWS Bedrock | [docs.aws.amazon.com](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages.html) | [aws-bedrock.md](references/providers/aws-bedrock.md) |
| NVIDIA NIM | [docs.api.nvidia.com](https://docs.api.nvidia.com/nim/reference/llm-apis) | [nvidia-nim.md](references/providers/nvidia-nim.md) |
| 魔搭 ModelScope | [modelscope.cn](https://modelscope.cn/docs/model-service/API-Inference/intro) | [modelscope.md](references/providers/modelscope.md) |
| GitHub Copilot SDK | [docs.github.com](https://docs.github.com/en/copilot/concepts/agents/openai-codex) | [github-copilot.md](references/providers/github-copilot.md) |

### 网关 & 聚合平台

| 厂商 | 官方文档 | 参考 |
|------|----------|------|
| OpenRouter | [openrouter.ai](https://openrouter.ai/docs/api/reference/overview/) | [openrouter.md](references/providers/openrouter.md) |
| 硅基流动 SiliconFlow | [docs.siliconflow.com](https://docs.siliconflow.com/en/api-reference/chat-completions/chat-completions) | [siliconflow.md](references/providers/siliconflow.md) |
| AiHubMix | [docs.aihubmix.com](https://docs.aihubmix.com/en) | [aihubmix.md](references/providers/aihubmix.md) |
| Novita AI | [novita.ai](https://novita.ai/docs/api-reference) | [novita-ai.md](references/providers/novita-ai.md) |
| NewAPI | [docs.newapi.pro](https://docs.newapi.pro/en/) | [newapi.md](references/providers/newapi.md) |

### 中转 / 代理服务

| 厂商 | 官方文档 | 参考 |
|------|----------|------|
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

### 跨厂商对比

| 主题 | 参考 |
|------|------|
| 请求格式差异 | [request-shape-differences.md](references/comparisons/request-shape-differences.md) |
| 流式输出差异 | [streaming-differences.md](references/comparisons/streaming-differences.md) |
| 工具调用差异 | [tool-calling-differences.md](references/comparisons/tool-calling-differences.md) |
| 结构化输出差异 | [structured-output-differences.md](references/comparisons/structured-output-differences.md) |

---

## 安装

### Claude Code

```bash
# macOS / Linux
mkdir -p ~/.claude/skills
git clone https://github.com/v2ish1yan/use-native-llm-apis.git ~/.claude/skills/use-native-llm-apis

# Windows PowerShell
New-Item -ItemType Directory -Force -Path "$HOME\.claude\skills" | Out-Null
git clone https://github.com/v2ish1yan/use-native-llm-apis.git "$HOME\.claude\skills\use-native-llm-apis"
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

更新：

```bash
git -C ~/.claude/skills/use-native-llm-apis pull   # Claude Code
git -C ~/.codex/skills/use-native-llm-apis pull     # Codex
```

> 文件夹名必须是 `use-native-llm-apis`。安装后重启 agent。

---

## 使用方法

### 任务路由

| 你想... | 从这里开始 |
|---------|-----------|
| 接入一个厂商 | [integrate-one-provider.md](references/recipes/integrate-one-provider.md) |
| 在厂商之间迁移 | [migrate-between-providers.md](references/recipes/migrate-between-providers.md) |
| 加流式输出 | [add-streaming.md](references/recipes/add-streaming.md) |
| 加工具调用 | [add-tool-calling.md](references/recipes/add-tool-calling.md) |
| 加结构化 JSON 输出 | [add-structured-output.md](references/recipes/add-structured-output.md) |
| 调试失败的请求 | [debug-failed-request.md](references/recipes/debug-failed-request.md) |

### 示例 Prompt

```
Use $use-native-llm-apis to write an Anthropic streaming request in TypeScript.
```

```
我要把 OpenAI 接口切换成 DeepSeek
```

```
帮我排查这个 DeepSeek 请求为什么一直 401
```

完整的触发短语和路由规则见 [prompt-patterns.md](references/recipes/prompt-patterns.md)。

---

## 仓库结构

```
use-native-llm-apis/
├── SKILL.md              # Skill 定义和触发规则
├── CLAUDE.md             # Claude Code 专用指南
├── README.md             # 英文文档
├── README_CN.md          # 中文文档（本文件）
└── references/
    ├── index.md           # 入口
    ├── recipes/           # 任务工作流指南
    ├── providers/         # 各厂商 API 参考 (31)
    ├── comparisons/       # 跨厂商对比 (4)
    └── research/          # 覆盖状态和来源注册
```

---

<div align="center">

**MIT License** · [覆盖状态](references/research/coverage-status.md) · [来源注册](references/research/source-registry.md)

</div>
