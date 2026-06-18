---
name: polyhaven-assets
description: Search, inspect, and download CC0 Poly Haven models, HDRIs, and textures.
metadata:
  dcc-mcp:
    version: v0.1.0
    dcc: python
    display_name: Poly Haven Assets
    group: asset.download.cc0
    default_icon: package
    affinity: any
    marketplace: dcc-asset-polyhaven
    tools: tools.yaml
    execution: sync
    permissions:
      - network
      - filesystem
    examples:
      - "Search Poly Haven for chair models"
      - "List available GLTF files for a Poly Haven model"
      - "Download a Poly Haven GLTF model and dependencies"
    contact:
      name: dcc-mcp team
      url: https://github.com/dcc-mcp/dcc-asset-polyhaven
    install:
      add_source: "dcc-mcp-cli marketplace add dcc-mcp/dcc-asset-polyhaven"
      then_install: "dcc-mcp-cli marketplace install dcc-asset-polyhaven"
---

# Poly Haven Assets

Use this skill for Poly Haven CC0 asset discovery and downloads. It does not
import files into a DCC scene; host-specific import belongs in host skills.
