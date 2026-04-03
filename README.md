# use-native-llm-apis

A Codex skill for provider-native LLM API development.

This repository packages a reusable skill that helps agents and developers work with mainstream large-model APIs without repeatedly searching vendor docs during implementation. It focuses on native HTTP request and response formats, provider-specific differences, and cross-provider migration guidance.

## What this skill is for

Use this skill when you need to:

- integrate a provider's native LLM API
- migrate code between providers
- implement streaming requests
- add tool calling or function calling
- request structured JSON output
- handle multimodal request payloads
- debug request-shape mismatches between vendors

The skill is designed for active development work, not broad market comparison.

## Current pilot coverage

Stage 1 currently includes:

- OpenAI
- Anthropic
- Gemini
- DeepSeek

Stage 2 has started with:

- Zhipu GLM
- Alibaba Bailian / DashScope
- Kimi / Moonshot
- Doubao / Volcengine Ark
- MiniMax
- StepFun
- Azure OpenAI
- AWS Bedrock
- NVIDIA NIM

It also includes comparison guides for:

- request shape differences
- streaming differences
- tool-calling differences
- structured-output differences

## Repository structure

```text
.
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
`-- references/
    |-- index.md
    |-- comparisons/
    |-- providers/
    `-- research/
```

## How to use

After installing the skill, invoke it in a prompt such as:

```text
Use $use-native-llm-apis to write an Anthropic streaming request example in TypeScript.
```

Or:

```text
Use $use-native-llm-apis to convert an OpenAI request into Gemini native format.
```

## Install locally

Copy this repository into your Codex skills directory so the folder name becomes:

```text
~/.codex/skills/use-native-llm-apis
```

On this machine, the installed path is:

```text
C:\Users\39473\.codex\skills\use-native-llm-apis
```

After installing or updating the skill, restart Codex so it reloads the skill metadata.

## Key references

- Entry point: [references/index.md](references/index.md)
- OpenAI: [references/providers/openai.md](references/providers/openai.md)
- Anthropic: [references/providers/anthropic.md](references/providers/anthropic.md)
- Gemini: [references/providers/gemini.md](references/providers/gemini.md)
- DeepSeek: [references/providers/deepseek.md](references/providers/deepseek.md)
- Zhipu GLM: [references/providers/zhipu-glm.md](references/providers/zhipu-glm.md)
- Alibaba Bailian / DashScope: [references/providers/alibaba-bailian.md](references/providers/alibaba-bailian.md)
- Kimi / Moonshot: [references/providers/kimi-moonshot.md](references/providers/kimi-moonshot.md)
- Doubao / Volcengine Ark: [references/providers/doubao-volcengine-ark.md](references/providers/doubao-volcengine-ark.md)
- MiniMax: [references/providers/minimax.md](references/providers/minimax.md)
- StepFun: [references/providers/stepfun.md](references/providers/stepfun.md)
- Azure OpenAI: [references/providers/azure-openai.md](references/providers/azure-openai.md)
- AWS Bedrock: [references/providers/aws-bedrock.md](references/providers/aws-bedrock.md)
- NVIDIA NIM: [references/providers/nvidia-nim.md](references/providers/nvidia-nim.md)
- Saved source URLs: [references/research/source-registry.md](references/research/source-registry.md)

## Project status

This repository is under active development.

The current version has already been refined through three real prompt-driven trial tasks:

- Anthropic streaming in TypeScript
- OpenAI to Gemini request migration
- DeepSeek tool-calling flow

Those trial runs were used to improve the skill's practical examples and comparison notes.

## Next development direction

Stage 2 is intended to expand toward the broader provider set surfaced by `cc-switch`, prioritizing native vendors before aggregators and relays. Likely next additions include:

- Zhipu GLM
- Alibaba Bailian / DashScope
- Kimi / Moonshot
- Doubao / Volcengine Ark
- MiniMax
- StepFun
- Azure OpenAI
- AWS Bedrock
- NVIDIA NIM

## Validation

This skill can be checked with the local validator from the Codex skill-creator toolkit:

```text
python C:\Users\39473\.codex\skills\.system\skill-creator\scripts\quick_validate.py <path-to-skill>
```

The current repository contents have already passed validation in both the project directory and the installed directory.

## Maintenance rule

When adding or updating provider coverage, save the documentation URLs used for research in [references/research/source-registry.md](references/research/source-registry.md). This keeps future refresh work fast and avoids rediscovering the same vendor docs repeatedly.
