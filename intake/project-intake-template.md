Status: Draft — ready for review
Project name: Munim 2.1 — Redesigning Cloud Accounting for India's CAs and MSMEs
Client/company: Munim (themunim.com)
Publicly shareable: Yes

---

## 1. Summary

Munim is a cloud accounting and billing platform built for Indian chartered accountants (CAs) and MSME business owners. In 2.1, I led the UX and UI redesign end to end — architecture, interaction design, and the design system — cutting core task time by roughly 70% and coinciding with the user base growing from 12,000 to over 100,000.

- **Product type:** Cloud-based accounting & billing SaaS
- **Platform:** Web at launch, later extended to Android and iOS
- **Timeline:** ~2 months — 1 month of architecture and IA work, 1 month of development
- **Role:** Sole UX/UI owner, working within a 3-person team
- **Team:** 3 people total

---

## 2. Problem

**The user problem.** Most Indian CAs learned their workflow on Tally — dense, keyboard-driven, everything-on-one-screen software. When accounting moved to the cloud, that mental model didn't translate cleanly: cloud interfaces need to be responsive, and Munim's first fold was carrying too many fields at once, with additional fields dynamically activating based on prior input. The result was a form that felt unpredictable rather than efficient — the opposite of what a CA doing repetitive, high-volume data entry needs.

Compounding this, a large share of CA users were still working on older 1440px displays, which showed up repeatedly in support tickets. Designing one interface that held up cleanly from a legacy desktop monitor to a modern laptop was a recurring source of friction, not a one-time fix.

**The business problem.** Weak day-to-day usability was translating directly into retention risk — users were leaving for more established platforms like Vyapar. For a product competing on trust with an audience of finance professionals, usability friction wasn't just an annoyance, it was a churn driver.

**Why it mattered.** CAs and MSME owners are not casual users — they touch this software daily, often for hours, to run someone else's business finances. Friction here has a compounding cost: every extra second per invoice multiplies across hundreds of clients and thousands of transactions.

---

## 3. Research

**Methods:**
- Interviews with CAs and non-technical MSME owners
- Usage analytics and heatmaps to locate where friction concentrated
- Competitive benchmarking against Tally, Zoho Books, and Vyapar
- A practical timing test on a core task (invoice creation)

**Key finding.** In the old design, creating an invoice for a new customer took an average of **1 minute 38 seconds**. That single number became the north star for the redesign — if the new IA and interaction model couldn't beat it decisively, the redesign hadn't done its job.

**Competitor insights.** Tally and traditional accounting tools set the expectation of density and keyboard control that CA users carry into any new platform. Zoho Books and Vyapar showed how competitors were already modernizing that experience for the cloud — raising the bar Munim needed to clear.

**User pain points:**
- Dynamic, conditionally-appearing fields that made forms feel unstable
- Inconsistent experience across screen sizes and resolutions
- No fast way to repeat the handful of tasks users do every single day
- A dashboard that didn't clearly answer "how is my business actually doing right now"
- Heavy reliance on the mouse in a user base that strongly prefers the keyboard

**Constraints.** The redesign had to preserve the information density CAs are used to and rely on, without recreating the old overwhelm — and it had to reach full keyboard parity, since CAs rarely touch the mouse.

---

## 4. Design Process

**Target users.** Two core segments: professional CAs managing multiple clients' books, and MSME owners/entrepreneurs managing their own business — different technical comfort levels, same need for speed and clarity.

**Information architecture.** The biggest structural shift was moving away from single, long-scrolling panels where every field is exposed at once, toward a tabbed, sectioned layout with progressive disclosure — grouping related fields (Basic Information, Mailing Details, Statutory Information, Bank Details, etc.) behind clear navigation instead of one continuous form.

**Design system.** Built a consistent component system applied across every screen, so the product would stop feeling like a set of stitched-together modules and start feeling like one coherent tool.

**Validation.** Heuristic evaluation with the team to catch usability issues systematically, combined with the invoice-creation timing test as a quantitative check on whether changes were actually working.

---

## 5. Decisions

### Decision 1 — A global quick-add bar
**What changed:** Added a persistent entry point, accessible from anywhere in the product, for creating new records — instead of requiring users to first navigate into the right module.
**Why:** In the old design, "where do I add this" was a recurring point of friction, especially on a cloud platform used across many contexts.
**Evidence:** Recurring pattern in interviews and support tickets around locating the right place to add a record.
**Tradeoff:** A persistent UI element has to earn its place on every single screen without competing visually with in-context actions — it needed a restrained, consistent treatment rather than a loud one.

