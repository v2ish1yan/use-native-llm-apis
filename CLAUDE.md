# use-native-llm-apis for Claude Code

## What this skill is for

Provider-native API implementation work: integrating, migrating, adding streaming, adding tool calling, adding structured output, and debugging auth or request-shape failures.

Not for: model comparison, pricing research, prompt engineering, or generic AI product design that does not require provider-native API work.

## Quick route

1. Check trigger applicability in [references/recipes/prompt-patterns.md](references/recipes/prompt-patterns.md)
2. Pick a task recipe in `references/recipes/`
3. Resolve the exact provider file through [references/providers/index.md](references/providers/index.md)
4. Load a comparison file from `references/comparisons/` only when migrating or extending behavior

## File reading

Use targeted reads. Do not load the entire references directory upfront.

```text
Read: references/recipes/integrate-one-provider.md
Read: references/providers/index.md
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
