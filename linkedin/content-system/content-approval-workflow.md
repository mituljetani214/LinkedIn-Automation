# Content Approval Workflow

Status: active
Last updated: 2026-07-23

This workflow keeps LinkedIn automation human-approved. AI can research, draft, organize, and suggest improvements, but Mitul approves before anything is posted.

## Core Rule

No automatic publishing in V1.

Every post must move through:

```text
Idea -> Draft -> Review -> Approved -> Published -> Measured -> Learned
```

## Folder Flow

```text
linkedin/posts/drafts/
```

AI-generated or rough human content. Not ready to post.

```text
linkedin/posts/review/
```

Drafts that need Mitul's decision. These should be close to final but still editable.

```text
linkedin/posts/approved/
```

Mitul has approved the content. These are ready to manually post on LinkedIn.

```text
linkedin/posts/published/
```

Content that has been posted. Add the LinkedIn URL and posting date.

```text
linkedin/posts/rejected/
```

Drafts that should not be posted. Keep them for learning.

## Approval Status Values

Use one of these statuses inside each post file:

- `idea`
- `draft`
- `needs_review`
- `approved`
- `published`
- `rejected`
- `needs_rewrite`

## Weekly Content Workflow

### Monday: Generate Ideas

Inputs:

- `career/career-intake-summary.md`
- `career/projects.md`
- `knowledge/writing-style.md`
- `linkedin/profile/linkedin-profile-copy.md`
- `research/daily/`

Output:

- 10-15 ideas in `linkedin/posts/drafts/`

### Tuesday: Draft Content

Turn the best ideas into:

- Text posts
- Carousel outlines
- Case study snippets
- Comment prompts

### Wednesday: Review

Move strong drafts into `linkedin/posts/review/`.

Mitul reviews:

- Is this true?
- Does this sound like me?
- Is there any confidential information?
- Is the hook strong?
- Is the CTA natural?

### Thursday-Friday: Approve And Post

Move approved files into `linkedin/posts/approved/`.

Mitul manually posts on LinkedIn.

After posting, move the file into `linkedin/posts/published/` and add:

- Posted date
- LinkedIn URL
- First 24-hour metrics when available

### Sunday: Learn

Add metrics to `analytics/linkedin_metrics.csv`.

Then run:

```powershell
python scripts/generate_weekly_report.py
```

## What AI Can Do

- Research trends
- Suggest content ideas
- Draft posts
- Rewrite hooks
- Create carousel outlines
- Generate comment ideas
- Suggest posting order
- Analyze metrics
- Recommend next experiments

## What Mitul Must Approve

- Final post content
- Any personal story
- Any metric or product growth claim
- Any client/company mention
- Any recruiter or connection message
- Any public case study detail

## Approval Checklist

Before moving a post to `approved`, check:

- [ ] It is truthful.
- [ ] It sounds like Mitul.
- [ ] It has one clear idea.
- [ ] It does not reveal confidential client details.
- [ ] Metrics are framed safely.
- [ ] It teaches something useful.
- [ ] The CTA feels natural.
- [ ] It supports the profile positioning.

## Safe Metric Rules

Use:

- "Contributed during growth from..."
- "Supported..."
- "Helped reduce..."
- "Worked on UX/product design during..."

Avoid:

- "I alone grew..."
- "Guaranteed..."
- "10x revenue..." unless verified
- Any metric without a source or timeframe

## First Content Pillars

1. AI-native Product Design
2. Human-Centered AI
3. SaaS UX and Enterprise UX
4. Design Systems
5. Product Thinking
6. Workflow Simplification
7. UX Leadership
8. Case Studies With Measurable Outcomes

