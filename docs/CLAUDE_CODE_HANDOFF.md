# Claude Code Handoff: LinkedIn Automation / AI Career OS

Last updated: 2026-07-23
Owner: Mitul Jetani
Repository: https://github.com/mituljetani214/LinkedIn-Automation

## 1. Project Purpose

This repository is Mitul Jetani's AI Career OS.

The goal is not only LinkedIn automation. The goal is to create a modular, human-approved system that grows Mitul's career by managing career knowledge, generating LinkedIn content, improving personal branding, creating portfolio/case-study assets, tracking analytics, and learning from performance over time.

The current priority is the LinkedIn content automation system:

```text
Career Brain + Project Proof + Writing Voice
  -> AI Content Ideas
  -> Draft Posts
  -> Human Review
  -> Approved Content
  -> Ready-to-Post Package
  -> Manual LinkedIn Publishing
  -> Analytics
  -> Learning Loop
```

## 2. Non-Negotiable Rules

- Do not auto-publish to LinkedIn in the first working version.
- Mitul must approve final content before publishing.
- Do not fabricate metrics, employers, clients, awards, or product impact.
- Munim growth must be framed as contribution, not solo causation.
- Do not use "10x revenue" publicly until stronger evidence exists.
- Do not reveal confidential client details, especially for Group8A.
- AI can draft, organize, package, and recommend. Mitul approves.

## 3. Current Repository State

Completed:

- Repo initialized and synced to GitHub.
- Career intake system completed.
- Master career intake completed.
- LinkedIn profile intake completed.
- Writing voice intake completed.
- Two project intake files created.
- Career source-of-truth files populated.
- LinkedIn profile brushup completed.
- Human-approved content workflow created.

Current latest known commit:

```text
ab79e0a Add human-approved content workflow
```

## 4. Important Folders

```text
career/
```

Source-of-truth career facts, positioning, projects, skills, and metrics.

```text
intake/
```

Raw and structured intake data. This is mostly complete and should be used as evidence, not overwritten casually.

```text
knowledge/
```

Durable writing style and research/source knowledge.

```text
linkedin/profile/
```

Paste-ready LinkedIn profile copy and optimization strategy.

```text
linkedin/content-system/
```

Content approval workflow and first 30-day content plan.

```text
linkedin/posts/
```

Human-approved post pipeline:

```text
drafts/
review/
approved/
published/
rejected/
```

```text
templates/
```

Reusable content templates.

```text
scripts/
```

Local automation helpers.

```text
analytics/
```

LinkedIn metrics CSV and weekly reports.

## 5. Key Files To Read First

Read these before making automation decisions:

```text
README.md
ROADMAP.md
PROJECT_PLAN.md
docs/OPERATING_SYSTEM.md
career/career-intake-summary.md
career/profile.md
career/projects.md
career/skills.md
career/metrics.md
knowledge/writing-style.md
linkedin/profile/linkedin-profile-copy.md
linkedin/content-system/content-approval-workflow.md
linkedin/content-system/first-30-day-plan.md
templates/linkedin-approval-post.md
```

## 6. Mitul's Career Positioning

Recommended market-facing positioning:

```text
Lead Product Designer | AI-Powered SaaS, Design Systems, Enterprise UX, Product Strategy
```

Mitul is positioned between:

- Lead Product Designer
- Lead UI/UX Engineer
- UX Architect
- AI Product Designer
- Design Systems Lead
- Design Technologist
- Human-AI Interaction Designer

Core themes:

- AI-native Product Design
- Human-Centered AI
- SaaS UX
- Enterprise UX
- Design Systems
- Product Thinking
- Workflow Simplification
- UX Leadership
- Case Studies With Measurable Outcomes

## 7. Writing Voice

Mitul's writing should be:

- Clear
- Practical
- Simple
- Minimal
- Human
- Evidence-based
- Product-thinking led
- Useful for product designers, founders, recruiters, and product teams

Approved phrases:

