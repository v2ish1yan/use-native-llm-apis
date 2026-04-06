# Coverage Status

This file tracks current repository depth against the provider and gateway families surfaced by `cc-switch`.

Depth labels:

- `gold`: strong end-to-end reference; usually enough for direct code generation
- `usable`: enough detail for many integrations, but not yet a full native reference
- `skeleton`: basic notes only; not enough to promise reliable code generation by themselves
- `partial`: some public signals or one access style verified, but still incomplete
- `pending`: intended for future coverage
- `blocked`: no sufficiently reliable official public docs located yet for a proper reference

## Native and official provider families

| Provider | Depth | Notes |
|---|---|---|
| OpenAI | usable | Strong enough for many integrations, but not yet a full deep-reference peer to Anthropic or Gemini |
| Anthropic | gold | Native Messages, streaming, tool use, and implementation example coverage |
| Gemini | gold | Native `contents` / `parts` reference with rich implementation detail |
| DeepSeek | gold | Deep request and streaming guidance for the official API shape in practice |
| Zhipu GLM | usable | Good request-shape coverage, but not yet a top-tier deep reference |
| Alibaba Bailian / DashScope | usable | Usable compatible-mode reference, but not full native-depth parity |
| Kimi / Moonshot | usable | Good practical coverage, but still short of top-tier depth |
| Doubao / Volcengine Ark | usable | Good practical guidance, still not a gold reference |
| MiniMax | gold | Rich provider file with advanced-feature notes |
| StepFun | usable | Solid starting reference, still thinner than core gold providers |
| Azure OpenAI | usable | Deployment-specific guidance, not a full native-provider deep reference |
| AWS Bedrock | usable | Useful deployment guidance, but not the same as a first-party native reference |
| NVIDIA NIM | skeleton | Basic auth/base-url/endpoint notes only |
| ModelScope API Inference | usable | Serviceable hosted OpenAI-compatible guidance |
| Xiaomi MiMo | usable | Good routing and API-family notes, still not a gold reference |
| BaiLing | blocked | Public official API docs not yet confirmed enough for a reliable provider reference |

## Gateway and aggregation layers

| Provider | Depth | Notes |
|---|---|---|
| OpenRouter | usable | Dedicated gateway reference with practical integration value |
| NewAPI | usable | Public docs now support a practical gateway reference across chat and responses routes |
| AiHubMix | usable | Dedicated aggregation-layer reference |
| SiliconFlow | usable | One of the stronger gateway references, including request and feature notes |
| Novita AI | skeleton | Has a file, but depth is still thin |
| GitHub Copilot / Copilot SDK | usable | Special OAuth / BYOK reference with real integration value |
| PackyCode | skeleton | Relay notes only |
| Cubence | skeleton | Relay notes only |
| CrazyRouter | skeleton | Relay notes only |
| Ai Go Code | skeleton | Relay notes only |
| AICodeMirror | skeleton | Relay/tutorial notes only |
| Right Code | usable | Public curl examples make the relay's protocol families concrete enough for practical integration |
| X-Code API | skeleton | Relay notes only |
| DMXAPI | usable | Public docs support practical guidance across chat, responses, Claude, and Gemini surfaces |
| AICoding | pending | Third-party relay |
| SSSAiCode | pending | Third-party relay |
| Compshare | usable | Public protocol docs now support a practical multi-surface gateway reference |
| Micu | pending | Third-party relay |
| CTok.ai | partial | Official API root and `/v1/models` are verified, but public protocol docs remain limited |

## Cloud and managed variants

| Provider | Depth | Notes |
|---|---|---|
| AWS Bedrock (AK/SK) | usable | Included in AWS Bedrock reference |
| AWS Bedrock (API key) | usable | Covered as Bedrock deployment style note |
| Azure OpenAI | usable | Included as separate official provider |

## Comparison file honesty

The comparison files are not 31-provider matrices.

They are strongest for the core providers they explicitly discuss:

- OpenAI
- Anthropic
- Gemini
- DeepSeek

For gateways, relays, and OpenAI-compatible services, prefer the provider file first and treat comparison docs as partial guidance.

## Maintenance rule

When a provider changes depth, also update:

- `references/providers/index.md`
- `references/research/source-registry.md`
- `README.md`
- `references/research/cc-switch-provider-notes.md` when the change affects expansion planning
