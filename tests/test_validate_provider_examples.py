from pathlib import Path
import tempfile
import unittest

from scripts.validate_provider_examples import (
    build_provider_report,
    extract_curl_blocks,
    extract_curl_commands,
    normalize_shell_block,
    validate_curl_command,
)


class ValidateProviderExamplesTests(unittest.TestCase):
    def test_extracts_and_normalizes_multiline_curl(self) -> None:
        text = """```bash
curl https://api.example.com/v1/chat/completions \\
  -H "Authorization: Bearer $KEY" \\
  -d '{"model":"demo"}'
```"""
        blocks = extract_curl_blocks(text)
        self.assertEqual(len(blocks), 1)
        normalized = normalize_shell_block(blocks[0])
        self.assertIn("curl https://api.example.com/v1/chat/completions", normalized)
        commands = extract_curl_commands(blocks[0])
        self.assertEqual(len(commands), 1)

    def test_validates_json_payload(self) -> None:
        check = validate_curl_command(
            """curl https://api.example.com/v1/chat/completions -H "Content-Type: application/json" -d '{"model":"demo","messages":[]}'"""
        )
        self.assertTrue(check.ok)

    def test_reports_invalid_json_payload(self) -> None:
        check = validate_curl_command(
            """curl https://api.example.com/v1/chat/completions -d '{"model": }'"""
        )
        self.assertFalse(check.ok)
        self.assertTrue(any("invalid JSON payload" in error for error in check.errors))

    def test_skips_placeholder_dns_hosts(self) -> None:
        content = """# Demo

- Base URL: `https://YOUR-RESOURCE-NAME.openai.azure.com`

```bash
curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses \\
  -H "api-key: $AZURE_OPENAI_API_KEY" \\
  -d '{"model":"demo","input":"hello"}'
```
"""
        with tempfile.TemporaryDirectory() as tmp:
            provider = Path(tmp) / "demo.md"
            provider.write_text(content, encoding="utf-8")
            report = build_provider_report(provider)
        self.assertEqual(len(report.curl_checks), 1)
        self.assertTrue(report.curl_checks[0].ok)
        self.assertTrue(any(check.status == "skipped" for check in report.host_checks))


if __name__ == "__main__":
    unittest.main()
