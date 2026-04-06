# Choose the Right Recipe

Use this page when the provider may already be known but the task boundary is still fuzzy.

## Goal

Pick exactly one recipe before opening provider files or writing code.

## Fast classifier

| If the user is trying to... | Use this recipe |
|------|------|
| make one provider work for the first time | `integrate-one-provider.md` |
| move working code from provider A to provider B | `migrate-between-providers.md` |
| keep the same provider but stream partial output | `add-streaming.md` |
| let the model call local functions or external tools | `add-tool-calling.md` |
| force machine-parseable JSON or schema-shaped output | `add-structured-output.md` |
| fix `400`, `401`, `403`, `404`, `415`, `422`, or bad output shape | `debug-failed-request.md` |
| fix `429`, intermittent `5xx`, or add retry / backoff | `handle-rate-limits-and-errors.md` |

## Do not confuse these pairs

| Looks similar | Real split |
|------|------|
| debug vs retry | `400/401/422` usually means request correctness; `429/5xx` usually means retry policy |
| integrate vs migrate | brand new provider path = integrate; working old provider path being ported = migrate |
| structured output vs tool calling | user wants schema-shaped final data = structured output; user wants the model to call a function = tool calling |
| integrate vs streaming | streaming is never the first step; first get one non-stream request working |

## One-question rule

Ask at most one clarification question when the task is still ambiguous:

- provider missing -> ask which provider
- provider known but task unknown -> ask what they need to do with that provider
- provider and task both known -> do not ask; route immediately

## Ready-to-route examples

| User request | Route |
|------|------|
| "我要接入 DeepSeek API" | `integrate-one-provider.md` |
| "把 OpenAI 改成 Gemini 原生格式" | `migrate-between-providers.md` |
| "给 Claude 请求加流式输出" | `add-streaming.md` |
| "让模型调用天气函数" | `add-tool-calling.md` |
| "让模型稳定返回 JSON" | `add-structured-output.md` |
| "这个 Anthropic 请求一直 401" | `debug-failed-request.md` |
| "这个接口一直 429，帮我加退避重试" | `handle-rate-limits-and-errors.md` |

## Exit criteria

This page is complete when you can say, in one sentence:

- which single recipe applies
- whether a clarification question is still required
