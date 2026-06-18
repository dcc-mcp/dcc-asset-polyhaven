from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _polyhaven import api


@skill_entry
def main(query: str | None = None, asset_type: str = "models", limit: int = 10, **_: Any) -> dict[str, Any]:
    try:
        params = {} if asset_type == "all" else {"t": asset_type}
        data = api("/assets", params)
        needle = (query or "").lower()
        items = []
        for asset_id, meta in data.items():
            haystack = " ".join(
                [
                    asset_id,
                    str(meta.get("name", "")),
                    " ".join(meta.get("tags", [])),
                    " ".join(meta.get("categories", [])),
                ]
            ).lower()
            if needle and needle not in haystack:
                continue
            items.append(
                {
                    "id": asset_id,
                    "name": meta.get("name"),
                    "type": meta.get("type"),
                    "categories": meta.get("categories", []),
                    "tags": meta.get("tags", [])[:12],
                    "thumbnail_url": meta.get("thumbnail_url"),
                }
            )
            if len(items) >= limit:
                break
        return skill_success("Poly Haven assets found", assets=items, count=len(items))
    except Exception as exc:
        return skill_exception(exc, message="Failed to search Poly Haven")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)

