# use-native-llm-apis

面向 agent 的原生 LLM API 集成 skill。

它不是一个通用 SDK，也不是“31 家厂商完全同深度”的资料堆。它真正解决的是另一个更常见、也更烦人的问题：

- 接入新模型时，总要重新查 auth header、base URL、request body
- 不同厂商接口“像又不完全像”，迁移时最容易在字段层面踩坑
- agent 很容易直接猜 provider 路径、猜兼容性、猜流式格式，然后把代码写歪

这个 skill 的价值，不在“厂商数量”本身，而在它把这些高频错误收成了一条稳定路径：

1. 先判断这个请求该不该触发 skill
2. 再选择正确任务 recipe
3. 再从 provider 索引定位到具体厂商文档
4. 必要时再看跨厂商差异
5. 最后才开始写代码

[English README](README-EN.md)

## 为什么这个 skill 值得用

如果你在做下面这些事，它通常能比“边搜边猜”更快、更稳：

- 接入某个具体厂商的原生 API
- 把 OpenAI 请求迁移到 Gemini、Anthropic、DeepSeek 等原生格式
- 给现有请求加 streaming、tool calling、structured output
- 排查 400 / 401 / 422 这类请求级错误
- 接入 OpenRouter、SiliconFlow、NewAPI、DMXAPI 这类网关或中转服务

它特别适合 agent 场景，因为它不只是给资料，还约束 agent 的工作顺序，尽量减少：

- 直接从 `SKILL.md` 猜 provider slug
- 把 OpenAI-compatible 错当成 fully compatible
- provider 还没看就开始写 wrapper
- 在 streaming / tools / JSON mode 上沿用错误心智模型

## 它到底包含什么

- 一个触发边界清楚的 skill
- 一套机械化路由：`start-here -> recipe -> providers/index -> provider file -> optional comparison -> checklist`
- 一组高频任务 recipe
- 一个覆盖 31 个 provider / gateway / relay 的参考库
- 一套维护文档、覆盖状态和 source registry

## 覆盖说明

这个仓库的内容深度不是平均分布的。当前活跃层级主要是：

- `gold`: 可以支撑比较强的端到端代码生成
- `usable`: 足够支持很多实际集成，但还不是顶级深度
- `partial`: 有公开可验证信息，但不足以承诺稳定端到端生成

旧的维护语境里可能还会出现 `skeleton` 这个保留或历史标签，但当前 live snapshot 以 [coverage-status.md](references/research/coverage-status.md) 为准。

不要把“有 31 个条目”理解成“有 31 份同质量参考”。

## 什么时候会触发这个 skill

当下面两件事同时成立时：

1. 用户明确提到了某个 provider，或者语义上已经指向 provider-native API
2. 用户要做的是代码实现，而不是价格比较、prompt 设计或泛泛的 AI 规划

典型触发例子：

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

更完整的触发和 few-shot 示例见 [prompt-patterns.md](references/recipes/prompt-patterns.md)。

## 使用路径

skill 触发后，推荐按这个顺序走：

1. 打开 [start-here.md](references/start-here.md)
2. 选一个任务 recipe
3. 从 [providers/index.md](references/providers/index.md) 找到精确 provider 文件
4. 打开对应 provider 文件
5. 只有在确实需要时才看 comparison 文件
6. 跑一遍 [routing-checklist.md](references/routing-checklist.md)
7. 再写或改代码

## 高价值 recipe

| 场景 | 入口 |
|---|---|
| 接入一个 provider | [integrate-one-provider.md](references/recipes/integrate-one-provider.md) |
| 厂商迁移 | [migrate-between-providers.md](references/recipes/migrate-between-providers.md) |
| 添加流式输出 | [add-streaming.md](references/recipes/add-streaming.md) |
| 添加工具调用 | [add-tool-calling.md](references/recipes/add-tool-calling.md) |
| 添加结构化 JSON 输出 | [add-structured-output.md](references/recipes/add-structured-output.md) |
| 排查失败请求 | [debug-failed-request.md](references/recipes/debug-failed-request.md) |

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

目录名必须保持为 `use-native-llm-apis`。安装或更新后重启 agent。

## 仓库结构

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

## 如果你要维护这个 skill

建议先看：

- [validation-and-maintenance.md](references/research/validation-and-maintenance.md)
- [skill-smoke-tests.md](references/research/skill-smoke-tests.md)
- [coverage-status.md](references/research/coverage-status.md)
- [source-registry.md](references/research/source-registry.md)

一句话总结这个 skill 的定位：

它不是“万能 LLM 接入库”，而是“让 agent 在原生 API 集成时少猜、少绕路、少写错”的工作路由器加参考库。