### Decision 2 — A favorites/shortcuts bar for daily tasks
**What changed:** Surfaced one-click access to the handful of tasks users repeat constantly: adding customers, creating invoices, and finding and analyzing reports.
**Why:** Research showed that most daily usage collapses into a small, repeatable set of actions — forcing users through full navigation for each one added up to real, cumulative friction.
**Evidence:** Interview findings and usage-pattern analytics pointing to the same handful of repeat tasks.
**Tradeoff:** Needed to stay lightweight and uncluttered rather than becoming a second, competing navigation system.

### Decision 3 — A business-health dashboard
**What changed:** Expanded the dashboard to surface stock levels, what needs restocking, sales activity, and where profit is being gained or lost — at a glance.
**Why:** The previous dashboard didn't give owners or CAs a clear read on business health, which fed directly into the retention problem.
**Evidence:** Business-side usability gap identified through research and competitor comparison.
**Tradeoff:** More information on one screen risks reintroducing the density problem the rest of the redesign was solving — this had to be balanced carefully against the "no unnecessary scrolling" principle.

### Decision 4 — A keyboard-first interaction model
**What changed:** Built full keyboard accessibility with visible shortcuts (for example, ⌥+S to save, Esc to discard), so the product could be operated end to end without a mouse.
**Why:** CA users overwhelmingly prefer the keyboard — a habit carried over from years on Tally and similar desktop tools.
**Evidence:** Direct, consistent user preference surfaced in research.
**Tradeoff:** Every new interaction pattern had to be checked for keyboard operability, which rules out mouse-dependent patterns like hover-only reveals.

### Decision 5 — A unified design system
**What changed:** Standardized components and visual language across the entire product surface.
**Why:** To replace the old, inconsistent feel with something predictable and trustworthy — important for software handling financial data.
**Evidence:** Cross-screen inconsistency was one of the clearest gaps in the old product.
**Tradeoff:** Standardizing across a large feature set is slow, front-loaded work — a meaningful share of the one-month architecture phase went into getting this right before development started.

---

## 6. Iterations

**Before:** Dense, single-scroll panels exposing every field at once, as in the original item-creation flow.

**After:** Sectioned, tabbed flows with progressive disclosure, clear labeling, and visible keyboard controls, as in the redesigned account-creation flow.

**What improved:** Reduced visual noise per screen, a clearer sense of where you are in a task, and a measurable drop in task time — invoice creation went from ~1:38 to under 30 seconds.

*Note: the two flows shown below aren't the identical screen pre/post-redesign — pairing an exact same-screen before/after would make this section even stronger for the final portfolio page, if you have one available from the design file.*

**Before — Create Item (v2.0):**
![Before: dense single-scroll Create Item panel](before-create-item.png)

**After — Create Account (v2.1):**
![After: tabbed, sectioned Create Account flow](after-create-account.png)

**Dashboard — business health at a glance (v2.1):**
![Dashboard surfacing income, stock, and revenue signals](dashboard-overview.png)

---

## 7. Impact

- **User impact:** Invoice creation time cut by roughly 70%, from ~1:38 to under 30 seconds. Full keyboard-first workflows for CA power users.
- **Business impact:** User base grew from 12,000 before the update to 40,000+ within one month of the 2.1 launch, and to roughly 100,000 users at present.
- **Metrics:** 12,000 → 40,000+ (1 month post-launch) → ~100,000 (current); invoice creation time reduced ~70%.
- **Stakeholder feedback:** Positive response from clients, with support tickets shifting from complaints toward appreciation of the 2.1 design.
- **What shipped:** Munim 2.1 on web, followed by native Android and iOS apps.

---

## 8. Lessons

**What I learned:** The strongest design decisions came directly from fact-based, current-state research — not assumptions. Grounding the redesign in real usage data, interviews, and a hard timing benchmark is what made it possible to identify the actual problems (not just the visible ones) and defend the decisions made to fix them.

**What this proves about my design skill:** The ability to take a legacy, structurally unorganized product — serving a demanding, keyboard-first professional user base — and turn it into a scalable, consistent design system that drove measurable, compounding business growth.

---

## 9. Content Angles

- **LinkedIn lesson:** "We didn't redesign Munim because it looked outdated — we redesigned it because a stopwatch told us invoices took 1:38 to create. Here's what changed when we chased that number down to under 30 seconds."
- **Carousel idea:** Before/after screens side by side, with the invoice-time stat and the 12K → 100K growth curve as the hook.
- **Case study title:** "Munim 2.1: Redesigning Cloud Accounting for 100,000+ Indian CAs and MSMEs"
- **Portfolio headline:** "From 1:38 to under 30 seconds — rebuilding Munim's UX around how accountants actually work"

