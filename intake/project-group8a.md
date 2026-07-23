# Project Intake: Group8A

Status:Draft — ready for review
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
