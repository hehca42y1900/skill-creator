# skill-creator

This repository hosts Claude Code project skills under `.claude/skills/`. Because skills live there, Claude Code automatically discovers and activates them for this project — no extra setup is needed.

## Installed skills

| Skill | Description | Source |
| --- | --- | --- |
| `skill-creator` | Create new Claude Code skills, iteratively improve existing ones, run evals, benchmark performance, and optimize skill descriptions for better triggering accuracy. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |
| `brand-guidelines` | Applies Anthropic's official brand colors and typography to artifacts for consistent visual identity. | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/brand-guidelines) |
| `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers in Python (FastMCP) or Node/TypeScript. | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/mcp-builder) |
| `avoid-ai-writing` | Audits and rewrites text to remove "AI-isms" — detect-only, edit-in-place, and voice-profile modes with an iterate-to-convergence pass. | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) |
| `naming` | Metaphor-driven process for naming products, brands, SaaS tools, and open source projects, with availability checks and an anti-slop evaluation rubric. | [glacierphonk/naming](https://github.com/glacierphonk/naming) |
| `proektnoe-upravlenie-alferov` | Project-management assistant based on Pavel Alferov's RIM-III model (book "Проектное управление. Как правильно делать правильные вещи", Skolkovo / MIF, 2025) — Pentabasis, CYNEFIN domain selection, Russian management specifics. | User-provided |

## Layout

```
.claude/skills/skill-creator/       SKILL.md + bundled scripts/agents/references/assets
.claude/skills/brand-guidelines/    SKILL.md
.claude/skills/mcp-builder/         SKILL.md + reference/scripts
.claude/skills/avoid-ai-writing/    SKILL.md
.claude/skills/naming/              SKILL.md + reference files, industries/, languages/, scripts/, templates/
.claude/skills/proektnoe-upravlenie-alferov/  SKILL.md + references/ (29 chapter notes)
```

Just describe what you want (e.g. "help me create a skill for X", "style this artifact with our brand colors", "help me build an MCP server for X", "clean up the AI-isms in this doc", "help me name this project") and Claude will use the relevant skill.

## Source & License

`skill-creator`, `brand-guidelines`, and `mcp-builder` are licensed under Apache 2.0 — see the `LICENSE.txt` inside each skill's folder. `avoid-ai-writing` and `naming` are licensed under MIT — see the `LICENSE` file inside each skill's folder. `proektnoe-upravlenie-alferov` has no separate license file; it is user-authored notes derived from the referenced book (no verbatim excerpts).
