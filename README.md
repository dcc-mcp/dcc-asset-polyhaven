# DCC-MCP Poly Haven Assets

Search and download CC0 assets from Poly Haven.

Poly Haven asks API clients to send a unique User-Agent. This skill does that
and keeps the implementation to simple search/list/download tools.

Downloads return a validated `asset_descriptor` with the preferred local file, Poly Haven source
URL, CC0 license, and dependency paths for a DCC adapter import skill.

## Example result

![A rendered red Barrel_01 asset imported into Blender](docs/images/polyhaven-barrel-01.jpg)

This image was produced through the real workflow: `download_polyhaven_asset`
downloaded `Barrel_01`, its `asset_descriptor` was passed to the Blender import
skill, and Blender rendered the result. The showcased asset is
[Barrel_01](https://polyhaven.com/a/Barrel_01) from Poly Haven, licensed under
[CC0 1.0](https://polyhaven.com/license).

## Install

```bash
dcc-mcp-cli marketplace add dcc-mcp/dcc-asset-polyhaven
dcc-mcp-cli marketplace install dcc-asset-polyhaven
```

## Tools

- `search_polyhaven_assets`
- `list_polyhaven_files`
- `download_polyhaven_asset`
