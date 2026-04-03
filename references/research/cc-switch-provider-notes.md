# CC Switch Provider Notes

This note is not the user-facing quick reference. It is a coverage map for expanding this skill toward all providers surfaced by `cc-switch`.

## What was inspected

- `src/config/claudeProviderPresets.ts`
- `src/config/codexProviderPresets.ts`
- `src/config/geminiProviderPresets.ts`
- `src/config/universalProviderPresets.ts`

## Pilot providers

Stage 1 intentionally covers:

- OpenAI
- Anthropic
- Gemini
- DeepSeek

These four providers are enough to validate the skill structure across:

- Responses-style APIs
- Messages-style APIs
- `contents` and `parts` APIs
- officially OpenAI-compatible but provider-specific APIs

## Native and official vendor families visible in cc-switch

The local `cc-switch` presets surface these direct vendor or cloud-provider families that matter for Stage 2 native coverage:

- OpenAI
- Anthropic / Claude
- Google Gemini
- DeepSeek
- Azure OpenAI
- AWS Bedrock
- Zhipu GLM / Z.ai
- Alibaba Bailian / DashScope
- Moonshot Kimi
- StepFun
- MiniMax
- DouBao / Volcengine Ark
- Baidu Wenxin family
- Xiaomi MiMo
- Nvidia

Some names show up as vendor-native endpoints for one app while others appear as provider-specific compatibility adapters for Claude Code, Codex, or Gemini CLI.

## Gateway and relay families visible in cc-switch

`cc-switch` also includes many non-native gateways, aggregators, and relays. These matter for future compatibility notes, but they should not replace native provider docs in this skill:

- NewAPI
- OpenRouter
- AiHubMix
- SiliconFlow
- DMXAPI
- PackyCode
- Cubence
- AIGoCode
- RightCode
- AICodeMirror
- AICoding
- CrazyRouter
- SSSAiCode
- Compshare
- Micu
- X-Code API
- CTok.ai
- ModelScope
- Novita AI

## Useful implementation clues from cc-switch

- `Claude` presets distinguish protocol families with `apiFormat`, including `anthropic`, `openai_chat`, and `openai_responses`.
- `Codex` presets consistently use `wire_api = "responses"` for OpenAI-style backends.
- `Gemini` presets use base URLs that map to Gemini-native endpoints or relay-specific Gemini front doors.
- `UniversalProviderPresets` show that `cc-switch` treats NewAPI and custom gateways as cross-protocol routers rather than native providers.

These patterns confirm that the skill should keep native provider docs separate from gateway docs.

## Stage 2 recommendation

Expand in this order:

1. Native first-party APIs
2. Cloud-provider native wrappers with distinct auth or URL rules
3. Major Chinese vendor-native APIs
4. Aggregators and relays only after the native layer is solid

Current Stage 2 in progress:

- Zhipu GLM
- Alibaba Bailian / DashScope
- Kimi / Moonshot
- Doubao / Volcengine Ark

## Primary sources for the pilot

- OpenAI docs: <https://platform.openai.com/docs/>
- Anthropic docs: <https://docs.anthropic.com/>
- Gemini docs: <https://ai.google.dev/gemini-api/docs>
- DeepSeek docs: <https://api-docs.deepseek.com/>
