---
name: social-media-content-kit
description: Helps write and plan social media content for Telegram, VK, and Instagram — post templates, a content/promotion strategy checklist, and a tone-of-voice framework for keeping a brand's voice consistent across posts. Use this whenever the user asks to write a post, caption, or channel content for Telegram/VK/Instagram, wants to plan a posting/content strategy or content calendar, or wants to define or check a brand's tone of voice — even if they just paste a product/offer and ask "write a post about this" without naming the skill.
---

# Social Media Content Kit

This skill turns a raw idea, offer, or announcement into a platform-ready post, and helps plan the content strategy and voice behind a whole channel — not just a single post.

## When to use this

- "Write a post for our Telegram channel about [offer/news/event]"
- "Мне нужен пост для VK / Instagram про..."
- "Помоги спланировать контент-стратегию/контент-план для соцсетей"
- "Определи tone of voice для нашего бренда"
- Reviewing or fixing an existing post/caption that "doesn't feel right" for the channel

If the user only asks for research or competitor analysis (no post itself), that's a different job — check whether `content-research-writer` or `marketer-assistant` fits better first, and feel free to use them together (e.g., research the audience with `marketer-assistant`, then write the post with this skill).

## How to work

1. **Figure out the platform and the goal first.** A post that works on Telegram (long-form, no algorithmic reach limit, supports markdown/HTML formatting, native to send links) reads completely differently from an Instagram caption (algorithm-fed, hook has to survive being cut off after ~125 characters, hashtags matter) or a VK post (broader, older, more mixed-age audience than Instagram; native reposts/communities matter more than hashtags). Don't reuse one draft across all three unless the user explicitly wants that — read `references/platform-templates.md` for the shape each platform actually rewards.

2. **Check for an existing tone of voice.** If the user has described their brand's voice before, or there's a tone-of-voice doc in the project, use it. Otherwise, if this is a recurring channel (not a one-off post), it's worth 2-3 quick questions before writing anything: who is this brand talking to, and what should a reader feel — trusted, entertained, urgency to buy? `references/tone-of-voice.md` has a short framework for capturing this in a way that stays useful across many future posts, not just this one.

3. **Draft the post using the matching template**, then adapt it — templates are a starting shape, not a fill-in-the-blank form. A post that mechanically follows a template's slots usually reads stiffer than one that keeps the template's *logic* (hook → payoff → CTA) while varying the wording naturally.

4. **If the ask is about strategy/planning rather than a single post**, use `references/strategy-checklist.md` instead of jumping straight to templates — a content calendar or launch plan needs goals and cadence decided before any individual post gets written.

5. **Give the user the reasoning, not just the output**, when it's not a trivial one-liner — e.g., "used a question-hook for Instagram since the caption gets cut off in-feed" — so they can push back or reuse the reasoning themselves later.

## Reference files

- `references/platform-templates.md` — post structures and formatting norms per platform (Telegram, VK, Instagram), with examples
- `references/strategy-checklist.md` — checklist for planning a content/promotion strategy or content calendar
- `references/tone-of-voice.md` — framework for defining and checking a brand's tone of voice
