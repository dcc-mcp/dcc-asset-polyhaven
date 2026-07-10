from __future__ import annotations

from pathlib import Path
from typing import Any

from dcc_mcp_core.asset_import import AssetAttribution, AssetDescriptor, AssetFileVariant
from dcc_mcp_core.skill import skill_entry, skill_error, skill_exception, skill_success

from _polyhaven import api, fetch


def asset_descriptor(asset_id: str, local_path: str, dependencies: list[str]) -> dict[str, Any]:
    descriptor = AssetDescriptor(
        asset_id=f"polyhaven:{asset_id}",
        variants=[
            AssetFileVariant(
                local_path=local_path,
                format=Path(local_path).suffix.lstrip(".").lower() or "unknown",
                preferred=True,
            )
        ],
        attribution=AssetAttribution(
            source_url=f"https://polyhaven.com/a/{asset_id}",
            license_spdx="CC0-1.0",
            attribution_text="Poly Haven asset — CC0 1.0 Universal.",
        ),
        extra={"dependencies": dependencies},
    )
    descriptor.validate()
    return descriptor.to_dict()


@skill_entry
def main(
    asset_id: str,
    output_dir: str,
    file_type: str = "gltf",
    resolution: str = "2k",
    include_dependencies: bool = True,
    **_: Any,
) -> dict[str, Any]:
    try:
        data = api(f"/files/{asset_id}")
        variant = ((data.get(file_type) or {}).get(resolution) or {}).get(file_type)
        if not variant:
            return skill_error("Poly Haven variant not found", f"{asset_id} {file_type} {resolution}", raw=data)

        downloaded = [fetch(variant["url"], output_dir, variant["url"].rsplit("/", 1)[-1])]
        if include_dependencies:
            for relative_name, dep in (variant.get("include") or {}).items():
                downloaded.append(fetch(dep["url"], output_dir, relative_name))

        return skill_success(
            "Poly Haven asset downloaded",
            files=downloaded,
            asset_id=asset_id,
            asset_descriptor=asset_descriptor(asset_id, downloaded[0], downloaded[1:]),
        )
    except Exception as exc:
        return skill_exception(exc, message="Failed to download Poly Haven asset")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)
