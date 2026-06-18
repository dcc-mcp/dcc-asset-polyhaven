from __future__ import annotations

import json
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


BASE_URL = "https://api.polyhaven.com"
HEADERS = {"User-Agent": "dcc-mcp-polyhaven/0.1"}


def api(path: str, params: dict[str, Any] | None = None) -> Any:
    url = BASE_URL + path
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch(url: str, output_dir: str, relative_name: str) -> str:
    target = Path(output_dir) / Path(relative_name)
    target.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=120) as resp:
        target.write_bytes(resp.read())
    return str(target)
