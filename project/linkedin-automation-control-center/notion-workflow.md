# Notion Workflow Instructions

Status: active
Last updated: 2026-07-27

## Database

Name: LinkedIn Content OS

Database URL:

https://app.notion.com/p/3a61ac6e1ea78070a906d645e0bf1e77?v=3a61ac6e1ea7806d8c81000ce50ea77a&source=copy_link

## Purpose

Notion is the human approval dashboard. It should show what is drafted, what needs edits, what is approved, what needs an image, and what is ready for Buffer.

## Required Properties

- Name
- Status
- Post Date
- Category
- Source
- Repo File
- LinkedIn URL
- Approval
- Needs Image
- Package Ready
- Impressions
- Reactions
- Comments
- Saves

## Status Meaning

- `Review`: draft is ready for human review.
- `Needs Edits`: content needs revision.
- `Approved`: content is approved for packaging.
- `Packaged`: caption and approved asset are ready for Buffer.
- `Published`: post is live.
- `Rejected`: do not publish.

## Automation Rule

The repo creates and updates the content. Notion reflects the current review state.

When a content item is generated:

1. Create or update a Notion row.
2. Add the full post content inside the Notion page body.
3. Set `Status` to `Review`.
4. Set `Needs Image` based on the content type.
5. Set `Approval` to unchecked.

When Mitul approves:

1. Set `Approval` to checked.
2. Set `Status` to `Approved`.
3. Generate the matching visual package.
4. Upload the approved asset to Cloudinary.
5. Set `Package Ready` to checked after the Cloudinary URL is attached.
6. Set `Status` to `Packaged` when the post is ready for Buffer.
