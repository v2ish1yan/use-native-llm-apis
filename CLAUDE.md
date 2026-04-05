# use-native-llm-apis for Claude Code

## What this skill is for

Provider-native API implementation work: integrating, migrating, adding streaming, adding tool calling, adding structured output, and debugging auth or request-shape failures.

Not for: pricing research, model comparison, prompt engineering, or generic AI product design without provider-native API work.

## Quick route

1. Start at [references/start-here.md](references/start-here.md)
2. Pick exactly one task recipe
3. Resolve the exact provider file through [references/providers/index.md](references/providers/index.md)
4. Open one comparison file only when the task requires it

## File reading

Use targeted reads. Do not load the entire references tree upfront.

```text
Read: references/start-here.md
Read: references/recipes/integrate-one-provider.md
Read: references/providers/index.md
Read: references/providers/deepseek.md
```

## Code generation

- Prefer raw HTTP shape over abstraction-heavy wrappers
- Prefer native `fetch` examples unless the user asked for a specific SDK
- Make streaming examples runnable, not just descriptive
- Keep provider-specific fields visible until the request path is proven correct

## Task completion bar

A provider integration task is complete when:

1. one non-stream request path works
2. auth header and base URL are correct
3. request shape matches the provider reference
4. response parsing reads the expected output fields
5. provider-specific caveats are reflected in the delivered code

## Maintenance

- Keep trigger rules aligned with `SKILL.md`
- Keep start routing aligned with `references/start-here.md`
- Keep few-shot routing aligned with `references/recipes/prompt-patterns.md`
