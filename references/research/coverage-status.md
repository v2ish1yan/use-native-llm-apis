# Coverage Status

This file tracks current repository coverage against the provider and gateway families surfaced by `cc-switch`.

Status labels:

- `covered`: provider or gateway has a dedicated reference file
- `partial`: covered indirectly or only through one access style
- `pending`: intended for future coverage
- `blocked`: no sufficiently reliable official public docs located yet for a proper reference

## Native and official provider families

| Provider | Status | Notes |
|---|---|---|
| OpenAI | covered | Native Responses-focused reference |
| Anthropic | covered | Native Messages and streaming reference |
| Gemini | covered | Native `contents` / `parts` reference |
| DeepSeek | covered | Official OpenAI-compatible chat reference |
| Zhipu GLM | covered | Official BigModel chat-completions-style reference |
| Alibaba Bailian / DashScope | covered | Official compatible-mode reference |
| Kimi / Moonshot | covered | Official chat, streaming, tools, JSON mode docs |
| Doubao / Volcengine Ark | covered | Official Responses and compatibility docs |
| MiniMax | covered | Official Anthropic/OpenAI-compatible docs |
| StepFun | covered | Official chat-completions-style docs |
| Azure OpenAI | covered | Official Azure v1 Responses guidance |
| AWS Bedrock | covered | Official Claude Messages on Bedrock guidance |
| NVIDIA NIM | covered | Official hosted LLM API reference |
| ModelScope API Inference | covered | Official hosted OpenAI-compatible inference |
| Xiaomi MiMo | covered | Official docs route and llms index confirmed, including OpenAI and Anthropic API references |
| BaiLing | blocked | Public official API docs not yet confirmed enough for a reliable provider reference |

## Gateway and aggregation layers

| Provider | Status | Notes |
|---|---|---|
| OpenRouter | covered | Dedicated gateway reference |
| NewAPI | covered | Dedicated gateway reference |
| AiHubMix | covered | Dedicated aggregation-layer reference |
| SiliconFlow | covered | Dedicated hosted aggregation-layer reference |
| Novita AI | covered | Dedicated aggregation-layer reference |
| GitHub Copilot / Copilot SDK | covered | Special OAuth / BYOK reference |
| PackyCode | covered | Dedicated relay reference with docs site |
| Cubence | covered | Dedicated relay reference |
| CrazyRouter | covered | Dedicated relay reference |
| Ai Go Code | covered | Dedicated relay reference with docs center |
| AICodeMirror | covered | Dedicated relay reference with public tutorial docs |
| Right Code | covered | Dedicated relay reference with docs and curl examples |
| X-Code API | covered | Dedicated relay reference with docs site |
| DMXAPI | covered | Dedicated relay reference with docs site |
| AICoding | pending | Third-party relay |
| SSSAiCode | pending | Third-party relay |
| Compshare | covered | Official Compshare / ModelVerse docs expose OpenAI, Responses, Anthropic, and Gemini protocol entries |
| Micu | pending | Third-party relay |
| CTok.ai | pending | Third-party relay |

## Cloud and managed variants

| Provider | Status | Notes |
|---|---|---|
| AWS Bedrock (AK/SK) | covered | Included in AWS Bedrock reference |
| AWS Bedrock (API key) | covered | Covered as Bedrock deployment style note |
| Azure OpenAI | covered | Included as separate official provider |

## Maintenance rule

When a provider moves from `pending` or `blocked` to `covered`, also update:

- `references/index.md`
- `references/research/source-registry.md`
- `README.md`
- `references/research/cc-switch-provider-notes.md` when the change affects expansion planning
