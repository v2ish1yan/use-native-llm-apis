# Provider File Selector

Use this file when you know the provider name but do not know the exact file path.

Do not guess provider slugs from memory. Open the exact file linked in the table.

## Read this first

Not every provider file in this folder is equally deep.

Use the `Depth` column:

- `gold`: strong end-to-end reference
- `usable`: enough detail for many integrations
- `skeleton`: basic notes only; expect to verify against official docs before shipping

If the provider is not in this table, return to the main task and say coverage is missing instead of inventing a path.

## How to use this page

1. Find the provider name or alias in the table.
2. Check the `Depth` column before trusting the file.
3. Open the linked file directly from the `File` column.
4. Return to the current recipe and continue with that exact file.

## Provider lookup table

| Provider | Depth | Common aliases | File |
|----------|-------|----------------|------|
| OpenAI | usable | GPT, Chat Completions, Responses API | [openai.md](openai.md) |
| Anthropic | gold | Claude, Anthropic Claude | [anthropic.md](anthropic.md) |
| Gemini | gold | Google Gemini, PaLM successor | [gemini.md](gemini.md) |
| DeepSeek | gold | DeepSeek API | [deepseek.md](deepseek.md) |
| Zhipu GLM | usable | Zhipu, BigModel, ChatGLM | [zhipu-glm.md](zhipu-glm.md) |
| Alibaba Bailian / DashScope | usable | Bailian, DashScope, Tongyi | [alibaba-bailian.md](alibaba-bailian.md) |
| Kimi / Moonshot | usable | Kimi, Moonshot AI | [kimi-moonshot.md](kimi-moonshot.md) |
| Doubao / Volcengine Ark | usable | Doubao, Ark, Volcengine | [doubao-volcengine-ark.md](doubao-volcengine-ark.md) |
| MiniMax | gold | MiniMax API | [minimax.md](minimax.md) |
| StepFun | usable | Step, StepFun API | [stepfun.md](stepfun.md) |
| Xiaomi MiMo | usable | MiMo, Xiaomi | [xiaomi-mimo.md](xiaomi-mimo.md) |
| Azure OpenAI | usable | Azure, Azure AI Foundry OpenAI | [azure-openai.md](azure-openai.md) |
| AWS Bedrock | usable | Bedrock, Amazon Bedrock | [aws-bedrock.md](aws-bedrock.md) |
| NVIDIA NIM | skeleton | NIM, NVIDIA API Catalog | [nvidia-nim.md](nvidia-nim.md) |
| ModelScope | usable | Aliyun ModelScope | [modelscope.md](modelscope.md) |
| GitHub Copilot SDK | usable | GitHub Models, Copilot | [github-copilot.md](github-copilot.md) |
| OpenRouter | usable | OpenRouter API | [openrouter.md](openrouter.md) |
| SiliconFlow | usable | Silicon Flow | [siliconflow.md](siliconflow.md) |
| AiHubMix | usable | AIHubMix | [aihubmix.md](aihubmix.md) |
| Novita AI | skeleton | Novita | [novita-ai.md](novita-ai.md) |
| NewAPI | usable | New API | [newapi.md](newapi.md) |
| PackyCode | skeleton | Packy API | [packycode.md](packycode.md) |
| Cubence | skeleton | Cubence API | [cubence.md](cubence.md) |
| CrazyRouter | skeleton | Crazy Router | [crazyrouter.md](crazyrouter.md) |
| Compshare | usable | Compshare API, ModelVerse | [compshare.md](compshare.md) |
| CTok.ai | skeleton | CTok | [ctok-ai.md](ctok-ai.md) |
| Right Code | usable | RightCode, Right Codes | [rightcode.md](rightcode.md) |
| X-Code API | skeleton | XCode, X-Code | [xcode-api.md](xcode-api.md) |
| Ai Go Code | skeleton | AIGoCode, AI Go Code | [aigocode.md](aigocode.md) |
| AICodeMirror | skeleton | AI Code Mirror | [aicodemirror.md](aicodemirror.md) |
| DMXAPI | usable | DMX API | [dmxapi.md](dmxapi.md) |

## Notes

- This page exists to remove path guessing from recipes and task routing.
- `references/index.md` remains the top-level entry for task selection and cross-provider comparisons.
- Comparison files are strongest for the core providers they explicitly discuss. Do not treat them as full 31-provider matrices.
