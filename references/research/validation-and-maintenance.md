# Validation and Maintenance

Use this file when updating the skill itself, not when using provider references during application development.

## Maintenance goals

Keep five things healthy:

1. trigger boundaries stay precise
2. routing stays mechanical
3. provider status stays honest
4. validation stays runnable on the maintainer's machine
5. ambiguous prompts do not silently route down the wrong path

## Single-source rules

- `SKILL.md` defines when the skill should load and how the top-level execution protocol works.
- `references/start-here.md` defines the first routing path after the skill loads.
- `references/recipes/choose-the-right-recipe.md` is the task disambiguation page when provider or task language is fuzzy.
- `references/routing-checklist.md` defines the final pre-coding self-check.
- `references/recipes/prompt-patterns.md` gives trigger examples and few-shot routing examples.
- `README.md` is the Chinese human-facing entry document and should not become a second source of trigger truth.
- `README-EN.md` is the English human-facing companion and should stay aligned with `README.md`.
- `references/research/coverage-status.md` is the source of truth for depth labels such as `gold`, `usable`, `skeleton`, `partial`, `pending`, and `blocked`.

## Update checklist

When changing the skill itself:

1. Decide whether the change affects trigger rules, routing, or maintainer workflow.
2. Update `SKILL.md` first if trigger boundaries or execution protocol changed.
3. Update `references/start-here.md` if the first routing path changed.
4. Update `references/recipes/choose-the-right-recipe.md` if task disambiguation changed.
5. Update `references/routing-checklist.md` if the pre-coding contract changed.
6. Update `references/recipes/prompt-patterns.md` if trigger examples or routing examples changed.
7. Update `README.md` only after the above files are correct.
8. Update `README-EN.md` after `README.md` if the human-facing explanation changed.
9. If provider maturity changed, update `references/research/coverage-status.md`.
10. If new official docs were used, update `references/research/source-registry.md`.

## Validation

### Preferred validation command on Windows

The local validator script may fail on Windows if Python reads files with `gbk` instead of UTF-8.

Use:

```powershell
$env:PYTHONUTF8='1'
python C:\Users\39473\.codex\skills\.system\skill-creator\scripts\quick_validate.py <path-to-skill>
```

Example:

```powershell
$env:PYTHONUTF8='1'
python C:\Users\39473\.codex\skills\.system\skill-creator\scripts\quick_validate.py E:\AI\SKILL\use-api\use-native-llm-apis-repo
```

### Expected result

The validator should print:

```text
Skill is valid!
```

### Provider example health check

Use the provider example validator when changing provider files, curl snippets, or documented base URLs.

It does not call real APIs. Instead, it checks:

- whether documented `curl` examples still parse cleanly
- whether JSON request bodies inside those examples are structurally valid
- whether documented base URLs and curl hosts still resolve via DNS

Command:

```powershell
python E:\AI\SKILL\use-api\use-native-llm-apis-repo\scripts\validate_provider_examples.py --providers-dir E:\AI\SKILL\use-api\use-native-llm-apis-repo\references\providers
```

Expected behavior:

- exit code `0` when no curl or DNS failures are found
- placeholder hosts such as `YOUR-RESOURCE-NAME...` may be reported as skipped instead of failed

## Smoke-test bar

Before calling a routing change "good", run the prompt set in [skill-smoke-tests.md](skill-smoke-tests.md).

A routing change is not complete unless it passes all three buckets:

- direct trigger prompts
- ambiguous prompts that should ask one clarification question
- non-trigger prompts that should stay out of this skill

## Quality bar for changes

Do not merge a skill-quality change unless:

- trigger wording became clearer or at least not broader without justification
- `SKILL.md`, `start-here.md`, `choose-the-right-recipe.md`, `routing-checklist.md`, `prompt-patterns.md`, `README.md`, and `README-EN.md` still agree on boundaries
- examples do not smuggle in unverified architecture assumptions
- coverage marketing does not overstate maturity compared with `coverage-status.md`
- the first 30 seconds of use feel easier, not harder

## Common failure modes

- frontmatter description turns into a mini README
- README repeats rules that already live in `SKILL.md`
- few-shot examples route ambiguous requests too aggressively
- provider counts are advertised without clarifying maturity differences
- a new routing page is added but not linked from `SKILL.md`
- a new routing page exists but is missing from `start-here.md`, `references/index.md`, or smoke tests
- Windows validation breaks because UTF-8 mode was not enabled
