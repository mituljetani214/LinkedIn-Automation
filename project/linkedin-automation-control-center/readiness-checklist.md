# Readiness Checklist

Status: ready except Cloudinary upload credential
Last updated: 2026-07-27

## Ready

- Repo structure exists.
- Content lifecycle folders exist.
- Content generation plan exists.
- Writing voice intake exists.
- Project intake exists.
- Notion database is reachable.
- Notion sync scripts exist.
- Buffer connector exposes account, channel, idea, post, and analytics tools.
- Buffer organization is connected: My Organization.
- Buffer LinkedIn channel is connected: Mitul Jetani.
- Cloudinary folder name is defined: `Linkedin Automation`.

## Needs Setup

- Add `CLOUDINARY_API_SECRET` to local `.env`, or create an unsigned upload preset.
- Confirm Buffer organization and LinkedIn channel before scheduling.
- Decide the default posting schedule.
- Decide whether approved posts first become Buffer ideas or scheduled posts.

## Human Approval Gates

- Content approval before image generation.
- Image approval before Cloudinary upload.
- Final package approval before Buffer scheduling.
- Explicit confirmation before immediate publishing.

## Current Recommendation

Use this workflow first:

1. Draft content in repo.
2. Sync content into Notion.
3. Approve content in Notion.
4. Generate image.
5. Approve image.
6. Upload image to Cloudinary.
7. Create Buffer idea.
8. Schedule after final review.
