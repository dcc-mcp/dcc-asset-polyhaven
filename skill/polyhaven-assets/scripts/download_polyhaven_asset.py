from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_error, skill_exception, skill_success

from _polyhaven import api, fetch


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

        return skill_success("Poly Haven asset downloaded", files=downloaded, asset_id=asset_id)
    except Exception as exc:
        return skill_exception(exc, message="Failed to download Poly Haven asset")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)

