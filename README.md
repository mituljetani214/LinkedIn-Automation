# LinkedIn Automation

AI Career OS for Mitul Jetani.

My AI Brain for my profile which understands my whole career path.

This repository is a modular, human-approved system for growing a UI/UX design career through better knowledge management, LinkedIn content, portfolio building, recruiter outreach, research, and analytics.

## Vision

Build an open-source AI operating system that continuously grows a professional career while keeping the human in control of publishing, networking, and final decisions.

## Core Principles

- Open source
- Free first
- AI assisted
- Human approved
- Modular
- Extendable

## What This Repo Contains

- `career/` - resume, skills, projects, achievements, and career facts
- `knowledge/` - durable source-of-truth knowledge used by all agents
- `agents/` - role definitions for each AI assistant workflow
- `prompts/` - reusable prompts for content, research, outreach, and analysis
- `templates/` - markdown templates for posts, case studies, reports, and messages
- `research/` - daily trend and UX research notes
- `linkedin/` - posts, comments, outreach drafts, and profile optimization work
- `analytics/` - metrics, reports, and learnings
- `automation/` - n8n and workflow definitions
- `scripts/` - local helpers for generating drafts and reports
- `.github/workflows/` - scheduled automation entry points

## Human Approval Rule

No content should be published automatically. Every LinkedIn post, comment, recruiter message, portfolio update, and resume change should move through draft, review, and approved states.

## Quick Start

1. Fill in `career/profile.md`, `career/resume.md`, `career/projects.md`, and `career/metrics.md`.
2. For a guided setup, start with `intake/README.md` and complete the career intake forms.
3. Check whether the intake is ready:

```powershell
python scripts/check_career_intake.py
```

4. Use `templates/linkedin-post.md` to draft the first seven posts.
5. Run the weekly content helper:

```powershell
python scripts/generate_content_calendar.py
```

6. Review drafts in `linkedin/posts/`.
7. Add performance numbers to `analytics/linkedin_metrics.csv`.
8. Generate a weekly analytics report:

```powershell
python scripts/generate_weekly_report.py
```

## MVP Status

Phase 1 is implemented as a local repository scaffold with starter docs, templates, prompts, agent specs, analytics tracking, simple generation scripts, and a guided career intake system.

## Current Next Step

The repo is now ready for the content automation phase.

Start here:

- `linkedin/content-system/content-approval-workflow.md`
- `linkedin/content-system/first-30-day-plan.md`
- `templates/linkedin-approval-post.md`

Check content pipeline status:

```powershell
python scripts/content_status_report.py
```
