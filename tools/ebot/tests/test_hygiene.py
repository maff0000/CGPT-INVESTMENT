"""The package stays free of shells, extra clients, and stored secrets."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402,F401

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "ebot"


class HygieneTests(unittest.TestCase):
    def test_package_source_has_no_shell_or_extra_clients(self):
        forbidden = (
            "import subprocess",
            "from subprocess",
            "os.system(",
            "eval(",
            "exec(",
            "import socket",
            "import requests",
            "import http.client",
        )
        for path in sorted(PACKAGE.glob("*.py")):
            text = path.read_text(encoding="utf-8")
            for snippet in forbidden:
                self.assertNotIn(snippet, text, path.name + " contains " + snippet)
            if path.name != "massive.py":
                self.assertNotIn("urlopen", text, path.name)

    def test_only_the_client_names_the_provider_host(self):
        for path in sorted(PACKAGE.glob("*.py")):
            text = path.read_text(encoding="utf-8")
            if path.name == "massive.py":
                self.assertIn("https://api.massive.com", text)
            elif path.name == "cli.py":
                self.assertIn("api.massive.com", text)
            else:
                self.assertNotIn("api.massive.com", text, path.name)

    def test_no_secret_files_are_shipped(self):
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            self.assertFalse(path.name.startswith(".env"), path.name)
            self.assertNotEqual(path.suffix, ".key", path.name)


if __name__ == "__main__":
    unittest.main()
