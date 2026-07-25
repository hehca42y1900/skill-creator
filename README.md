# skill-creator

This repository hosts the official [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator) skill from Anthropic's [anthropics/skills](https://github.com/anthropics/skills) repository, set up as a Claude Code project skill.

`skill-creator` helps you create new Claude Code skills, iteratively improve existing ones, run evals to test them, benchmark performance, and optimize skill descriptions for better triggering accuracy.

## Layout

```
.claude/skills/skill-creator/   Official skill-creator skill (SKILL.md + bundled scripts/agents/references/assets)
```

Because the skill lives under `.claude/skills/`, Claude Code automatically discovers and activates it for this project — no extra setup is needed. Just describe what you want (e.g. "help me create a skill for X" or "let's improve this skill based on user feedback") and Claude will use it.

## Source & License

Vendored from `anthropics/skills` (`skills/skill-creator`), licensed under Apache 2.0 — see `.claude/skills/skill-creator/LICENSE.txt`.
