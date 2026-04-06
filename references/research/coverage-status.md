# Coverage Status

This file tracks current repository depth against the provider and gateway families surfaced by `cc-switch`.

Depth labels:

- `gold`: strong end-to-end reference; usually enough for direct code generation
- `usable`: enough detail for many integrations, but not yet a full native reference
- `partial`: some public signals or one access style verified, but still incomplete
- `pending`: intended for future coverage
- `blocked`: no sufficiently reliable official public docs located yet for a proper reference

Reserved or historical depth labels:

- `skeleton`: basic notes only; not enough to promise reliable code generation by themselves

## Current snapshot

Current depth distribution across entries in this file:

- `gold`: 4
- `usable`: 28
- `partial`: 2
- `pending`: 3
- `blocked`: 1

This means the repository is no longer "a few deep files plus many empty placeholders." The main remaining weak spots are concentrated rather than spread everywhere.

## Highest-priority remaining gaps

The most important non-usable entries are now:

- `CTok.ai` (`partial`): public API root and `/v1/models` are verified, but protocol docs are still too limited
- `AICodeMirror` (`partial`): public setup/tutorial docs and endpoint patterns are verified, but protocol-level evidence is still thin
- `AICoding`, `SSSAiCode`, `Micu` (`pending`): no maintained provider files yet
- `BaiLing` (`blocked`): still lacks sufficiently reliable public official docs

The practical implication:

- the strongest next wins now come from upgrading `CTok.ai` or `AICodeMirror`
- after that, the next step is deciding whether `pending` entries are worth active expansion at all

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
| NVIDIA NIM | usable | Official API and model pages now support a practical hosted NIM reference with feature caveats |
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
| Novita AI | usable | Official OpenAI-compatible docs now support a practical hosted-platform reference |
| GitHub Copilot / Copilot SDK | usable | Special OAuth / BYOK reference with real integration value |
| PackyCode | usable | Public client guides now support a practical coding-tool relay reference |
| Cubence | usable | Public setup docs now support a practical multi-client coding relay reference |
| CrazyRouter | usable | Public docs now support a practical OpenAI-compatible gateway reference with streaming guidance |
| Ai Go Code | usable | Public client guides now support a practical multi-client coding relay reference |
| AICodeMirror | partial | Public setup/tutorial docs and observable endpoint patterns exist, but protocol detail is still too thin for `usable` |
| Right Code | usable | Public curl examples make the relay's protocol families concrete enough for practical integration |
| X-Code API | usable | Public guides now support a practical multi-client coding relay reference |
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
- `README-EN.md`
- `references/research/cc-switch-provider-notes.md` when the change affects expansion planning

