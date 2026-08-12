---
name: website-landing-builder
description: Guidance for planning, writing, and building complete marketing websites and landing pages — information architecture, conversion-focused copy, and production-ready responsive code. Covers hero sections, feature/benefit blocks, social proof, pricing, FAQ, CTA placement, plus performance, SEO basics, forms, and accessibility. Use this skill whenever the user asks to build, design, redesign, improve, or launch a landing page, marketing site, product page, portfolio site, SaaS homepage, waitlist page, or any single-page website — even if they only describe a business, product, or service they want a page for, without using the words "landing page" or "website" explicitly.
---

# Website & Landing Page Builder

Treat this as a small studio engagement that owns the whole page, not just the wireframe: what it says, how it's organized, what it looks like, and whether the code actually ships. A landing page has one job — get a specific visitor to take a specific action — and every section, sentence, and pixel either serves that job or gets cut.

This skill is about **structure, content, and build quality**. For the visual identity itself — palette, type pairing, layout concept, the one signature element that makes the page memorable — check whether a `frontend-design` skill is available in this project and lean on it; it exists specifically to avoid the generic AI-website look. If it isn't available, the condensed version is: pick a 4–6 color palette and a deliberate type pairing that fit *this* brief specifically (not your default choices), and give the page one genuinely distinctive moment instead of spreading effort evenly.

## Ground the brief before building

If the user's request doesn't pin these down, infer them from context and state your assumption in one line so they can correct it:

- **The one action** the page wants a visitor to take (buy, sign up, book a call, join a waitlist, download). Everything else is secondary.
- **Who's landing on it** and what they already believe or doubt when they arrive — a cold ad click needs more convincing than someone who followed a referral.
- **What the business/product actually is**, in the founder's own words if you have them. Generic copy comes from generic understanding of the subject.

## Page architecture

These are the sections marketing pages and landings reach for — treat them as a toolbox, not a checklist. Include what earns its place for this brief, drop what doesn't, and reorder when the story calls for it. A dev-tool selling to engineers might skip testimonials and lead with a code sample; a coaching business might skip pricing and lead with a video. See `references/page-structure.md` for what makes each block work and common failure modes.

1. **Nav** — minimal on conversion-focused pages (logo + one CTA is often enough); fuller on multi-page sites.
2. **Hero** — the single most persuasive claim above the fold, paired with the primary CTA. This is the whole pitch in one glance; most visitors decide here whether to keep reading.
3. **Problem or value proposition** — why this matters, in the visitor's terms, not the company's.
4. **Features → benefits** — translate what it does into what changes for the visitor. A feature list is a spec sheet; a benefit list is a reason to buy.
5. **Social proof** — logos, testimonials, numbers, case studies. Placed near the decision points, not dumped in one block.
6. **How it works** — for anything with onboarding friction or a process worth demystifying.
7. **Pricing** — if applicable, anchored and simple; hidden pricing is a conversion killer unless there's a real reason for it (enterprise sales).
8. **FAQ** — this is where you pre-answer the objections that are actually stopping people, not generic filler questions.
9. **Final CTA** — restate the offer once more before the footer; don't make it the only place to convert.
10. **Footer** — trust signals, legal, secondary links. Keep it out of the way of the primary conversion path.

## One goal, one CTA

Resist the instinct to give visitors multiple things to do. A page offering "Sign up" and "Learn more" and "Contact sales" with equal visual weight makes the visitor choose, and choosing is friction — most will choose nothing. Pick the one action that matters most for this brief, make it the loud button repeated at natural decision points (end of hero, after social proof, final CTA), and let everything else — secondary links, "learn more" — recede visually.

## Copy that converts

Words are structural on a landing page, not decoration — a vague headline loses the visitor before the design gets a chance to work. See `references/copywriting.md` for headline formulas, CTA phrasing, and microcopy patterns. The core habit: write the specific benefit, not the generic tagline. "Cut your invoice time from 2 hours to 10 minutes" beats "Streamline your workflow" because it's concrete enough to be believed.

## Build it to actually ship

A beautiful comp that isn't responsive, is slow, or has a broken form isn't a landing page — it's a mockup. See `references/technical-checklist.md` for the full pass, but the load-bearing ones:

- **Responsive** at minimum 375px (mobile), 768px (tablet), 1024–1440px (desktop) — check the hero and any multi-column sections specifically, they break first.
- **Performance** — optimize images (correct format, `srcset`/lazy-loading), avoid layout shift from async content, keep the JS payload proportional to what the page actually does.
- **Forms work** — validation, loading state on submit, a real success state and a real error state, not just a console log.
- **Accessibility** — labeled inputs, visible focus states, sufficient color contrast (4.5:1 for body text), alt text on meaningful images.
- **Meta basics** — title, description, and at minimum an Open Graph image, since these pages are built to be shared and clicked from search/social.

## Before calling it done

Read the page as a skeptical first-time visitor, not as its builder:

- Does the hero pass the 5-second test — can a stranger say what this is and what to do next?
- Is the primary CTA visible without scrolling on mobile, not just desktop?
- Do all links and the form actually work end to end?
- Does anything in the copy oversell what the product currently does?
- Would this page be mistaken for a template if you dropped in a different logo? If yes, go back to the one signature element and sharpen it.
