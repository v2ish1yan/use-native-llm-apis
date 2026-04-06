# Reference Index

Entry point for the skill's reference files.

If you are using this skill during coding work, start with [start-here.md](start-here.md).

## Recommended flow

1. open [start-here.md](start-here.md)
2. if the task is still fuzzy, open [recipes/choose-the-right-recipe.md](recipes/choose-the-right-recipe.md)
3. open exactly one task recipe
4. open [providers/index.md](providers/index.md) and click the exact provider file
5. open one comparison file only when the task requires it
6. run [routing-checklist.md](routing-checklist.md)
7. only then write or patch code

Do not guess provider file paths from memory when the provider name is available in this repo.

## By task

| Task | Recipe |
|------|--------|
| Integrate one provider | [recipes/integrate-one-provider.md](recipes/integrate-one-provider.md) |
| Migrate between providers | [recipes/migrate-between-providers.md](recipes/migrate-between-providers.md) |
| Add streaming | [recipes/add-streaming.md](recipes/add-streaming.md) |
| Add tool calling | [recipes/add-tool-calling.md](recipes/add-tool-calling.md) |
| Add structured output | [recipes/add-structured-output.md](recipes/add-structured-output.md) |
| Debug a failed request | [recipes/debug-failed-request.md](recipes/debug-failed-request.md) |
| Handle rate limits and retries | [recipes/handle-rate-limits-and-errors.md](recipes/handle-rate-limits-and-errors.md) |

## If the task is still unclear

- Start with [recipes/choose-the-right-recipe.md](recipes/choose-the-right-recipe.md)

## By provider

Need an exact provider path fast? Start from [providers/index.md](providers/index.md).

| Provider | File |
|----------|------|
| OpenAI | [providers/openai.md](providers/openai.md) |
| Anthropic (Claude) | [providers/anthropic.md](providers/anthropic.md) |
| Gemini | [providers/gemini.md](providers/gemini.md) |
| DeepSeek | [providers/deepseek.md](providers/deepseek.md) |
| Zhipu GLM | [providers/zhipu-glm.md](providers/zhipu-glm.md) |
| Alibaba Bailian / DashScope | [providers/alibaba-bailian.md](providers/alibaba-bailian.md) |
| Kimi / Moonshot | [providers/kimi-moonshot.md](providers/kimi-moonshot.md) |
| Doubao / Volcengine Ark | [providers/doubao-volcengine-ark.md](providers/doubao-volcengine-ark.md) |
| MiniMax | [providers/minimax.md](providers/minimax.md) |
| StepFun | [providers/stepfun.md](providers/stepfun.md) |
| Xiaomi MiMo | [providers/xiaomi-mimo.md](providers/xiaomi-mimo.md) |
| Azure OpenAI | [providers/azure-openai.md](providers/azure-openai.md) |
| AWS Bedrock | [providers/aws-bedrock.md](providers/aws-bedrock.md) |
| NVIDIA NIM | [providers/nvidia-nim.md](providers/nvidia-nim.md) |
| ModelScope | [providers/modelscope.md](providers/modelscope.md) |
| GitHub Copilot SDK | [providers/github-copilot.md](providers/github-copilot.md) |
| OpenRouter | [providers/openrouter.md](providers/openrouter.md) |
| SiliconFlow | [providers/siliconflow.md](providers/siliconflow.md) |
| AiHubMix | [providers/aihubmix.md](providers/aihubmix.md) |
| Novita AI | [providers/novita-ai.md](providers/novita-ai.md) |
| NewAPI | [providers/newapi.md](providers/newapi.md) |
| PackyCode | [providers/packycode.md](providers/packycode.md) |
| Cubence | [providers/cubence.md](providers/cubence.md) |
| CrazyRouter | [providers/crazyrouter.md](providers/crazyrouter.md) |
| Compshare | [providers/compshare.md](providers/compshare.md) |
| CTok.ai | [providers/ctok-ai.md](providers/ctok-ai.md) |
| Right Code | [providers/rightcode.md](providers/rightcode.md) |
| X-Code API | [providers/xcode-api.md](providers/xcode-api.md) |
| Ai Go Code | [providers/aigocode.md](providers/aigocode.md) |
| AICodeMirror | [providers/aicodemirror.md](providers/aicodemirror.md) |
| DMXAPI | [providers/dmxapi.md](providers/dmxapi.md) |

## By cross-provider topic

| Topic | File |
|-------|------|
| Request shape differences | [comparisons/request-shape-differences.md](comparisons/request-shape-differences.md) |
| Streaming differences | [comparisons/streaming-differences.md](comparisons/streaming-differences.md) |
| Tool-calling differences | [comparisons/tool-calling-differences.md](comparisons/tool-calling-differences.md) |
| Structured-output differences | [comparisons/structured-output-differences.md](comparisons/structured-output-differences.md) |

## Research and maintenance

- Start guide for maintainers: [research/validation-and-maintenance.md](research/validation-and-maintenance.md)
- Skill smoke tests: [research/skill-smoke-tests.md](research/skill-smoke-tests.md)
- Coverage maturity by provider: [research/coverage-status.md](research/coverage-status.md)
- Official doc URLs by provider: [research/source-registry.md](research/source-registry.md)
- Expansion planning notes: [research/cc-switch-provider-notes.md](research/cc-switch-provider-notes.md)
