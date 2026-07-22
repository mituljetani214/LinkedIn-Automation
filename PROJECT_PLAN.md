# Project Plan

## Objective

Create a Personal AI Career Assistant that helps Mitul Jetani grow LinkedIn presence, manage career knowledge, build portfolio assets, find opportunities, learn from analytics, and improve positioning over time.

## Scope

This project starts as a free-first local and GitHub-based operating system. It can later connect to Notion, Google Sheets, Figma, Google Drive, LinkedIn analytics exports, and n8n Community Edition.

## Architecture

```text
Internet
  -> Research Agent
  -> Knowledge Base
  -> Content Engine
  -> Image Engine
  -> LinkedIn Draft
  -> Human Review
  -> Publish
  -> Analytics
  -> Learning
  -> Improvement
```

## Operating Workflow

1. Career Brain stores source-of-truth career facts.
2. Research Agent collects trends and inspiration.
3. Content Agent converts research and career facts into drafts.
4. Human reviews and approves drafts.
5. Analytics Agent tracks performance.
6. Learning System updates topics, hooks, timing, and CTA recommendations.

## MVP Deliverables

- Repository structure
- Career knowledge files
- Career intake system
- Agent specifications
- Prompt library
- LinkedIn content templates
- Research report template
- Analytics CSV and weekly report generator
- GitHub Actions workflow placeholders
- n8n workflow notes

## Non-Goals For V1

- Auto-posting to LinkedIn
- Scraping private LinkedIn pages
- Sending recruiter messages without review
- Storing secrets in the repository
- Replacing human judgment
