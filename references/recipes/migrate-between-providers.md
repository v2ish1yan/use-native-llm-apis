# Migrate Between Providers

Use this recipe when existing code already works for one provider and must be ported to another.

## Goal

Preserve behavior while changing the wire format as little as necessary.

## What to open first

1. the current provider file
2. the target provider file
3. `references/comparisons/request-shape-differences.md`
4. one of the other comparison files if the task also involves streaming, tools, or structured output

## Migration order

1. Move auth and base URL first.
2. Remap the top-level request shape.
3. Remap system prompt placement.
4. Remap user content nesting.
5. Remap response parsing.
6. Remap advanced features such as streaming, tools, or schemas.

## High-risk areas

- `input` vs `messages` vs `contents`
- top-level `system` vs `role: "system"` vs inline config
- content blocks vs parts vs plain strings
- tool declaration keywords
- schema or JSON-mode controls
- stream event semantics

## Safe migration pattern

- Keep the old request next to the new one while porting.
- Change one concern at a time.
- Compare raw requests and raw responses, not only post-processed app objects.
- If the old code used an abstraction layer, temporarily peel it back until the new wire format is correct.

## Common trap

Mechanical renames are not enough. A provider migration is a shape migration, not a search-and-replace exercise.

## Exit criteria

This recipe is complete when:

- the target provider returns a successful response
- the app reads the correct output field
- advanced features are re-validated instead of assumed
