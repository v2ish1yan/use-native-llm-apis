#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import socket
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse


CURL_BLOCK_RE = re.compile(r"```(?:bash|sh|shell|zsh)\n(.*?)```", re.S)
BASE_URL_RE = re.compile(r"- Base URL:\s*`([^`]+)`")
DATA_FLAGS = {"-d", "--data", "--data-raw", "--data-binary", "--json"}
PLACEHOLDER_MARKERS = (
    "your-",
    "your_",
    "example",
    "<",
    ">",
    "{",
    "}",
)
TOKEN_RE = re.compile(r"""'[^']*'|"[^"]*"|\S+""", re.S)


@dataclass
class CurlCheck:
    command: str
    url: str | None
    ok: bool
    errors: list[str] = field(default_factory=list)


@dataclass
class HostCheck:
    source: str
    url: str
    host: str
    status: str
    addresses: list[str] = field(default_factory=list)
    error: str | None = None


@dataclass
class ProviderReport:
    file: str
    curl_checks: list[CurlCheck] = field(default_factory=list)
    host_checks: list[HostCheck] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return all(check.ok for check in self.curl_checks) and all(
            check.status in {"resolved", "skipped"} for check in self.host_checks
        )


def extract_curl_blocks(text: str) -> list[str]:
    return [match.group(1).strip() for match in CURL_BLOCK_RE.finditer(text) if "curl " in match.group(1)]


def normalize_shell_block(block: str) -> str:
    lines = []
    current = ""
    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        if line.endswith("\\"):
            current += line[:-1].rstrip() + " "
            continue
        current += line
        lines.append(current.strip())
        current = ""
    if current.strip():
        lines.append(current.strip())
    return "\n".join(lines)


def extract_curl_commands(block: str) -> list[str]:
    normalized = normalize_shell_block(block)
    commands = []
    for line in normalized.splitlines():
        stripped = line.strip()
        if stripped.startswith("curl "):
            commands.append(stripped)
    return commands


def strip_wrapping_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def tokenize_command(command: str) -> list[str]:
    tokens = TOKEN_RE.findall(command)
    joined = "".join(tokens)
    compact_original = re.sub(r"\s+", "", command)
    compact_joined = re.sub(r"\s+", "", joined)
    if compact_original != compact_joined:
        raise ValueError("unable to tokenize command cleanly")
    return tokens


def parse_curl_command(command: str) -> tuple[str | None, str | None]:
    parts = tokenize_command(command)
    if not parts or parts[0] != "curl":
        raise ValueError("command does not start with curl")

    url = None
    data = None
    i = 1
    while i < len(parts):
        part = parts[i]
        if part in DATA_FLAGS:
            if i + 1 >= len(parts):
                raise ValueError(f"missing payload after {part}")
            data = strip_wrapping_quotes(parts[i + 1])
            i += 2
            continue
        unwrapped = strip_wrapping_quotes(part)
        if unwrapped.startswith("http://") or unwrapped.startswith("https://"):
            url = unwrapped
        i += 1
    return url, data


def validate_curl_command(command: str) -> CurlCheck:
    errors: list[str] = []
    url = None

    try:
        url, data = parse_curl_command(command)
    except ValueError as exc:
        return CurlCheck(command=command, url=None, ok=False, errors=[str(exc)])

    if not url:
        errors.append("missing URL")
    else:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            errors.append(f"unsupported URL scheme: {parsed.scheme}")
        if not parsed.netloc:
            errors.append("URL missing host")

    if data:
        stripped = data.strip()
        if stripped.startswith("{") or stripped.startswith("["):
            try:
                json.loads(stripped)
            except json.JSONDecodeError as exc:
                errors.append(f"invalid JSON payload: {exc.msg}")

    return CurlCheck(command=command, url=url, ok=not errors, errors=errors)


def extract_base_urls(text: str) -> list[str]:
    return [match.group(1).strip() for match in BASE_URL_RE.finditer(text)]


