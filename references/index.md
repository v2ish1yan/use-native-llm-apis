# Reference Index

Use this file as the entry point for the skill.

## If you are integrating one provider

- OpenAI: [providers/openai.md](providers/openai.md)
- Anthropic: [providers/anthropic.md](providers/anthropic.md)
- Gemini: [providers/gemini.md](providers/gemini.md)
- DeepSeek: [providers/deepseek.md](providers/deepseek.md)
- Zhipu GLM: [providers/zhipu-glm.md](providers/zhipu-glm.md)
- Alibaba Bailian / DashScope: [providers/alibaba-bailian.md](providers/alibaba-bailian.md)
- Kimi / Moonshot: [providers/kimi-moonshot.md](providers/kimi-moonshot.md)
- Doubao / Volcengine Ark: [providers/doubao-volcengine-ark.md](providers/doubao-volcengine-ark.md)
- MiniMax: [providers/minimax.md](providers/minimax.md)
- StepFun: [providers/stepfun.md](providers/stepfun.md)
- Azure OpenAI: [providers/azure-openai.md](providers/azure-openai.md)
- AWS Bedrock: [providers/aws-bedrock.md](providers/aws-bedrock.md)
- NVIDIA NIM: [providers/nvidia-nim.md](providers/nvidia-nim.md)
- ModelScope API Inference: [providers/modelscope.md](providers/modelscope.md)
- OpenRouter: [providers/openrouter.md](providers/openrouter.md)
- NewAPI: [providers/newapi.md](providers/newapi.md)
- AiHubMix: [providers/aihubmix.md](providers/aihubmix.md)
- SiliconFlow: [providers/siliconflow.md](providers/siliconflow.md)
- Novita AI: [providers/novita-ai.md](providers/novita-ai.md)
- GitHub Copilot / Copilot SDK: [providers/github-copilot.md](providers/github-copilot.md)

For JavaScript or TypeScript work, start from the provider file and translate the minimal HTTP example into `fetch` code before adding app-specific wrappers.

## If you are migrating between providers

- Request and content shape differences: [comparisons/request-shape-differences.md](comparisons/request-shape-differences.md)
- Streaming differences: [comparisons/streaming-differences.md](comparisons/streaming-differences.md)
- Tool-calling differences: [comparisons/tool-calling-differences.md](comparisons/tool-calling-differences.md)
- Structured-output differences: [comparisons/structured-output-differences.md](comparisons/structured-output-differences.md)

## If you are debugging a broken request

Check these in order:

1. Provider file for auth and base URL
2. Request-shape comparison for nesting differences
3. Streaming comparison if the bug only appears in stream mode
4. Tool-calling or structured-output comparison if the failure is schema-related

For streaming bugs, also check whether the code is incorrectly parsing SSE as raw JSON lines or as another provider's delta format.

## Pilot scope

This pilot intentionally focuses on four representative providers:

- OpenAI for the current Responses-first workflow
- Anthropic for Messages API and event-stream semantics
- Gemini for `contents` and `parts` native structure
- DeepSeek for an officially OpenAI-compatible API with provider-specific caveats

Stage 2 expansion has started with:

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

## Stage 2 map

For the broader expansion path based on `cc-switch`, see [research/cc-switch-provider-notes.md](research/cc-switch-provider-notes.md).

For saved documentation URLs used during research and future refreshes, see [research/source-registry.md](research/source-registry.md).

For a live status view of what is already covered versus still pending, see [research/coverage-status.md](research/coverage-status.md).