- Design should solve real business problems.
- AI should augment humans, not replace human judgment.
- Human + AI is stronger than either alone.
- Every experience must remain human-centric.
- Never jump directly into design.
- Research first, design second.
- Understand the problem before designing the solution.
- Design is not only about screens; it is about decisions.
- Designing systems, not just screens.
- Simplifying complexity through product thinking.
- Good UX starts before Figma.

Avoid:

- Fake authority
- Generic motivational posts
- Unsupported claims
- AI replacement hype
- Claims like "I alone caused this growth"
- Empty thought leadership
- Overly academic UX language

## 8. Strongest Proof Points

Use these carefully:

- 9+ years of product, UI/UX, and design leadership experience.
- Led a team of 6 designers.
- Contributed UX/product design work during Munim's growth from approximately 12,000 to 100,000+ active customers.
- Reduced Munim invoice creation time from approximately 1:38 to under 30 seconds.
- Redesigned a 30+ page confidential SaaS dashboard for Group8A, making daily work roughly 2x faster.
- Built scalable Figma design systems for complex SaaS products.
- Uses AI across research, discovery, documentation, prototyping, content, and workflow design.
- DiamondRensu / HulkApps work supported 35% CRO improvement.

Metrics requiring caution:

- "80% happy users" needs clearer source.
- "10x revenue" needs stronger evidence and should not be used publicly yet.

## 9. Project Proof

### Munim 2.1

Publicly shareable.

Core story:

Munim is a cloud accounting and billing SaaS platform for Indian Chartered Accountants and MSME business owners. Mitul led UX/UI redesign across architecture, interaction design, and design systems.

Key points:

- Invoice creation went from approximately 1:38 to under 30 seconds.
- Product grew from approximately 12,000 to 100,000+ active customers during the period of Mitul's UX/product contribution.
- Use contribution language, not solo ownership.
- Strong content angles:
  - Good UX starts with a stopwatch, not a screen.
  - How we reduced invoice creation from 1:38 to under 30 seconds.
  - Why accounting UX needs keyboard-first design.
  - Designing cloud accounting for users trained by Tally.

### Group8A

Confidential client. Publicly refer to it as Group8A only.

Core story:

A confidential marketing agency SaaS dashboard used for affiliate marketing operations across 100+ clients. Mitul led UX redesign of a 30+ page dashboard and introduced a Figma design system.

Key points:

- Daily work became roughly 2x faster.
- Static tables became role-oriented, filterable views.
- Reporting was reconnected to daily workflow.
- Calendar view with lead status indicators helped high-volume lead tracking.
- Strong content angles:
  - One table, three roles, three views.
  - Why role-based dashboards beat one-size-fits-all tables.
  - How to redesign a tool people have used every day for four years.
  - Design systems matter most when a product has 30+ pages.

## 10. Existing Scripts

```text
scripts/check_career_intake.py
```

Checks if intake is complete.

```text
scripts/generate_content_calendar.py
```

Creates a weekly content calendar.

```text
scripts/generate_weekly_report.py
```

Reads `analytics/linkedin_metrics.csv` and generates a report.

```text
scripts/content_status_report.py
```

Counts posts across:

```text
drafts
review
approved
published
rejected
```

## 11. Automation System To Build Next

The next implementation should create a real approval-to-package workflow.

Recommended new folders:

```text
linkedin/posts/packages/
linkedin/assets/images/
linkedin/assets/carousels/
linkedin/assets/prompts/
```

Recommended new scripts:

```text
scripts/approve_post.py
scripts/reject_post.py
scripts/package_post.py
scripts/create_post_from_template.py
scripts/generate_first_posts.py
scripts/validate_post.py
```

### approve_post.py

Purpose:

- Move a post from `linkedin/posts/review/` to `linkedin/posts/approved/`.
- Change metadata from `Status: needs_review` to `Status: approved`.
- Add `Approved date`.
- Preserve filename.

Suggested usage:

```powershell
python scripts/approve_post.py post-file-name.md
```

### reject_post.py

Purpose:

- Move a post from `review/` to `rejected/`.
- Change status to `rejected`.
- Optionally append rejection reason.

### package_post.py

