# use-native-llm-apis for Claude Code

## What this skill is for

Provider-native API implementation work: integrating, migrating, adding streaming/tool-calling/structured-output, debugging auth/request-shape failures.

Not for: model comparison, pricing research, prompt engineering, generic AI product design without provider API work.

## Quick route

1. Check trigger applicability → [references/recipes/prompt-patterns.md](references/recipes/prompt-patterns.md)
2. Pick a task recipe → `references/recipes/`
3. Load the target provider → `references/providers/`
4. Load a comparison file → `references/comparisons/` (only when migrating or extending)

## File reading

Use targeted reads — do not load the entire references directory upfront:

```text
Read: references/recipes/integrate-one-provider.md
Read: references/providers/deepseek.md
Read: references/comparisons/streaming-differences.md
```

## Code generation

- Prefer raw HTTP shape over abstraction-heavy wrappers
- Prefer native `fetch` examples unless the user asked for a specific SDK
- Make streaming examples runnable, not just descriptive
- Keep provider-specific fields visible until the request path is proven correct

## Task completion bar

A provider integration task is complete when:

1. One non-stream request path works
2. Auth header and base URL are correct
3. Request shape matches the provider reference
4. Response parsing reads the expected output fields
5. Provider-specific caveats are reflected in the delivered code

## Coverage claims

Before claiming a provider is covered, verify in [coverage-status.md](references/research/coverage-status.md).

Before claiming a detail is current, verify in [source-registry.md](references/research/source-registry.md).

## Maintenance

- Keep trigger rules aligned with `SKILL.md`
- Keep routing examples aligned with `references/recipes/prompt-patterns.md`
- Prefer narrowing ambiguous routes over broadening triggers
