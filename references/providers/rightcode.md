# Right Code Relay

## Summary

Use Right Code when the project needs a coding-tool-oriented relay that standardizes access to Claude Code, Codex, Gemini CLI, and related agent workflows. Right Code is a distribution and relay platform, not a native model vendor.

## Auth and Base URL

Right Code's docs emphasize:

- one API key
- multiple AI agent integrations

The docs also expose direct curl examples that show provider-specific request headers and standardized relay usage.

## Primary access pattern

Right Code is documented as:

- one API key
- standardized interface
- multiple agent clients and integration modes

It supports configuration guidance for:

- CLI tools
- SDKs
- IDE extensions

## Practical notes

Because Right Code exposes both API examples and tool-specific setup guides, it is more documented than many relay platforms. That makes it reasonable to maintain a dedicated reference in this skill.

## Common pitfalls

- Treating Right Code as a native provider rather than a relay layer
- Assuming one request shape across all integrated upstream providers
- Forgetting that some examples are provider-specific even though the platform key is unified

## Sources

- Right Code docs home: <https://docs.right.codes/>
- Right Code intro: <https://docs.right.codes/docs/rc_quick_start/intro>
- Right Code curl examples: <https://docs.right.codes/docs/rc_extension/curl>
- Right Code OpenCode configuration: <https://docs.right.codes/docs/rc_extension/opencode>
