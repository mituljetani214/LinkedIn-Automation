# n8n Workflow: Research To Content

Status: design draft

## Nodes

1. Schedule Trigger
2. RSS / HTTP Request for approved sources
3. Extract article title, URL, and summary
4. AI summary node
5. Create research markdown
6. AI content draft node
7. Human review notification
8. Save approved draft

## Human Approval

Do not connect this workflow directly to LinkedIn publishing in V1.

## Data Destinations

- Research notes: `research/daily/`
- Post drafts: `linkedin/posts/`
- Analytics: `analytics/linkedin_metrics.csv`

