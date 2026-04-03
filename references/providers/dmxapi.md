# DMXAPI Relay

## Summary

Use DMXAPI when the project needs a hosted aggregation layer that supports multiple upstream provider formats through one platform. DMXAPI is not a native model vendor; it is a relay service with its own docs, routing layer, and standardized integration guidance.

## Auth and Base URL

DMXAPI's docs describe replacing upstream official bases with the DMXAPI base:

- `https://www.dmxapi.cn/v1`

The docs also mention using the root domain for other compatibility modes:

- `https://www.dmxapi.cn`

Auth:

- DMXAPI API key
- normally passed as `Authorization: Bearer ...`

## Primary access pattern

DMXAPI documents:

- quick-start integration
- common endpoint usage
- OpenAI-style requests
- Claude-style compatibility
- Responses API support

This makes it a multi-format relay rather than a single-format wrapper.

## Practical notes

The public docs explicitly say:

- replace the official OpenAI base URL with the DMXAPI base
- Claude original format is supported on the DMXAPI domain
- Responses API format is supported

That means it is reasonable to model DMXAPI as a compatibility gateway with multiple protocol surfaces.

## Common pitfalls

- Assuming DMXAPI only supports OpenAI-compatible requests
- Forgetting to replace the base URL when reusing official client code
- Treating DMXAPI as if it guarantees full upstream-native behavior

## Sources

- DMXAPI docs home: <https://doc.dmxapi.com/>
- DMXAPI Chinese docs home: <https://doc.dmxapi.com/zh/>
- DMXAPI quick start: <https://doc.dmxapi.com/jichu.html>
- DMXAPI common endpoints: <https://doc.dmxapi.com/jiekou.html>
- DMXAPI Responses API note: <https://doc.dmxapi.com/responses.html>
