# Add Structured Output

Use this recipe when the response must be consumed by code rather than read by a human.

## Goal

Make the output reliably parseable without pretending all providers expose the same schema feature.

## What to open first

1. the target provider file
2. `references/comparisons/structured-output-differences.md`

## Decision rule

Use the strongest supported boundary in this order:

1. native schema controls
2. tool or function calling as the schema boundary
3. tightly constrained JSON prompts

## Safe order

1. Start with a tiny schema.
2. Verify which native feature the provider actually supports.
3. Parse the result immediately after receipt.
4. Add validation in code.
5. Only then expand the schema.

## Common mistakes

- Assuming "JSON mode" means full schema enforcement
- Reusing OpenAI schema fields in Gemini unchanged
- Relying on prompt wording alone when strict parsing matters
- Skipping runtime validation because the provider "usually" returns valid JSON

## Minimal success test

Use a schema small enough to eyeball:

- `title: string`
- `priority: string`
- `done: boolean`

The request is successful only when your code parses and validates the result, not when the response merely looks JSON-shaped.

## Exit criteria

This recipe is complete when:

- the provider returns machine-consumable output
- your code validates it
- failure cases are handled explicitly
