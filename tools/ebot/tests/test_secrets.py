"""Key handling stays off the command line, out of git, and out of errors."""

from __future__ import annotations

import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402,F401

from ebot.errors import SecretSetupError
from ebot.secrets import (
    _PACKAGE_ROOT,
    credential_on_command_line,
    load_key_file,
    resolve_api_key,
)

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

    def test_key_inside_the_package_is_refused_even_when_absent(self):
        target = _PACKAGE_ROOT / "massive.key"
        self.assertFalse(target.exists())
        with self.assertRaises(SecretSetupError) as caught:
            load_key_file(str(target))
        message = str(caught.exception).lower()
        self.assertIn("package", message)
        self.assertNotIn("missing", message)
        self.assertNotIn(KEY, message)

    def test_existing_key_inside_the_package_is_not_read(self):
        target = _PACKAGE_ROOT / "massive.key"
        target.write_text(KEY + "\n", encoding="utf-8")
        os.chmod(target, 0o600)
        try:
            with self.assertRaises(SecretSetupError) as caught:
                load_key_file(str(target))
            message = str(caught.exception)
            self.assertIn("package", message.lower())
            self.assertNotIn("missing", message.lower())
            self.assertNotIn(KEY, message)
        finally:
            target.unlink(missing_ok=True)

    def test_key_inside_a_git_work_tree_is_refused_when_one_exists(self):
        git_root = None
        for parent in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
            if (parent / ".git").exists():
                git_root = parent
                break
        if git_root is None:
            self.skipTest("this process is not running inside a git work tree")
        target = git_root / "ebot-operator-key-test.key"
        if _PACKAGE_ROOT == git_root or _PACKAGE_ROOT in target.parents:
            self.skipTest("git root and package directory are the same")
        self.assertFalse(target.exists())
        with self.assertRaises(SecretSetupError) as caught:
            load_key_file(str(target))
        message = str(caught.exception).lower()
        self.assertIn("git", message)
        self.assertNotIn("missing", message)

    def test_standalone_copy_without_git_refuses_a_key_inside_the_package(self):
        source = Path(__file__).resolve().parents[1]
        script = r"""
import os
import sys
from pathlib import Path

sys.path.insert(0, os.environ["EBOT_ROOT"])
from ebot.errors import SecretSetupError
from ebot.secrets import load_key_file

def check(path, expected):
    try:
        load_key_file(path)
    except SecretSetupError as exc:
        text = str(exc).lower()
        if expected not in text:
            raise SystemExit("wanted %s in %s" % (expected, text))
        if expected != "missing" and "missing" in text:
            raise SystemExit("misreported as missing: " + text)
        return
    raise SystemExit("accepted " + path)

check(os.environ["INSIDE_PRESENT"], "package")
check(os.environ["INSIDE_ABSENT"], "package")
check(os.environ["OUTSIDE_ABSENT"], "missing")
"""
        with tempfile.TemporaryDirectory(prefix="ebot-standalone-") as temporary:
            dest = Path(temporary) / "ebot"
            shutil.copytree(
                source,
                dest,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".git", "*.key"),
            )
            self.assertFalse((dest / ".git").exists())
            present = dest / "massive.key"
            present.write_text(KEY + "\n", encoding="utf-8")
            os.chmod(present, 0o600)
            absent = dest / "does-not-exist.key"
            outside = Path(temporary) / "outside-missing.key"
            env = os.environ.copy()
            env["EBOT_ROOT"] = str(dest)
            env["INSIDE_PRESENT"] = str(present)
            env["INSIDE_ABSENT"] = str(absent)
            env["OUTSIDE_ABSENT"] = str(outside)
            completed = subprocess.run(
                [sys.executable, "-c", script],
                cwd=str(dest),
                env=env,
                capture_output=True,
                text=True,
            )
            self.assertEqual(
                completed.returncode,
                0,
                completed.stdout + completed.stderr,
            )
            self.assertNotIn(KEY, completed.stdout + completed.stderr)

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