def should_skip_host(host: str) -> bool:
    lowered = host.lower()
    return any(marker in lowered for marker in PLACEHOLDER_MARKERS)


def resolve_host(source: str, url: str) -> HostCheck:
    parsed = urlparse(url)
    host = parsed.hostname
    if not host:
        return HostCheck(source=source, url=url, host="", status="invalid", error="missing host")
    if should_skip_host(host):
        return HostCheck(source=source, url=url, host=host, status="skipped")

    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror as exc:
        return HostCheck(source=source, url=url, host=host, status="unresolved", error=str(exc))

    addresses = sorted({item[4][0] for item in infos if item[4]})
    return HostCheck(source=source, url=url, host=host, status="resolved", addresses=addresses)


def build_provider_report(path: Path) -> ProviderReport:
    text = path.read_text(encoding="utf-8")
    report = ProviderReport(file=path.name)

    for block in extract_curl_blocks(text):
        for command in extract_curl_commands(block):
            report.curl_checks.append(validate_curl_command(command))

    urls: list[tuple[str, str]] = []
    urls.extend(("base_url", url) for url in extract_base_urls(text))
    urls.extend(("curl", check.url) for check in report.curl_checks if check.url)

    seen: set[tuple[str, str]] = set()
    for source, url in urls:
        key = (source, url)
        if key in seen:
            continue
        seen.add(key)
        report.host_checks.append(resolve_host(source, url))

    return report


def summarize(reports: Iterable[ProviderReport]) -> dict[str, int]:
    reports = list(reports)
    return {
        "providers": len(reports),
        "providers_ok": sum(1 for report in reports if report.ok),
        "curl_checks": sum(len(report.curl_checks) for report in reports),
        "curl_failures": sum(1 for report in reports for check in report.curl_checks if not check.ok),
        "host_checks": sum(len(report.host_checks) for report in reports),
        "host_failures": sum(1 for report in reports for check in report.host_checks if check.status == "unresolved"),
        "host_skipped": sum(1 for report in reports for check in report.host_checks if check.status == "skipped"),
    }


def print_human(reports: list[ProviderReport]) -> None:
    summary = summarize(reports)
    print(
        f"Checked {summary['providers']} provider files, "
        f"{summary['curl_checks']} curl examples, {summary['host_checks']} host entries."
    )
    print(
        f"Providers OK: {summary['providers_ok']}/{summary['providers']} | "
        f"Curl failures: {summary['curl_failures']} | "
        f"DNS failures: {summary['host_failures']} | "
        f"DNS skipped: {summary['host_skipped']}"
    )

    for report in reports:
        if report.ok:
            continue
        print(f"\n[{report.file}]")
        for check in report.curl_checks:
            if check.ok:
                continue
            print(f"  curl error: {check.command}")
            for error in check.errors:
                print(f"    - {error}")
        for host in report.host_checks:
            if host.status != "unresolved":
                continue
            print(f"  dns error: {host.url}")
            print(f"    - {host.error}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate provider markdown curl examples and base URL DNS resolution."
    )
    parser.add_argument(
        "--providers-dir",
        default="references/providers",
        help="Directory containing provider markdown files.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON output.",
    )
    args = parser.parse_args()

    providers_dir = Path(args.providers_dir)
    reports = [
        build_provider_report(path)
        for path in sorted(providers_dir.glob("*.md"))
        if path.name != "index.md"
    ]

    if args.json:
        payload = {
            "summary": summarize(reports),
            "reports": [
                {
                    "file": report.file,
                    "ok": report.ok,
                    "curl_checks": [asdict(check) for check in report.curl_checks],
                    "host_checks": [asdict(check) for check in report.host_checks],
                }
                for report in reports
            ],
        }
        json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        print_human(reports)

    summary = summarize(reports)
    return 1 if summary["curl_failures"] or summary["host_failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
