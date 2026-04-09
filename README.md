<div align="center">

# llm-apis

**原生 LLM API 集成参考，写给编码助手用**

不再反复翻文档、对 header、猜 request body、试 streaming 格式

[English](README-EN.md) · [快速开始](#适合怎么用) · [安装](#安装) · [FAQ](#faq)

---

![覆盖 38+ Provider](https://img.shields.io/badge/Provider-38%2B-blue)
![4 Gold 级参考](https://img.shields.io/badge/Gold%20参考-4-brightgreen)
![28 Usable 级参考](https://img.shields.io/badge/Usable%20参考-28-green)
![License MIT](https://img.shields.io/badge/License-MIT-lightgrey)

</div>

## 解决什么问题

不同厂商的 API 总在"最烦的地方不一样" —— 路径兼容 ≠ 行为兼容。

这个 skill 让你接入大模型 API 时少查、少猜、少试错、少返工。

## 覆盖范围

| 类别 | Provider |
|:---|:---|
| **原生 LLM 厂商** | OpenAI · Anthropic · Gemini · DeepSeek · 智谱 · 百炼 · Kimi · 豆包 · MiniMax · StepFun · 小米 MiMo |
| **云与托管平台** | Azure OpenAI · AWS Bedrock · NVIDIA NIM · ModelScope · GitHub Copilot SDK |
| **网关与聚合层** | OpenRouter · SiliconFlow · AiHubMix · Novita AI · NewAPI |
| **中转与代理服务** | PackyCode · Cubence · CrazyRouter · Compshare · CTok.ai · Right Code · X-Code API · Ai Go Code · AICodeMirror · DMXAPI |

内容深度分级：

| 级别 | 说明 |
|:---:|:---|
| `gold` | 端到端参考，可直接支撑完整接入 |
| `usable` | 支持大部分实际集成，建议边写边核对 |
| `partial` | 有线索入口，不宜直接生成生产代码 |

> 详细状态见 [coverage-status.md](references/research/coverage-status.md)

## 适合怎么用

不需要手动翻仓库，直接对编码助手说出你的需求：

```
我要接入 DeepSeek API
```
```
帮我把 OpenAI 请求改成 Gemini 原生格式
```
```
给 Claude 请求加流式输出，用 TypeScript
```
```
这个请求一直 401，帮我排查一下
```

更多示例 → [prompt-patterns.md](references/recipes/prompt-patterns.md)

## 高频场景

| 场景 | 说明 |
|:---|:---|
| 接入厂商原生 API | auth header、base URL、endpoint 一次对齐 |
| 跨厂商迁移 | OpenAI → Gemini / Anthropic / DeepSeek 重点映射 |
| 加 streaming | 各厂商 SSE 格式差异速查 |
| 加 tool calling | 字段名、结构、调用方式对比 |
| 结构化 JSON 输出 | 各厂商支持方式与限制 |
| 请求级错误排查 | 400 / 401 / 422 / 429 / 5xx 排查模板 |
| 网关 / 中转接入 | OpenRouter、SiliconFlow 等兼容程度与注意事项 |

## 参考文档索引

| 文档 | 内容 |
|:---|:---|
| [providers/index.md](references/providers/index.md) | 厂商入口索引 |
| [request-shape-differences.md](references/comparisons/request-shape-differences.md) | 请求体差异对比 |
| [streaming-differences.md](references/comparisons/streaming-differences.md) | 流式输出差异 |
| [tool-calling-differences.md](references/comparisons/tool-calling-differences.md) | 工具调用差异 |
| [structured-output-differences.md](references/comparisons/structured-output-differences.md) | 结构化输出差异 |

## 安装

### 方式一：Claude Code 插件安装（推荐）

**直接安装（GitHub）**

```
/plugin install llm-apis@github:v2ish1yan/llm-apis
```

或先添加 Marketplace：

```
/plugin marketplace add v2ish1yan/llm-apis
/plugin install llm-apis@native-llm-apis-marketplace
```

### 方式二：手动克隆

**Codex**

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.codex\skills" | Out-Null
git clone https://github.com/v2ish1yan/llm-apis.git "$HOME\.codex\skills\llm-apis"
```

**Claude Code**

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.claude\skills" | Out-Null
git clone https://github.com/v2ish1yan/llm-apis.git "$HOME\.claude\skills\llm-apis"
```

**更新**

```powershell
git -C "$HOME\.codex\skills\llm-apis" pull
git -C "$HOME\.claude\skills\llm-apis" pull
```

> 目录名必须保持为 `llm-apis`。安装或更新后重启工具。

## FAQ

<details>
<summary><b>"很多平台都说自己 OpenAI-compatible，为什么还需要这个？"</b></summary>

因为路径兼容 ≠ 行为兼容。很多平台虽然接受 `/v1` 请求，但在鉴权 header、流式输出格式、tool calling 字段、structured output 支持、响应字段路径上仍有差异。真正出错的通常是"看起来差不多，但差在最关键的一两个字段上"。

</details>

<details>
<summary><b>"它和统一 SDK / 抽象层有什么区别？"</b></summary>

统一 SDK 解决"用同一套接口调多厂商"。这个 skill 解决"当你必须面对原生接口细节时，怎么少踩坑、少返工、少猜协议"。如果你的项目需要 provider-native 能力、精细迁移、或请求级调试，它通常比抽象层文档更直接。

</details>

<details>
<summary><b>"gold / usable / partial 怎么理解？"</b></summary>

- **gold** — 优先拿来做完整接入
- **usable** — 足够支撑大部分真实集成，建议边写边核对
- **partial** — 适合做线索入口，不适合直接生成生产代码

</details>

## 维护

相关文档：

- [validation-and-maintenance.md](references/research/validation-and-maintenance.md)
- [skill-smoke-tests.md](references/research/skill-smoke-tests.md)
- [coverage-status.md](references/research/coverage-status.md)
- [source-registry.md](references/research/source-registry.md)

---

<div align="center">

面向真实开发场景的原生 LLM API 参考与接入辅助工具

不是抽象层很重的统一 SDK

</div>
