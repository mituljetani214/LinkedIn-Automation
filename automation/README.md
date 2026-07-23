# Automation

This folder stores workflow definitions and notes.

## Current V1 Automation

- GitHub Actions can run local report scripts on a schedule.
- n8n workflow definitions can be added under `automation/n8n/`.
- Publishing and recruiter outreach remain human-approved.
- LinkedIn content now follows the approval workflow in `linkedin/content-system/content-approval-workflow.md`.

## Recommended n8n Flow

1. Schedule trigger
2. Collect RSS or source links
3. Summarize research
4. Save markdown report
5. Generate content draft
6. Send draft for review
7. Wait for human approval
8. Mark approved content for publishing

## Human Approval Content Flow

Use this flow before publishing:

```text
linkedin/posts/drafts/
  -> linkedin/posts/review/
  -> linkedin/posts/approved/
  -> manual LinkedIn post
  -> linkedin/posts/published/
  -> analytics/linkedin_metrics.csv
```

The system should never post automatically in V1.