Purpose:

- Take an approved post.
- Create a ready-to-post package under `linkedin/posts/packages/{slug}/`.
- Include:
  - `post.md`
  - `caption.txt`
  - `posting-checklist.md`
  - `image-prompt.md`
  - `hashtags.txt`
  - optional `carousel-outline.md`

### create_post_from_template.py

Purpose:

- Create a new draft from `templates/linkedin-approval-post.md`.
- Pre-fill status, date, category, and source.

### generate_first_posts.py

Purpose:

- Generate the first 4 review-ready posts from:
  - Munim
  - Group8A
  - writing style
  - LinkedIn positioning

Important:

- This script can be deterministic and template-based at first. It does not need an LLM API in v1.

### validate_post.py

Purpose:

- Verify each post has:
  - Status
  - Hook
  - Post Draft
  - CTA
  - Approval checklist
  - No forbidden phrases
  - Safe metric framing

## 12. Artifact / Image Automation Direction

Mitul asked whether ChatGPT can create ready-to-share images.

Recommended v1:

- Do not auto-generate final images until the post is approved.
- For every approved post, create an `image-prompt.md` and `carousel-outline.md`.
- Later, use image generation or a Figma/HTML template to create actual visuals.

Best first artifact types:

1. Single image quote/insight card
2. Carousel outline
3. PDF carousel document
4. Posting checklist

Recommended first visual format:

```text
1080 x 1350 LinkedIn portrait post
```

Design style:

- Minimal
- High contrast
- Clear typography
- One main idea
- No clutter
- Practical product-design feel

## 13. LinkedIn API Reality

LinkedIn's official Posts API can create organic posts with text, images, videos, documents, articles, and multi-image posts, but member posting requires OAuth permissions such as `w_member_social`.

Do not build auto-posting first.

Build this sequence:

```text
approved post
  -> ready-to-post package
  -> manual posting
  -> metrics tracking
```

Later add:

```text
LinkedIn OAuth
  -> token storage outside repo
  -> publish approved packages only
```

Never store LinkedIn access tokens in Git.

## 14. Content Approval State Machine

Use this workflow:

```text
idea
  -> draft
  -> needs_review
  -> approved
  -> packaged
  -> published
  -> measured
```

Existing repo folders currently support:

```text
drafts/
review/
approved/
published/
rejected/
```

Need to add:

```text
packages/
```

## 15. First Four Posts To Generate

Create these as review-ready drafts:

### Post 1

Theme:

Good UX starts before Figma.

Source:

Writing style + Munim project.

Angle:

Design should start with research, workflow, and problem understanding, not screens.

### Post 2

Theme:

From 1:38 to under 30 seconds.

Source:

Munim.

Angle:

How a task-time benchmark shaped the redesign.

### Post 3

Theme:

One table, three roles, three views.

Source:

Group8A.

Angle:

Role-based UX beats showing everyone the same data.

### Post 4

Theme:

Human + AI in product design.

Source:

Career positioning + writing style.

Angle:

AI helps research, discovery, documentation, and prototyping, but human judgment remains the core.

## 16. Preferred Implementation Style

- Keep scripts dependency-free Python where possible.
- Use markdown files as the database in v1.
- Preserve human approval as a file-state movement.
- Avoid overbuilding.
- Keep all generated content visible and editable.
- Use clear filenames and dates.
- Commit changes to GitHub after each meaningful phase.

## 17. Claude Code Starting Prompt

Use this prompt in Claude Code:

```text
You are working in the LinkedIn-Automation repository for Mitul Jetani's AI Career OS.

Read docs/CLAUDE_CODE_HANDOFF.md first.

Your next task is to implement the human-approved content automation layer:

1. Add packages folder structure.
2. Create approve/reject/package/create/validate scripts.
3. Generate the first four review-ready LinkedIn drafts from Munim, Group8A, and writing style source files.
4. Ensure no LinkedIn auto-posting exists yet.
5. Run scripts/content_status_report.py and validate the workflow.
6. Commit the changes.

Keep the system file-based, human-approved, and safe.
```

