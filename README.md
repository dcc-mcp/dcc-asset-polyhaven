# DCC-MCP Poly Haven Assets

<p align="center">
  <img src="docs/assets/dcc-asset-polyhaven.svg" alt="DCC-MCP · POLYHAVEN-ASSETS" width="600">
</p>

## Agent workflow

AI agents should use installed package skills through the shared gateway. IDE
users may continue to use the MCP endpoint.

### Install or update the CLI

`dcc-mcp-cli` is the preferred control path for every shell-capable agent. If
it is missing, ask the user before installing the latest official release:

```bash
# Linux/macOS
curl -fsSL https://raw.githubusercontent.com/dcc-mcp/dcc-mcp-core/main/scripts/install-cli.sh | sh

# Windows PowerShell
powershell -ExecutionPolicy Bypass -c "irm https://raw.githubusercontent.com/dcc-mcp/dcc-mcp-core/main/scripts/install-cli.ps1 | iex"
```

Keep an official build current through the release manifest:

```bash
dcc-mcp-cli update check
dcc-mcp-cli update apply
```

`update apply` downloads and stages the latest CLI for the next launch. It
does not update a running `dcc-mcp-server`; update that server in its own
environment.

```bash
dcc-mcp-cli dcc-types
dcc-mcp-cli list
dcc-mcp-cli search --query "<task>" --dcc-type <host>
dcc-mcp-cli describe <tool-slug>
dcc-mcp-cli call <tool-slug> --json '{"key":"value"}'
```

If the package skill is not active, call
`dcc-mcp-cli load-skill <skill-name> --dcc-type <host>`. After the task,
query `dcc-mcp-cli stats --range 24h --session-id <task-id>` and pass only
bounded evidence to the `review_skill_improvement` prompt from
`dcc-mcp-skills-creator`.


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