---

## 10. Assets

- **Figma link:** https://www.figma.com/design/GlNVPICg9KKMepBqpMmWu1/The-Munim-Accounting-2.1--Inter-?node-id=38942-26297&t=EZJE8n53lWlFVkyP-1
- **Public link:** https://themunim.com/
- **Screenshots:** before-create-item.png, after-create-account.png, dashboard-overview.png (included above)
- **Notes:** Add a matching same-screen before/after pair and any direct user quotes/testimonials if available — these two additions would meaningfully strengthen the Iterations and Impact sections above.

---
---


Status: Draft — ready for review
Project name: Group8A | SaaS
Client/company: Confidential (referred to publicly as "Group8A"), delivered while at Identixweb
Publicly shareable: Yes — as "Group8A," with the real client name withheld

---

## 1. Summary

Group8A is a confidential marketing agency running affiliate marketing for 100+ clients on a single internal dashboard their own team had built and used for over four years. I led the UX redesign of that dashboard — a 30+ page web app SaaS product — working directly with the client's Head of Design and one junior designer on my side, and introduced a proper Figma design system to close the gap between what designers specified and what developers shipped.

- **Product type:** Web app SaaS dashboard (admin + sub-account levels)
- **Platform:** Web
- **Timeline:** 2 months
- **Role:** UX lead, working directly with the client's Head of Design
- **Team:** Myself plus 1 junior designer, delivered as an Identixweb engagement

---

## 2. Problem

**The core problem:** the dashboard didn't feel alive — not at the admin level, and not at the sub-account level either. That showed up in a few concrete ways:

- **Static, one-size-fits-all tables.** Every user saw the same unfiltered table regardless of their actual job. An affiliate lead specialist working across multiple links only needs to see the fields tied to lead volume and source — not the full, undifferentiated dataset. Showing everything at first glance wasn't productive; it just added noise to a job that's already high-volume.
- **Reporting disconnected from daily work.** The affiliate team couldn't easily pull outcome-based reports from what they'd actually done that day — the analytical layer sat apart from the workflow instead of growing out of it.
- **A genuine visual and workflow gap for the people using it daily.** The agency's own employees — the ones tracking affiliate performance every day — were working with a tool that had aged out of their actual needs, both visually and functionally.
- **Lead tracking on high-volume days was a real pain point.** With 100+ leads active at once, employees struggled to identify where any single lead stood — what stage it was in, where it had come from, what outcome it needed next. Finding one lead's status inside that volume was genuinely difficult.

**Why it mattered:** this wasn't a cosmetic complaint — it was daily friction for the people whose entire job is processing that data, on a tool that had already been in production for four years without a structural rethink.

---

## 3. Research

**Methods:**
- Contextual inquiry with the employees actually using the platform day to day
- Direct meetings and conversations with the client's team
- Review of real analytics and client reports to see actual usage patterns, not assumptions

**Key finding.** The client-side stakeholder — the Head of Design — already had a deep, accurate operational understanding of the whole system and how work should be prioritized inside it. That reframed the research approach: rather than proposing new design theories in isolation, the team's job was to validate any new direction against what that stakeholder already knew to be true about how the system needed to run. That discipline kept decisions accurate and avoided rework later in the build.

**User pain points:** unfiltered, role-blind tables; reporting that didn't reflect daily work; a calendar/lead-tracking view with no clear way to identify individual lead status inside a high volume of daily activity; a visual experience that had fallen behind what the daily users needed.

---

## 4. Design Process

**Stakeholder alignment.** Worked directly with the client's Head of Design throughout, using their operational knowledge of the system as the validating layer for every proposed change.

**Design system.** Built a proper design system inside Figma specifically to close the gap between design intent and development output — critical on a 30+ page product where inconsistency compounds fast.

**Workflow-first thinking.** Instead of designing generic table and report views, the team asked users directly how they work day to day, then built views scoped to that specific job — not the dataset as a whole.

**Validation.** Produced multiple design variants and ran them through usability testing to identify the most suitable direction before committing, followed by training sessions with the client's team once the new design shipped.

---

## 5. Decisions

### Decision 1 — Role-oriented, filterable tables
**What changed:** Replaced the static, everything-at-once table with role-scoped views — for example, an affiliate lead specialist sees only the fields relevant to tracking leads across multiple links, not the full dataset.
**Why:** Showing every field to every user at first glance wasn't productive; most of what was on screen wasn't relevant to the task at hand.
**Evidence:** Direct conversations with employees about how they actually work day to day.
**Tradeoff:** Role-based views require more upfront architecture — filters and fields have to be defined per table and per use case rather than built once generically.

