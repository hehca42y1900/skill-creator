# skill-creator

This repository hosts Claude Code project skills under `.claude/skills/`. Because skills live there, Claude Code automatically discovers and activates them for this project — no extra setup is needed.

## Installed skills

| Skill | Description | Source |
| --- | --- | --- |
| `skill-creator` | Create new Claude Code skills, iteratively improve existing ones, run evals, benchmark performance, and optimize skill descriptions for better triggering accuracy. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |
| `brand-guidelines` | Applies Anthropic's official brand colors and typography to artifacts for consistent visual identity. | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/brand-guidelines) |
| `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers in Python (FastMCP) or Node/TypeScript. | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/mcp-builder) |

## Layout

```
.claude/skills/skill-creator/       SKILL.md + bundled scripts/agents/references/assets
.claude/skills/brand-guidelines/    SKILL.md
.claude/skills/mcp-builder/         SKILL.md + reference/scripts
```

Just describe what you want (e.g. "help me create a skill for X", "style this artifact with our brand colors", "help me build an MCP server for X") and Claude will use the relevant skill.

## Source & License

All skills vendored here are licensed under Apache 2.0 — see the `LICENSE.txt` inside each skill's folder.
