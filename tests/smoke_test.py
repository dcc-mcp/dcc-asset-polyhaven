from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "polyhaven-assets"
SCRIPTS = SKILL / "scripts"


def load(name: str):
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def validate_skill() -> None:
    from dcc_mcp_core import validate_skill

    report = validate_skill(str(SKILL))
    assert not report.has_errors, report


def descriptor_smoke() -> None:
    downloader = load("download_polyhaven_asset")
    descriptor = downloader.asset_descriptor("ArmChair_01", "/tmp/chair.gltf", ["/tmp/chair.bin"])
    assert descriptor["variants"][0]["local_path"] == "/tmp/chair.gltf"
    assert descriptor["attribution"]["license_spdx"] == "CC0-1.0"
    assert descriptor["extra"]["dependencies"] == ["/tmp/chair.bin"]


def hdri_download_smoke() -> None:
    downloader = load("download_polyhaven_asset")
    files = {"hdri": {"1k": {"hdr": {"url": "https://example.test/studio_1k.hdr"}}}}
    with patch.object(downloader, "api", return_value=files), patch.object(
        downloader, "fetch", return_value="/tmp/studio_1k.hdr"
    ):
        result = downloader.main(asset_id="studio", output_dir="/tmp", file_type="hdr", resolution="1k")
    assert result["success"], result
    assert result["context"]["asset_descriptor"]["variants"][0]["format"] == "hdr"


def live_polyhaven_smoke() -> None:
    if os.environ.get("RUN_LIVE_API_SMOKE") != "true":
        print("skip live Poly Haven API smoke")
        return
    search = load("search_polyhaven_assets").main(query="chair", asset_type="models", limit=1)
    assert search["success"], search
    assert search["context"]["assets"], search
    files = load("list_polyhaven_files").main(asset_id="ArmChair_01")
    assert files["success"], files
    assert "gltf" in files["context"]["files"], files


def main() -> None:
    validate_skill()
    descriptor_smoke()
    hdri_download_smoke()
    live_polyhaven_smoke()


if __name__ == "__main__":
    main()
