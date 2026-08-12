# Technical Checklist Reference

The pass to run before calling a landing page or marketing site done. Grouped so you can work through it section by section rather than as one undifferentiated list.

## Responsive

- Test at minimum four widths: 375px (small mobile), 768px (tablet), 1024px (small desktop/laptop), 1440px (desktop). Hero sections and multi-column feature/pricing grids break first — check those specifically at each width.
- No horizontal scroll at any width — a single oversized element (a wide table, an un-constrained image, a fixed-width block) is the usual culprit.
- Touch targets at least 44x44px on mobile; don't rely on hover-only interactions for anything essential, since touch devices have no hover.
- Body text at minimum 16px on mobile to avoid the browser auto-zooming into inputs on focus.

## Performance

- Serve images in a modern format (WebP/AVIF) with `srcset` for responsive sizing, and lazy-load anything below the fold.
- Reserve layout space for async content (images, embeds, loaded data) so it doesn't jump the page around as it arrives — set explicit width/height or aspect-ratio.
- Keep the JS payload proportional to the page's actual interactivity — a mostly-static marketing page shouldn't ship a full app bundle.
- Respect `prefers-reduced-motion` for any scroll-triggered or ambient animation.

## Forms

- Validate on the client for immediate feedback, but always validate/sanitize on the server too — client-side checks are a UX convenience, not a security boundary.
- Disable the submit button (or show a loading state) during submission to prevent duplicate submits.
- Build a real success state (not just clearing the form silently) and a real error state that explains what to fix.
- Label every input properly (`<label for>` or `aria-label`) — placeholder text is not a substitute for a label, since it disappears once the user starts typing.

## Accessibility

- Color contrast at minimum 4.5:1 for body text, 3:1 for large text/UI components.
- Visible focus states on every interactive element — don't remove the browser's focus ring without replacing it.
- Alt text on meaningful images; empty `alt=""` on purely decorative ones so screen readers skip them.
- Tab order follows visual order; nothing interactive is unreachable by keyboard.

## SEO / sharing basics

- `<title>` and meta description specific to the page, not the site-wide default.
- Open Graph tags (`og:title`, `og:description`, `og:image`) so shared links preview correctly on social — these pages are built to be shared, so this isn't optional polish.
- One `<h1>` per page, used for the actual headline, not a logo or nav item.
- Semantic HTML (`<nav>`, `<main>`, `<section>`, `<footer>`) over generic `<div>` soup — this helps both SEO and assistive tech.

## Before shipping

- Click every link and submit every form end to end, including on mobile.
- Check the page at actual network speed (throttle to a slower connection) rather than only on a fast local/dev connection — first impressions of a marketing page are often on mobile data.
- Verify analytics/conversion tracking is actually wired to the primary CTA, not just present somewhere on the page.
