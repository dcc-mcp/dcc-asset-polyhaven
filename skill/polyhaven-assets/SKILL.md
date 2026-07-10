---
name: polyhaven-assets
description: Search, inspect, and download Poly Haven CC0 assets as validated AssetDescriptors.
license: MIT
compatibility: "dcc-mcp-core 0.19+, Python 3.7+"
metadata:
  dcc-mcp:
    version: v0.1.0
    dcc: python
    layer: domain
    tags:
      - asset
      - polyhaven
      - cc0
      - models
      - hdris
      - textures
      - download
    search-hint: "poly haven, polyhaven, cc0 assets, model download, hdri download, texture download, gltf, blend, fbx"
    produces: [asset_descriptor]
    tools: tools.yaml
---

# Poly Haven Assets

Use this skill for Poly Haven CC0 asset discovery and downloads. It does not
import files into a DCC scene; host-specific import belongs in host skills.

`download_polyhaven_asset` returns an `asset_descriptor` with a local preferred variant, CC0
attribution, and any downloaded dependencies. Pass that descriptor to a DCC adapter import skill.
