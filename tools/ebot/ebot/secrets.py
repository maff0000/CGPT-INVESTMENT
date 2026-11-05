"""Load a Massive API key without printing it.

The key comes from a hidden terminal prompt or a mode-0600 file outside any
git repository. There is no command-line key flag.
"""

from __future__ import annotations

import os
import stat
from pathlib import Path
from typing import Optional

from ebot.errors import SecretSetupError

_PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def credential_on_command_line(argv: list[str]) -> bool:
    """True when argv tries to pass a secret as a flag. The value is not read."""
    blocked = {"--api-key", "--apikey", "--token", "--key", "--secret"}
    for arg in argv:
        name = arg.split("=", 1)[0]
        if name in blocked:
            return True
    return False


def _git_root(start: Path) -> Optional[Path]:
    current = start.resolve()
    if current.is_file():
        current = current.parent
    for parent in [current, *current.parents]:
        if (parent / ".git").exists():
            return parent
    return None


def key_file_is_outside_repos(path: Path) -> bool:
    """Refuse keys stored in the package tree or any git work tree."""
    resolved = path.resolve()
    if resolved == _PACKAGE_ROOT or _PACKAGE_ROOT in resolved.parents:
        return False
    if _git_root(resolved) is not None:
        return False
    cwd_root = _git_root(Path.cwd())
    if cwd_root is not None and (resolved == cwd_root or cwd_root in resolved.parents):
        return False
    return True


def load_key_file(path: str) -> str:
    """Read one key line from a private 0600 file. Never print the contents."""
    candidate = Path(path)
    if not key_file_is_outside_repos(candidate):
        raise SecretSetupError(
            "Key file must be outside any git repository and outside the E-Bot package directory."
        )
    try:
        info = candidate.stat()
    except OSError:
        raise SecretSetupError("Key file is missing.") from None
    if not stat.S_ISREG(info.st_mode):
        raise SecretSetupError("Key file must be a regular file owned by you with mode 0600.")
    if info.st_uid != os.getuid():
        raise SecretSetupError("Key file must be a regular file owned by you with mode 0600.")
    if info.st_mode & 0o077:
        raise SecretSetupError("Key file must be a regular file owned by you with mode 0600.")
    try:
        text = candidate.read_text(encoding="utf-8")
    except OSError:
        raise SecretSetupError("Key file could not be read.") from None
    lines = text.splitlines()
    if len(lines) != 1 or not lines[0].strip() or lines[0] != lines[0].strip():
        raise SecretSetupError("Key file must contain one non-empty line and nothing else.")
    key = lines[0].strip()
    if any(char.isspace() for char in key):
        raise SecretSetupError("Key file must contain one non-empty line and nothing else.")
    return key


def resolve_api_key(
    key_file: Optional[str],
    *,
    stdin_is_tty: bool,
    prompter,
) -> Optional[str]:
    """Return the key, or None when the operator still needs to set one up.

    ``prompter`` is ``getpass.getpass`` in real use. Tests pass a stub.
    A missing key is SETUP_NEEDED, not a failed HTTP call.
    """
    if key_file:
        return load_key_file(key_file)
    if not stdin_is_tty:
        return None
    try:
        entered = prompter("Enter Massive API key (input hidden): ")
    except (EOFError, KeyboardInterrupt):
        return None
    if entered is None:
        return None
    cleaned = str(entered).strip()
    if not cleaned or any(char.isspace() for char in cleaned):
        return None
    return cleaned
