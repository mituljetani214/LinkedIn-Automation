# LinkedIn Automation Control Center

Status: ready except Cloudinary upload secret
Last updated: 2026-07-27
Owner: Mitul Jetani

This folder is the operating guide for this chat and the LinkedIn automation project.

The repository remains the source of truth for strategy, drafts, approvals, and generated packages. Notion is the review dashboard. Cloudinary is the approved asset store. Buffer is the publishing and scheduling layer after human approval.

## Core Workflow

1. Maintain the GitHub repository.
2. Generate content from the approved repo plan, career intake, project intake, writing voice, and research.
3. Add every generated content item to the Notion LinkedIn Content OS database.
4. Wait for human review and approval in Notion.
5. Generate the matching image or carousel asset with ChatGPT Images 2.0.
6. Upload only approved assets to Cloudinary under the `Linkedin Automation` folder.
7. Package the approved caption, asset URL, alt text, category, and schedule metadata.
8. Send the ready package to Buffer for LinkedIn scheduling after final approval.
9. Sync final status back into the repo and Notion.

## Source Of Truth

- Career and positioning: `career/` and `intake/`
- Content plan: `linkedin/content-system/`
- Draft posts: `linkedin/posts/review/`
- Approved posts: `linkedin/posts/approved/`
- Published posts: `linkedin/posts/published/`
- Notion setup: `notion/`
- Automation scripts: `scripts/`
- Generated assets: `assets/`

## Readiness

Ready now:

- GitHub repository structure exists.
- Content approval folders exist.
- Notion database is connected and usable.
- Buffer connector is available in this session.
- Buffer has a connected LinkedIn profile for Mitul Jetani.
- Cloudinary cloud name and API key were provided by the user.

Needs one more item before full automation:

- Cloudinary upload requires either `CLOUDINARY_API_SECRET` or an unsigned upload preset. The API key alone is not enough for secure uploads.

## Approval Rule

No content should go to Buffer until it is approved by Mitul in Notion or explicitly approved in chat.

No image should be uploaded to Cloudinary until the related post is approved.

No real credential should be committed to GitHub.
