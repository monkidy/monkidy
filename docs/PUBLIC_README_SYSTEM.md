# Public README design — editorial grammar

**Scope:** presentation guidance for Hichem's public GitHub profile and selected public repos. It is not the owner of any product's brand, technical truth, or release authority. The product's established design canon wins whenever they differ.

## One idea

A README is an entrance, not a wall of proof. Show one question, one object the visitor can inspect, one limit, and one exit. The rest can remain in the technical sections.

## Shared material, never a cloned template

- Editorial hierarchy: a clear name, one actual human sentence, visible public object, evidence and limitations, then installation/docs when relevant.
- Materials drawn from the existing public site: paper `#F6F1E7`, ink `#171713`, graphite `#5F5A50`, oxide `#C5682B`, restrained gold `#C8A96A`.
- Headers are illustrations, not fake screenshots or proof. All claims remain text, readable without the image.
- Use no remote tracking, dynamic GitHub-stats badges, artificial activity indicators, pseudo-testimonials or invented counts.
- Avoid decorative badge farms, gradient AI visuals, large grids of technology logos and faux dashboards.
- The GitHub reader's theme and narrow screen are first-rank: test both modes and the mobile layout; provide descriptive alt text.
- Prefer sharp reusable PNG + editable SVG source. Keep asset sizes small. No font files bundled or downloaded at runtime.
- Preserve a project's own identity: **SkeptOpus** keeps its brand, its four verdict characters and its current copy canon; **ACE Receipts** can use a dark proof chamber; **ANIMA** can use a spare three-lock illustration. Do not force them into the same colors.

## Templates by reader's purpose

### Product or open-source tool
1. Product name and one-sentence job.
2. Real screenshot, illustration or exact sample, explicitly distinguishable.
3. One working command / demo entry.
4. What it does not promise.
5. Features and installation.
6. Evidence, constraints, security notes, licence.

### Competition or experiment
1. The problem / constraint and what was actually submitted.
2. One credible demonstration or result with source.
3. Status: submitted, judged, failed or pending, with date.
4. Reproduction, evidence, comparison and failure cases.
5. Honest limits and dependencies.

### Research or archived object
1. What question was tested.
2. What can be reproduced and where.
3. What was learned, with measurement and uncertainty.
4. Reproduction method and bounded dependencies.
5. Historical status; do not imply ongoing active maintenance.

## Review gate before any public merge

Check the exact branch and asset paths. Confirm no internal file locations, secrets, endpoints or unpublished facts. Validate links, imagery, dark/light and narrow GitHub rendering. Confirm all existing technical sections, licence, safety disclaimers and dated evidence survive. Ask the owner for visual acceptance when required. Merge never proves that GitHub rendered the intended page.

## Explicit non-goals

No repo renaming, no global badge generator, no new visual framework, no automatic publication system, no rewriting every README into a sales page, no silent changes to product assets. This document adds a lightweight editorial grammar to existing work.


## V3 correction — 19 November 2026 (founder visual rejection)

The V2 minimal banners and generic marks were rejected as visually amateur. Do not re-present them as accepted brand design. The new *candidate* editorial assets use custom high-contrast artwork and project-specific illustrated symbols; they are **not registered logos, official product screenshots or technical proof**. Retain source provenance, use legible paired mobile artwork and test actual GitHub rendering. SkeptOpus retains its original animation and cast, linked from the project's own public repository. The original illustration is not a replacement for a project's technical evidence or brand canon. Never publish a visual-only PASS based on visual novelty.

## V4 / SkeptOpus visual lineage / 19 November 2026

**Source of inspiration, not source of ownership:** the live site
https://skeptopus.systasys.com/ was read in Chrome on 19 Nov 2026
(desktop and mobile; intro explicitly skipped). Its observed typographic stack
is DM Sans, DM Mono and Instrument Serif. Its current hero uses dark petrol
(#152329), a dark teal/green radial-to-linear background, ivory text,
mint (#B9DECB), and warm coral (#F27769). The older pastel brand bible
describes a different time/context; don't silently substitute it for live
rendering.

This GitHub family is an *adaptation*, not a copy of the SkeptOpus product
identity. The actual SkeptOpus character, red O, wordmark and animated banner
remain the project's own (media/banner-animated.webp, linked from its repo).
The new Hichem/ACE/ANIMA/EINSTEIN gradients, proof paths and shapes are original
candidate editorial illustrations, **not** registered logos or certification.

Rules: desktop and mobile art authored separately, no emojis, no fake success
ticks, no claims about a live payment, no invented metrics. Artwork is not proof.
Show real outcomes and accessible text. Review both GitHub dark and light, at
360/390/1280px. If a linked image fails, do not merge.

Editable generator: docs/brand/render_v4.py (Python Pillow + Playwright;
Google Fonts loaded by Chrome, no bundled font binaries). Run it to recreate
the assets locally. Public README remains the source of public facts.
Founder aesthetic acceptance and an independent review are separate gates.

## V5 / SkeptOpus profile illustration / 19 November 2026

Founder requested that the SkeptOpus **card on the personal GitHub profile** match the approved family of V4 project covers (gradients, typography and restrained mark-making). The two newly created assets are original *editorial presentation*, not the official brand files and not a certification or proof of software behavior. No change was requested to the public SkeptOpus product, website, mascot, red-O identity or its own README.

- Profile display: `assets/brand-v4/skeptopus-editorial-desktop.webp` (1800x600) and `assets/brand-v4/skeptopus-editorial-mobile.webp` (900x1120).
- Source/provenance: `docs/brand/skeptopus-editorial-source.png` is the output of the 19 Nov user-approved image draft; `docs/brand/skeptopus-mobile-compose.py` re-composes its elements for mobile. These are not source assets or trademarks from the SkeptOpus repo.
- Canonical SkeptOpus art remains in `systasys/skeptopus/media` and `core/art`. The original animated art remains in the SkeptOpus repository and can be opened directly by selecting the editorial cover in its README.
- Gate: review actual GitHub desktop/mobile appearance, check legible labels and no unintended brand confusion, and only then decide whether to merge the **profile** PR. Avoid passing candidate visual art into the product's brand canon by inference.
