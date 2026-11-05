"""Remove credential material from text that an operator might copy."""

from __future__ import annotations

import re

_API_KEY_QUERY = re.compile(r"(?i)api[_-]?key=[^&\s]+")


def redact(text: str, secrets: list[str]) -> str:
    """Replace known secrets and query-string keys. Does not log anything."""
    cleaned = text
    for secret in secrets:
        if not secret or len(secret) < 8:
            continue
        cleaned = cleaned.replace("Bearer " + secret, "Bearer [REDACTED]")
        cleaned = cleaned.replace(secret, "[REDACTED]")
    cleaned = _API_KEY_QUERY.sub("apiKey=[REDACTED]", cleaned)
    return cleaned
