# Validation and Maintenance

Use this file when updating the skill itself, not when using provider references during application development.

## Maintenance goals

Keep four things healthy:

1. trigger boundaries stay precise
2. routing docs stay consistent
3. provider status stays honest
4. validation stays runnable on the maintainer's machine

## Single-source rules

- `SKILL.md` defines when the skill should load.
- `references/recipes/prompt-patterns.md` gives trigger examples and routing examples.
- `README.md` explains the project to humans and should not become a second source of trigger truth.
- `references/research/coverage-status.md` is the source of truth for maturity labels such as `covered`, `partial`, `pending`, and `blocked`.

## Update checklist

When changing the skill itself:

1. Check whether the change affects trigger rules, routing, or maintenance behavior.
2. Update `SKILL.md` first if trigger boundaries changed.
3. Update `references/recipes/prompt-patterns.md` if trigger examples or routing changed.
4. Update `README.md` only after the above files are correct.
5. If provider maturity changed, update `references/research/coverage-status.md`.
6. If new official docs were used, update `references/research/source-registry.md`.

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

## Quality bar for changes

Do not merge a skill-quality change unless:

- trigger wording became clearer or at least not broader without justification
- `SKILL.md`, `prompt-patterns.md`, and `README.md` still agree on boundaries
- examples do not smuggle in unverified architecture assumptions
- coverage marketing does not overstate maturity compared with `coverage-status.md`

## Common failure modes

- frontmatter description turns into a mini README
- README repeats rules that already live in `SKILL.md`
- few-shot examples route ambiguous requests too aggressively
- provider counts are advertised without clarifying maturity differences
- Windows validation breaks because UTF-8 mode was not enabled
