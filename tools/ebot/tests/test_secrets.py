"""Key handling stays off the command line, out of git, and out of errors."""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402,F401
import stat
import tempfile
import unittest
from pathlib import Path

from ebot.errors import SecretSetupError
from ebot.secrets import credential_on_command_line, load_key_file, resolve_api_key

KEY = "unit-test-massive-key"


class SecretTests(unittest.TestCase):
    def test_mode_0600_file_outside_git_is_read_without_echo(self):
        handle, name = tempfile.mkstemp(prefix="ebot-key-")
        os.close(handle)
        path = Path(name)
        try:
            path.write_text(KEY + "\n", encoding="utf-8")
            os.chmod(path, 0o600)
            self.assertEqual(load_key_file(str(path)), KEY)
            os.chmod(path, 0o644)
            with self.assertRaises(SecretSetupError) as caught:
                load_key_file(str(path))
            self.assertNotIn(KEY, str(caught.exception))
            self.assertIn("0600", str(caught.exception))
        finally:
            path.unlink(missing_ok=True)

    def test_key_inside_the_repo_or_package_is_refused(self):
        with self.assertRaises(SecretSetupError) as caught:
            load_key_file("/workspace/tools/ebot/massive.key")
        self.assertNotIn("massive.key contents", str(caught.exception))
        self.assertIn("git", str(caught.exception).lower())

    def test_missing_outside_file_does_not_invent_a_key(self):
        missing = Path(tempfile.gettempdir()) / "ebot-missing-key-file"
        if missing.exists():
            missing.unlink()
        with self.assertRaises(SecretSetupError) as caught:
            load_key_file(str(missing))
        self.assertIn("missing", str(caught.exception).lower())

    def test_group_readable_bit_is_refused_even_if_owner_can_read(self):
        handle, name = tempfile.mkstemp(prefix="ebot-key-")
        os.close(handle)
        path = Path(name)
        try:
            path.write_text(KEY + "\n", encoding="utf-8")
            os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP)
            with self.assertRaises(SecretSetupError):
                load_key_file(str(path))
        finally:
            path.unlink(missing_ok=True)

    def test_command_line_flags_are_detected_without_returning_the_value(self):
        self.assertTrue(credential_on_command_line(["run", "--api-key", KEY]))
        self.assertTrue(credential_on_command_line(["--token=" + KEY]))
        self.assertFalse(credential_on_command_line(["run", "massive-smoke", "--session", "2026-11-04"]))

    def test_non_interactive_stdin_does_not_prompt_or_succeed(self):
        class Silent:
            def isatty(self):
                return False

        def prompter(_prompt):
            raise AssertionError("prompted")

        self.assertIsNone(resolve_api_key(None, stdin_is_tty=Silent().isatty(), prompter=prompter))

    def test_blank_hidden_prompt_is_setup_needed_not_a_key(self):
        self.assertIsNone(resolve_api_key(None, stdin_is_tty=True, prompter=lambda _prompt: "  "))


if __name__ == "__main__":
    unittest.main()
