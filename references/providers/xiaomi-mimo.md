# Xiaomi MiMo API Open Platform

## Summary

Use Xiaomi MiMo's official platform when integrating MiMo family models directly. Xiaomi's public docs now clearly expose both:

- OpenAI-compatible chat API
- Anthropic-compatible chat API

That makes MiMo one of the clearer examples of a vendor that officially supports multiple compatibility surfaces on the same platform.

## Auth and Documentation Entry

Official docs entry points:

- `https://platform.xiaomimimo.com/#/docs/welcome`
- `https://platform.xiaomimimo.com/llms.txt`

The `llms.txt` index confirms that Xiaomi publishes first-party docs for:

- first API call
- OpenAI API
- Anthropic API
- Codex integration
- Claude Code integration
- tool calling
- multimodal understanding
- speech synthesis

## Primary access patterns

Xiaomi MiMo officially documents two chat API styles:

- OpenAI API
- Anthropic API

This means your client choice should follow the surrounding app architecture:

- use OpenAI-compatible flows for OpenAI-style clients
- use Anthropic-compatible flows for Claude-style clients and tools

## Models and platform positioning

The public entry page describes the platform as providing access to:

- `MiMo-V2-Pro`
- `MiMo-V2-Omni`
- TTS models and related voice features

This matters because the platform is broader than simple text chat.

## Tool and multimodal support

The public docs index explicitly includes:

- web search tool calling
- image understanding
- audio understanding
- video understanding
- speech synthesis

That is strong official evidence that Xiaomi MiMo should be treated as a serious multimodal and tool-capable platform, not just a plain text-completions endpoint.

## Client integration notes

The public docs index also includes integration guides for:

- Codex
- Claude Code
- OpenCode
- OpenClaw
- Cline
- Roo Code
- Cherry Studio
- Zed
- Qwen Code

This aligns closely with the `cc-switch` preset and makes MiMo directly relevant to coding-agent workflows.

## Common pitfalls

- Assuming MiMo only supports one compatibility surface
- Treating the OpenAI-compatible and Anthropic-compatible modes as interchangeable in one client
- Ignoring modality-specific docs when moving from text chat to image, audio, or video workflows
- Assuming voice features belong to a separate product rather than the same official platform

## Sources

- Xiaomi MiMo docs route: <https://platform.xiaomimimo.com/#/docs/welcome>
- Xiaomi MiMo llms index: <https://platform.xiaomimimo.com/llms.txt>
- Xiaomi MiMo first API call: <https://platform.xiaomimimo.com/docs/quick-start/first-api-call.md>
- Xiaomi MiMo OpenAI API: <https://platform.xiaomimimo.com/docs/api/chat/openai-api.md>
- Xiaomi MiMo Anthropic API: <https://platform.xiaomimimo.com/docs/api/chat/anthropic-api.md>
- Xiaomi MiMo Codex integration: <https://platform.xiaomimimo.com/docs/integration/codex.md>
- Xiaomi MiMo Claude Code integration: <https://platform.xiaomimimo.com/docs/integration/claudecode.md>
- Xiaomi MiMo web search tool calling: <https://platform.xiaomimimo.com/docs/usage-guide/tool-calling/web-search.md>
