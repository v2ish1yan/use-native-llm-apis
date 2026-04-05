# use-native-llm-apis

A Codex skill for provider-native LLM API development.

This repository helps agents and developers integrate mainstream model APIs without repeatedly re-searching vendor docs during implementation. It focuses on raw request and response shapes, auth, base URLs, provider differences, and migration work between vendors.

## Why this exists

Most LLM integration work gets slowed down by the same problems:

- forgetting each provider's exact request shape
- mixing native APIs with OpenAI-compatible assumptions
- breaking streaming or tool-calling when switching providers
- repeatedly searching official docs for the same auth and endpoint details

This skill packages those answers into a workflow that is faster to use during real coding work.

## What this skill is for

Use this skill when you need to:

- integrate a provider-native LLM API
- migrate code between providers
- add streaming support
- add tool calling or function calling
- add structured JSON output
- handle multimodal request payloads
- debug request-shape mismatches, auth failures, or wrong endpoint usage

This skill is for implementation work, not broad market comparison.

## Start here

If you only remember one rule, remember this one:

**Start from the task recipe, not from the full provider list.**

Open [references/index.md](references/index.md), then use this path:

1. Decide whether this skill applies.
2. Start from the matching recipe in `references/recipes/`.
3. Open the target provider file.
4. Open a comparison file if you are migrating or adding advanced behavior.
5. Only go back to the web when the bundled references are missing a time-sensitive detail.

## Common usage paths

| Task | Open first |
|---|---|
| Decide whether this skill should trigger | [references/recipes/prompt-patterns.md](references/recipes/prompt-patterns.md) |
| Integrate one provider | [references/recipes/integrate-one-provider.md](references/recipes/integrate-one-provider.md) |
| Migrate between providers | [references/recipes/migrate-between-providers.md](references/recipes/migrate-between-providers.md) |
| Add streaming | [references/recipes/add-streaming.md](references/recipes/add-streaming.md) |
| Add tool calling | [references/recipes/add-tool-calling.md](references/recipes/add-tool-calling.md) |
| Add structured output | [references/recipes/add-structured-output.md](references/recipes/add-structured-output.md) |
| Debug a failed request | [references/recipes/debug-failed-request.md](references/recipes/debug-failed-request.md) |

## Prompts that should trigger this skill

Typical requests that should cause an agent to load this skill:

- "`wo yao jie ru deepseek da mo xing api`"
- "`bang wo dui jie Anthropic api`"
- "`zhe ge xiang mu yao diao yong OpenAI API`"
- "`ba OpenAI gai cheng Gemini yuan sheng ge shi`"
- "`gei zhe ge xiang mu jia liu shi shu chu`"
- "`bang wo jie gong ju diao yong`"
- "`rang mo xing fan hui jie gou hua JSON`"
- "`pai cha zhe ge mo xing jie kou wei shen me 400/401`"

More trigger examples and few-shot routing notes live in [references/recipes/prompt-patterns.md](references/recipes/prompt-patterns.md).

## Example prompts

```text
Use $use-native-llm-apis to write an Anthropic streaming request example in TypeScript.
```

```text
Use $use-native-llm-apis to convert an OpenAI request into Gemini native format.
```

```text
Use $use-native-llm-apis to add streaming to an existing Anthropic fetch client.
```

```text
Use $use-native-llm-apis to debug why this Gemini request returns 400.
```

```text
Use $use-native-llm-apis to port this OpenAI tool-calling flow to DeepSeek.
```

## Coverage at a glance

### Stage 1 pilot providers

- OpenAI
- Anthropic
- Gemini
- DeepSeek

### Stage 2 expanded providers and gateways

- Zhipu GLM
- Alibaba Bailian / DashScope
- Kimi / Moonshot
- Doubao / Volcengine Ark
- MiniMax
- StepFun
- Azure OpenAI
- AWS Bedrock
- NVIDIA NIM
- ModelScope API Inference
- OpenRouter
- NewAPI
- AiHubMix
- SiliconFlow
- Novita AI
- GitHub Copilot / Copilot SDK
- PackyCode
- Cubence
- CrazyRouter
- Xiaomi MiMo
- Compshare
- CTok.ai
- Right Code
- X-Code API
- Ai Go Code
- AICodeMirror
- DMXAPI

### Cross-provider comparison guides

- request shape differences
- streaming differences
- tool-calling differences
- structured-output differences

For live coverage status, see [references/research/coverage-status.md](references/research/coverage-status.md).

## Repository structure

```text
.
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
`-- references/
    |-- index.md
    |-- recipes/
    |-- comparisons/
    |-- providers/
    `-- research/
```

## Key references

### Entry points

- [references/index.md](references/index.md)
- [references/recipes](references/recipes)
- [references/research/source-registry.md](references/research/source-registry.md)
- [references/research/coverage-status.md](references/research/coverage-status.md)

### Core native providers

- [references/providers/openai.md](references/providers/openai.md)
- [references/providers/anthropic.md](references/providers/anthropic.md)
- [references/providers/gemini.md](references/providers/gemini.md)
- [references/providers/deepseek.md](references/providers/deepseek.md)

