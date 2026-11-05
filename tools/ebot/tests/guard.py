"""Block real network use before the package captures urllib symbols."""

import http.client
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _blocked(*args, **kwargs):
    raise AssertionError("offline test blocked a network call")


def install():
    urllib.request.urlopen = _blocked
    http.client.HTTPConnection.request = _blocked
    http.client.HTTPSConnection.request = _blocked


install()
