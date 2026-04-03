# StepFun API

## Summary

Use StepFun's official API when integrating Step-family models directly. StepFun exposes an OpenAI-chat-completions-style interface for mainstream text generation and multimodal message inputs. This is an official vendor API, not a relay.

## Auth and Base URL

- Base URL: `https://api.stepfun.com/v1`
- Auth header: `Authorization: Bearer $STEPFUN_API_KEY`
- Content type: `application/json`

## Primary text-generation endpoint

- `POST /chat/completions`

## Minimal request

```bash
curl https://api.stepfun.com/v1/chat/completions \
  -H "Authorization: Bearer $STEPFUN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "step-1-8k",
    "messages": [
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

## Response shape

StepFun documents an OpenAI-like response envelope:

- `id`
- `object`
- `model`
- `choices`
- `choices[0].message`
- `usage`

## Streaming notes

- Enable with `"stream": true`
- Streaming is SSE-based
- Incremental chunks follow the OpenAI-style `chat.completion.chunk` pattern
- Text arrives in `choices[*].delta.content`

## Tool-calling notes

StepFun's public chat API emphasizes `messages` and multimodal content arrays. Tool-calling conventions should be treated as OpenAI-style where supported, but verify model support before assuming every Step model offers identical function-calling behavior.

## Structured-output notes

Use provider-documented JSON-oriented controls where the target model supports them. Do not rely only on prompt wording for machine-consumed output.

## Multimodal notes

StepFun explicitly documents that user `content` can be either:

- plain text
- a multipart object array

This matters because StepFun's chat API is not text-only; it is designed for mixed text, image, audio, and video message payloads on supported models.

## Common pitfalls

- Treating StepFun as a generic OpenAI relay instead of an official provider API
- Assuming every Step model has the same multimodal or tool support
- Parsing streaming chunks as full JSON responses instead of deltas

## Sources

- StepFun chat completion create: <https://platform.stepfun.com/docs/api-reference/chat/chat-completion-create>
- StepFun chat response object: <https://platform.stepfun.com/docs/en/api-reference/chat/object>
- StepFun quick start for Step Plan: <https://platform.stepfun.com/docs/zh/stepplan/quick-start>
