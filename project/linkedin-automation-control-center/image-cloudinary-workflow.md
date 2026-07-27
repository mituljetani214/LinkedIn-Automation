# Image And Cloudinary Workflow

Status: blocked until Cloudinary secret or unsigned preset is added
Last updated: 2026-07-27

## Goal

Generate a visual asset for each approved LinkedIn post, store the approved version in Cloudinary, and attach the Cloudinary URL to Notion and Buffer.

## Image Generation

Use ChatGPT Images 2.0 to create visuals that match the post:

- Single image for text posts.
- Multi-slide carousel for carousel posts.
- Clean product-thinking visuals for UX/product strategy posts.
- Clear hierarchy and high readability for mobile LinkedIn.
- Avoid generic AI robot visuals, dark stock-photo moods, and cluttered text-heavy graphics.

## Required Image Package

Each approved visual package should include:

- Source post file
- Image prompt
- Final asset filename
- Alt text
- Cloudinary public URL
- Notion page URL
- Buffer post or idea ID

## Cloudinary Configuration

The user provided:

- Key name: LinkedIn Automation
- Product environment / cloud name: `yxkladut`
- API key: provided in chat
- Folder: `Linkedin Automation`

Do not commit the API key or secret to GitHub. Store real values in `.env`.

Required local `.env` values:

```text
CLOUDINARY_CLOUD_NAME=yxkladut
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
CLOUDINARY_FOLDER=Linkedin Automation
```

## Important Blocker

Cloudinary signed upload requires an API secret. The API key alone is not enough.

Alternative: create an unsigned upload preset in Cloudinary and add it to `.env` later if we choose an unsigned browser-safe flow.

## Upload Rule

Only upload assets for posts that are approved.

Never upload rejected drafts or early experiments to the production Cloudinary folder.
