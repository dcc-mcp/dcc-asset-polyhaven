# DCC-MCP Poly Haven Assets

Search and download CC0 assets from Poly Haven.

Poly Haven asks API clients to send a unique User-Agent. This skill does that
and keeps the implementation to simple search/list/download tools.

Downloads return a validated `asset_descriptor` with the preferred local file, Poly Haven source
URL, CC0 license, and dependency paths for a DCC adapter import skill.

## Install

```bash
dcc-mcp-cli marketplace add dcc-mcp/dcc-asset-polyhaven
dcc-mcp-cli marketplace install dcc-asset-polyhaven
```

## Tools

- `search_polyhaven_assets`
- `list_polyhaven_files`
- `download_polyhaven_asset`
