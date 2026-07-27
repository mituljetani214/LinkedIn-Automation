# Buffer Publishing Workflow

Status: connected and available after approval
Last updated: 2026-07-27

## Goal

Move approved LinkedIn content packages into Buffer so Mitul can schedule or publish with confidence.

## Verified Connection

- Buffer organization: My Organization
- LinkedIn channel: Mitul Jetani
- Channel status: connected

## Buffer Rule

Do not publish immediately unless Mitul explicitly asks for immediate publishing and confirms the final preview.

Preferred flow:

1. Create Buffer idea for approved content.
2. Attach Cloudinary asset URL when available.
3. Confirm LinkedIn channel.
4. Schedule with `addToQueue` or a confirmed custom date/time.
5. Store the Buffer ID back in Notion and the repo package.

## Required Package Before Buffer

- Approved post text
- Approved visual URL, if the post needs media
- Alt text
- Target service: LinkedIn
- Target channel ID
- Suggested schedule
- Notion page URL
- Repo file path

## Scheduling Modes

- `addToQueue`: use Buffer's existing schedule.
- `customScheduled`: use a specific approved date and time.
- `shareNext`: next available queue slot.
- `shareNow`: only with explicit confirmation.

## Status Updates

After Buffer accepts a package:

- Set Notion `Status` to `Scheduled`.
- Store Buffer post or idea ID.
- Keep the repo file in `linkedin/posts/approved/` until live.
- Move to `linkedin/posts/published/` after publishing.
