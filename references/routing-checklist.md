# Routing Checklist

Run this checklist before writing or patching code.

- I picked exactly one task recipe.
- I used [recipes/choose-the-right-recipe.md](recipes/choose-the-right-recipe.md) if the task was ambiguous.
- I opened the provider file from [providers/index.md](providers/index.md), not from memory.
- I only opened a comparison file if the task really needs one.
- The provider is known.
- The task is known.
- If the main symptom is `429` or intermittent `5xx`, I am using the retry recipe rather than the request-shape debug recipe.
- If the main symptom is `400`, `401`, or `422`, I am checking request correctness before adding retries.
- I am doing implementation work, not market comparison or prompt writing.

If any line is false, stop and fix routing before coding.