### Additional providers and gateways

- [references/providers/zhipu-glm.md](references/providers/zhipu-glm.md)
- [references/providers/alibaba-bailian.md](references/providers/alibaba-bailian.md)
- [references/providers/kimi-moonshot.md](references/providers/kimi-moonshot.md)
- [references/providers/doubao-volcengine-ark.md](references/providers/doubao-volcengine-ark.md)
- [references/providers/minimax.md](references/providers/minimax.md)
- [references/providers/stepfun.md](references/providers/stepfun.md)
- [references/providers/azure-openai.md](references/providers/azure-openai.md)
- [references/providers/aws-bedrock.md](references/providers/aws-bedrock.md)
- [references/providers/nvidia-nim.md](references/providers/nvidia-nim.md)
- [references/providers/modelscope.md](references/providers/modelscope.md)
- [references/providers/openrouter.md](references/providers/openrouter.md)
- [references/providers/newapi.md](references/providers/newapi.md)
- [references/providers/aihubmix.md](references/providers/aihubmix.md)
- [references/providers/siliconflow.md](references/providers/siliconflow.md)
- [references/providers/novita-ai.md](references/providers/novita-ai.md)
- [references/providers/github-copilot.md](references/providers/github-copilot.md)
- [references/providers/packycode.md](references/providers/packycode.md)
- [references/providers/cubence.md](references/providers/cubence.md)
- [references/providers/crazyrouter.md](references/providers/crazyrouter.md)
- [references/providers/xiaomi-mimo.md](references/providers/xiaomi-mimo.md)
- [references/providers/compshare.md](references/providers/compshare.md)
- [references/providers/ctok-ai.md](references/providers/ctok-ai.md)
- [references/providers/rightcode.md](references/providers/rightcode.md)
- [references/providers/xcode-api.md](references/providers/xcode-api.md)
- [references/providers/aigocode.md](references/providers/aigocode.md)
- [references/providers/aicodemirror.md](references/providers/aicodemirror.md)
- [references/providers/dmxapi.md](references/providers/dmxapi.md)

## Install in Codex

Codex discovers personal skills from your local skills directory. For this skill to load correctly, the final folder name must be exactly:

```text
use-native-llm-apis
```

The target install path is:

```text
~/.codex/skills/use-native-llm-apis
```

On this machine, that path is:

```text
C:\Users\39473\.codex\skills\use-native-llm-apis
```

### Method 1: install from the current local repository

Use this when you already have the repo on disk and want to copy it into Codex.

PowerShell:

```powershell
$source = "E:\AI\SKILL\use-api\use-native-llm-apis-repo"
$target = "$HOME\.codex\skills\use-native-llm-apis"

New-Item -ItemType Directory -Force -Path "$HOME\.codex\skills" | Out-Null
Remove-Item -Recurse -Force $target -ErrorAction SilentlyContinue
Copy-Item -Recurse -Force $source $target
```

### Method 2: clone directly into the Codex skills directory

Use this when installing on a new machine.

PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.codex\skills" | Out-Null
git clone https://github.com/v2ish1yan/use-native-llm-apis.git "$HOME\.codex\skills\use-native-llm-apis"
```

### Method 3: update an existing installation

If the skill is already installed and that folder is a git clone:

```powershell
git -C "$HOME\.codex\skills\use-native-llm-apis" pull
```

If the installed folder is only a copied snapshot, overwrite it again with Method 1.

### Restart Codex

After installing or updating the skill, restart Codex so it reloads skill metadata and file contents.

### Verify the install

1. Confirm that `SKILL.md` exists at `~/.codex/skills/use-native-llm-apis/SKILL.md`.
2. Restart Codex.
3. In a new prompt, try:

```text
Use $use-native-llm-apis to write a DeepSeek chat request example in TypeScript.
```

If Codex can load the skill, it should route through this repository's recipes and provider references instead of treating it like a generic coding request.

### Common install mistakes

- The folder name is wrong, such as `use-native-llm-apis-repo` instead of `use-native-llm-apis`.
- The repo was copied one level too deep, producing `~/.codex/skills/use-native-llm-apis/use-native-llm-apis-repo/SKILL.md`.
- Codex was not restarted after copying files.
- The installed copy is outdated while the repo version has newer docs.

## Validation

Validate the skill with:

```text
python C:\Users\39473\.codex\skills\.system\skill-creator\scripts\quick_validate.py <path-to-skill>
```

The repository version and the installed version have both been validated during development.

## Maintenance rules

- Save official documentation URLs in [references/research/source-registry.md](references/research/source-registry.md) whenever coverage is added or revised.
- Track provider status in [references/research/coverage-status.md](references/research/coverage-status.md).
- Prefer official provider docs over blogs or third-party tutorials when updating the skill.
- Do not add new provider claims from memory alone.

## Project status

This repository is under active development and has already been refined through real prompt-driven trial tasks, including:

- Anthropic streaming in TypeScript
- OpenAI to Gemini request migration
- DeepSeek tool-calling flow

Those trial runs were used to improve the skill's practical guidance and comparison notes.
