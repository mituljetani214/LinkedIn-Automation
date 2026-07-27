# Notion Sync Setup

Status: ready for manual setup
Last updated: 2026-07-24

## Goal

Use Notion as the LinkedIn content dashboard while the repository remains the source of truth for markdown post files.

## Setup Steps

1. Open the Notion database:

   https://app.notion.com/p/3a61ac6e1ea78070a906d645e0bf1e77?v=3a61ac6e1ea7806d8c81000ce50ea77a&source=copy_link

2. Add the properties listed in:

   `notion/linkedin-content-database-schema.md`

3. Create `.env` from `.env.example`.

4. Add your Notion internal integration token:

```text
NOTION_API_KEY=secret_xxx
NOTION_LINKEDIN_CONTENT_DATABASE_ID=3a61ac6e1ea78070a906d645e0bf1e77
```

5. Share the `LinkedIn Content OS` database with your Notion integration.

6. Dry-run export:

```powershell
python scripts/export_posts_to_notion.py --dry-run
```

7. Live export:

```powershell
python scripts/export_posts_to_notion.py
```

8. Pull Notion status changes back into folders:

```powershell
python scripts/import_notion_status.py
```

## How Approval Will Work

1. Codex or Claude creates markdown drafts in `linkedin/posts/review/`.
2. `export_posts_to_notion.py` creates Notion rows.
3. You review content in Notion.
4. You set `Status` to `Approved`.
5. `import_notion_status.py` moves the markdown file to `linkedin/posts/approved/`.
6. The next package script can create:
   - image prompt
   - carousel outline
   - posting checklist
   - caption text

## Important

Do not commit `.env`.

Do not store real Notion or LinkedIn tokens in GitHub.

