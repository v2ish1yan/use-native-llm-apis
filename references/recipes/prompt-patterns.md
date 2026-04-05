# Prompt Patterns and Few-Shot Triggers

Use this file when the goal is to recognize that a user is asking for provider-native LLM API integration work, even if they do not explicitly mention this skill.

## Trigger rule

This skill should be loaded when the user is clearly asking to:

- access a large-model API
- integrate or connect a provider API
- switch one model provider to another
- add streaming, tool calling, multimodal input, or structured output to an LLM request
- debug a broken model API request

If the user's request is about using a model API in code, assume this skill is relevant unless the task is clearly only product comparison or pricing research.

## Real user phrasing that should trigger this skill

- "`wo yao jie ru deepseek da mo xing api`"
- "`bang wo jie yi xia Anthropic api`"
- "`zhe ge xiang mu yao yong OpenAI API`"
- "`ba xian zai de OpenAI qing qiu gai cheng Gemini yuan sheng ge shi`"
- "`wo yao zai cha jian li jie ru Claude API`"
- "`gei zhe ge xiang mu jia da mo xing liu shi shu chu`"
- "`bang wo ba gong ju diao yong jie shang`"
- "`wo yao rang mo xing fan hui jie gou hua JSON`"
- "`zhe ge mo xing jie kou wei shen me yi zhi 400`"
- "`bang wo pai cha 401, shi bu shi jian quan ge shi cuo le`"
- "`wo yao ba xian zai de LLM jie kou cong OpenAI qie dao DeepSeek`"
- "`xiang mu li xu yao jie da mo xing jie kou`"
- "`zhe li xu yao diao yong mo xing API`"
- "`jie ru duo mo tai mo xing jie kou`"
- "`xie yi ge DeepSeek de fetch qing qiu`"

## Equivalent English phrasing

- "I need to integrate the DeepSeek API"
- "Hook up Anthropic in this project"
- "Convert this OpenAI request to Gemini native format"
- "Add streaming to our LLM client"
- "Wire tool calling into this model request"
- "Make the model return structured JSON"
- "Debug why this provider request is returning 400"
- "Switch this project from OpenAI to DeepSeek"

## Few-shot routing examples

### Example 1

User:

> `wo yao jie ru deepseek da mo xing api`

Correct interpretation:

- This is a provider-native integration task.
- Start with `references/recipes/integrate-one-provider.md`.
- Then open `references/providers/deepseek.md`.

### Example 2

User:

> `ba xian zai de OpenAI jie kou gai cheng Gemini yuan sheng ge shi`

Correct interpretation:

- This is a provider migration task.
- Start with `references/recipes/migrate-between-providers.md`.
- Then open `references/providers/openai.md`, `references/providers/gemini.md`, and `references/comparisons/request-shape-differences.md`.

### Example 3

User:

> `gei zhe ge xiang mu jia Claude liu shi shu chu`

Correct interpretation:

- This is a streaming task for one provider.
- Start with `references/recipes/add-streaming.md`.
- Then open `references/providers/anthropic.md` and `references/comparisons/streaming-differences.md`.

### Example 4

User:

> `rang mo xing diao yong ben di han shu cha tian qi`

Correct interpretation:

- This is a tool-calling task.
- Start with `references/recipes/add-tool-calling.md`.
- Then open the target provider file and `references/comparisons/tool-calling-differences.md`.

### Example 5

User:

> `zhe ge DeepSeek qing qiu yi zhi bao 401`

Correct interpretation:

- This is a request-debugging task.
- Start with `references/recipes/debug-failed-request.md`.
- Then open `references/providers/deepseek.md`.

## Non-trigger examples

These requests do not automatically require this skill:

- "`na ge da mo xing geng pian yi`"
- "`bang wo bi jiao yi xia OpenAI he Gemini na ge geng qiang`"
- "`zui jin you na xie da mo xing fa bu le`"

Those are research or recommendation tasks unless the user also asks to implement code against the API.

## Simple detection heuristic

If the request contains both:

1. a provider or model API idea such as `OpenAI`, `Anthropic`, `Claude`, `Gemini`, `DeepSeek`, `LLM API`, `large-model API`, `model API`
2. an implementation verb such as `jie ru`, `dui jie`, `diao yong`, `ji cheng`, `qian yi`, `gai zao`, `jia shang`, `debug`, `pai cha`

then this skill should usually be loaded.
