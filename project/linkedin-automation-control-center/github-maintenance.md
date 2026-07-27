# GitHub Maintenance Instructions

Status: active
Last updated: 2026-07-27

## Purpose

Keep the repository synchronized so Codex, Claude Code, Notion, Buffer, and future automation agents work from the same source of truth.

## Repo Rules

- Commit only intentional project changes.
- Do not commit `.env` or real credentials.
- Keep generated content in the correct lifecycle folder:
  - `linkedin/posts/drafts/`
  - `linkedin/posts/review/`
  - `linkedin/posts/approved/`
  - `linkedin/posts/published/`
  - `linkedin/posts/rejected/`
- Keep research notes in `research/daily/`.
- Keep project and career truth in `career/` and `intake/`.
- Keep system instructions in `docs/`, `automation/`, `notion/`, and this folder.

## Normal Update Flow

1. Pull the latest GitHub changes.
2. Generate or update content locally.
3. Run the repo status report.
4. Export updated content metadata to Notion.
5. Review the changed files.
6. Commit with a clear message.
7. Push to GitHub.

## Suggested Commit Messages

- `Add LinkedIn automation control center`
- `Add approved content package workflow`
- `Add Cloudinary asset upload helper`
- `Update Notion content sync instructions`

## Manual Push Fallback

If Codex cannot push because Git permission or token access fails, run:

```powershell
git status
git add .
git commit -m "Add LinkedIn automation control center"
git push
```