### Decision 2 — Reconnecting reporting to daily workflow
**What changed:** Rebuilt the analytical/status reporting layer so the affiliate team could see outcomes tied directly to their daily work, instead of a disconnected reporting module.
**Why:** The old reporting existed apart from the workflow, so it wasn't actually helping people track their own outcomes.
**Evidence:** Same workflow research — reporting was flagged as disconnected from daily use.
**Tradeoff:** Tying reporting to daily workflow requires the underlying data structure to support that granularity — a heavier lift than a general-purpose report.

### Decision 3 — A calendar view with status indicators for lead tracking
**What changed:** Introduced a calendar-based view with visual badges/indicators showing each lead's status, so employees could see where any given lead stood on a high-volume day.
**Why:** The single biggest daily friction point was losing track of individual leads inside 100+ concurrent leads — no clear way to see status at a glance.
**Evidence:** Directly identified as the most painful recurring workflow moment in research.
**Tradeoff:** A calendar-based structure has to stay legible even on the busiest days, which meant the visual indicator system needed to be extremely clear and low-noise, not just informative.

### Decision 4 — A real Figma design system
**What changed:** Established a proper, structured design system rather than one-off screens, so specs would translate cleanly from design to development.
**Why:** On a 30+ page product, inconsistency between design and build compounds quickly and slows everyone down.
**Evidence:** Recurring developer/designer handoff gap on the existing product.
**Tradeoff:** Building the system took real time upfront, in a project that already had a short two-month timeline.

### Decision 5 — Visual design pass plus variant testing
**What changed:** Alongside the functional fixes, gave the dashboard a genuine visual upgrade, and tested multiple design variants with users before settling on a direction.
**Why:** The interface hadn't just fallen behind functionally — it had fallen behind visually for people who look at it for hours every day.
**Evidence:** Direct user feedback and the variant usability tests themselves.
**Tradeoff:** Running true variant testing inside a two-month timeline meant the testing cycle had to be tight and decisive.

---

## 6. Iterations

**Before:** Static, unfiltered tables showing the same full dataset to every role; lead status scattered with no dedicated way to track it on high-volume days; reporting disconnected from daily work.

**After:** Role-scoped, filterable tables built around actual job function; a calendar view with clear status indicators for lead tracking; reporting tied directly to daily workflow output.

*Note: assets for this project are confidential/credential-gated, so no screenshots are included here — happy to slot them in if you're ever able to share sanitized versions.*

---

## 7. Impact

- **User impact:** Clearer understanding of each module compared to the old version; daily work roughly **2x faster** than before.
- **Business impact:** Positive feedback from the client's current users on the new system.
- **What shipped:** A redesigned 30+ page web SaaS dashboard, backed by a new Figma design system, covering both admin and sub-account experiences.

---

## 8. Lessons

**What I learned:** The strongest design decisions on this project didn't come from introducing new theory — they came from validating against a stakeholder who already deeply understood how the system needed to run, then translating that operational knowledge into role-specific, workflow-first interfaces. Listening to the person who already knows the system, before proposing what should change, is what kept the work accurate and avoided rework on a tight two-month timeline.

**What this proves about my design skill:** The ability to take a complex, long-standing internal tool — used daily by real operators under real time pressure — and rebuild it around how people actually work, not just how the data happens to be structured, while introducing the design-system discipline that keeps a 30+ page product consistent going forward.

---

## 9. Content Angles

- **LinkedIn lesson:** "The best UX insight on this project didn't come from a new framework — it came from asking one affiliate lead specialist what fields he actually needed to see. Here's what happened when we rebuilt a 100+ client dashboard around that answer."
- **Carousel idea:** "One table, three roles, three views" — showing how the same dataset was scoped differently per job function.
- **Case study title:** "Group8A: Rebuilding a 100-Client Affiliate Dashboard Around the People Who Actually Use It"
- **Portfolio headline:** "2x faster — redesigning a 4-year-old affiliate dashboard around real daily workflows"

---

## 10. Assets

- **Figma link:** Confidential / credential-gated, not publicly shareable
- **Screenshots:** Not available for public use
- **Public link:** Not applicable (internal client tool)
- **Notes:** If sanitized or blurred screens ever become shareable, adding a before/after of the table view or the calendar/lead-status view would be the strongest visual proof points for this case study.


