# Claude Code Plugin: llm-apis

Provider-native LLM API integration skill for Claude Code.

## Installation

### Direct GitHub Install (Recommended)

```
/plugin install llm-apis@github:v2ish1yan/use-native-llm-apis
```

### From Marketplace

```
/plugin marketplace add v2ish1yan/use-native-llm-apis
/plugin install llm-apis@native-llm-apis-marketplace
```

## Usage

Once installed, this skill automatically activates when you:

- Ask to integrate a provider's native LLM API
- Request migration between providers (e.g., OpenAI → Gemini)
- Need to add streaming, tool calling, or structured output
- Want to debug API errors (400, 401, 422, 429, 5xx)

### Example Prompts

```
我要接入 DeepSeek API
```

```
Convert this OpenAI request to Gemini native format
```

```
Add streaming to my Claude request
```

```
Debug why this request keeps returning 401
```

## Covered Providers

**Native LLM Providers**: OpenAI, Anthropic, Gemini, DeepSeek, Zhipu, Bailian, Kimi, Doubao, MiniMax, StepFun, Xiaomi MiMo

**Cloud Platforms**: Azure OpenAI, AWS Bedrock, NVIDIA NIM, ModelScope, GitHub Copilot SDK

**Gateways**: OpenRouter, SiliconFlow, AiHubMix, Novita AI, NewAPI

**Relays**: PackyCode, Cubence, CrazyRouter, Compshare, CTok.ai, Right Code, X-Code API, Ai Go Code, AICodeMirror, DMXAPI

## Documentation

- [Start Here](../references/start-here.md)
- [Provider Index](../references/providers/index.md)
- [Coverage Status](../references/research/coverage-status.md)
