# use-native-llm-apis

一个专门给编码助手用的原生 LLM API 集成 skill。

它的目标很简单：当你在项目里接入大模型 API 时，不用再反复去网上翻文档、对 header、猜 request body、试 streaming 格式，而是直接获得一套更稳定的参考和使用入口。

[English README](README-EN.md)

## 这个 skill 能做什么

它主要帮助你处理这些高频场景：

- 接入某个厂商的原生 LLM API
- 把 OpenAI 请求迁移到 Gemini、Anthropic、DeepSeek 等原生格式
- 给现有请求加 streaming
- 给模型请求加 tool calling
- 让模型返回结构化 JSON
- 排查 400 / 401 / 422 这类请求级错误
- 处理 429 / 5xx、退避重试、`Retry-After` 这类稳定性问题
- 接入 OpenRouter、SiliconFlow、NewAPI、DMXAPI 这类网关或中转服务

一句话说，它解决的不是“有没有 API”，而是“不同 API 的细节总是不一样，而且总在最烦的地方不一样”。

## 为什么值得装

如果你经常写和大模型接口相关的代码，这个 skill 能帮你少掉很多重复劳动：

- 少查：不用每次都重新找 auth header、base URL、endpoint
- 少猜：不用靠记忆硬猜 request shape、streaming 格式、工具调用字段
- 少试错：迁移厂商时，能更快发现差异点
- 少返工：避免代码先写完，才发现字段路径或鉴权方式错了

它特别适合这些需求：

- “我要接入 DeepSeek API”
- “帮我把 OpenAI 改成 Gemini 原生格式”
- “给 Claude 请求加流式输出”
- “帮我排查这个 401”
- “我要接入某个 OpenAI-compatible 平台，但不确定兼容到什么程度”

## 覆盖范围

这个仓库当前覆盖 31 个 provider / gateway / relay 条目：

| 类别 | 覆盖项 |
|---|---|
| 原生 LLM 厂商 | OpenAI, Anthropic, Gemini, DeepSeek, 智谱, 百炼, Kimi, 豆包, MiniMax, StepFun, 小米 MiMo |
| 云与托管平台 | Azure OpenAI, AWS Bedrock, NVIDIA NIM, ModelScope, GitHub Copilot SDK |
| 网关与聚合层 | OpenRouter, SiliconFlow, AiHubMix, Novita AI, NewAPI |
| 中转与代理服务 | PackyCode, Cubence, CrazyRouter, Compshare, CTok.ai, Right Code, X-Code API, Ai Go Code, AICodeMirror, DMXAPI |

但这里要说清楚：

这不是 31 家完全同深度的“满血参考库”。

当前内容深度分为：

- `gold`：足够强的端到端参考
- `usable`：能支持很多实际集成
- `partial`：有公开可验证信息，但还不够深

最新覆盖状态看这里：

- [coverage-status.md](references/research/coverage-status.md)

## 适合怎么用

最典型的用法不是“手动翻仓库”，而是直接在你的开发请求里说清楚你要做什么。

例如：

```text
我要接入 DeepSeek API
```

```text
帮我把 OpenAI 请求改成 Gemini 原生格式
```

```text
Use $use-native-llm-apis to write an Anthropic streaming request in TypeScript.
```

```text
这个 Claude 请求一直 401，帮我排查一下
```

更多示例可以看：

- [prompt-patterns.md](references/recipes/prompt-patterns.md)

## 你能从这个 skill 里得到什么

安装后，你拿到的不是一个 SDK，而是一组高价值参考：

- 常见厂商的请求格式说明
- auth header / base URL / endpoint 线索
- streaming、tool calling、structured output 的差异说明
- 厂商迁移时的重点映射
- 调试失败请求时的排查思路
- rate limit、重试退避、错误响应排查模板

如果你想继续深入看参考内容，可以看：

- [providers/index.md](references/providers/index.md)
- [request-shape-differences.md](references/comparisons/request-shape-differences.md)
- [streaming-differences.md](references/comparisons/streaming-differences.md)
- [tool-calling-differences.md](references/comparisons/tool-calling-differences.md)
- [structured-output-differences.md](references/comparisons/structured-output-differences.md)

## FAQ

### 既然很多平台都说自己 OpenAI-compatible，为什么还需要这个 skill？

因为“路径兼容”不等于“行为兼容”。

很多平台虽然能接受类似的 `/v1` 请求，但在这些地方仍然可能不同：

- 鉴权 header
- 流式输出格式
- tool calling 字段
- structured output 支持方式
- 响应字段路径

真正让代码出错的，通常不是“完全不会用”，而是“看起来差不多，但差在最关键的一两个字段上”。

### 它和统一 SDK / 抽象层有什么区别？

统一 SDK 解决的是“用同一套接口调用多个厂商”。

这个 skill 解决的是“当你必须面对原生接口细节时，怎么少踩坑、少返工、少猜协议”。

如果你的项目本来就需要 provider-native 能力、精细迁移、或请求级调试，它通常比抽象层文档更直接。

### 我应该怎么理解 `gold` / `usable` / `partial`？

- `gold`：可以优先拿来直接支撑更完整的接入实现
- `usable`：足够支持很多真实集成，但最好边写边核对
- `partial`：更适合做线索入口，不适合盲目生成完整生产代码

## 安装

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

更新：

```powershell
git -C "$HOME\.codex\skills\use-native-llm-apis" pull
git -C "$HOME\.claude\skills\use-native-llm-apis" pull
```

目录名必须保持为 `use-native-llm-apis`。安装或更新后重启工具。

## 维护与更新

如果你要维护这个 skill，建议先看：

- [validation-and-maintenance.md](references/research/validation-and-maintenance.md)
- [skill-smoke-tests.md](references/research/skill-smoke-tests.md)
- [coverage-status.md](references/research/coverage-status.md)
- [source-registry.md](references/research/source-registry.md)

这个 skill 最适合被理解成：

一个面向真实开发场景的原生 LLM API 参考与接入辅助工具，而不是一个抽象层很重的统一 SDK。
