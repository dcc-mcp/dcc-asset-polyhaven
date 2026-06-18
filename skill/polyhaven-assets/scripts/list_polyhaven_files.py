from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _polyhaven import api


@skill_entry
def main(asset_id: str, **_: Any) -> dict[str, Any]:
    try:
        data = api(f"/files/{asset_id}")
        files = {
            file_type: sorted(variants.keys())
            for file_type, variants in data.items()
            if isinstance(variants, dict)
        }
        return skill_success("Poly Haven files listed", asset_id=asset_id, files=files, raw=data)
    except Exception as exc:
        return skill_exception(exc, message="Failed to list Poly Haven files")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)

