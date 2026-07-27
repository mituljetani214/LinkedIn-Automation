# Notion Database Schema: LinkedIn Content OS

Status: setup required
Last updated: 2026-07-24

Database:

https://app.notion.com/p/3a61ac6e1ea78070a906d645e0bf1e77?v=3a61ac6e1ea7806d8c81000ce50ea77a&source=copy_link

## Current Connector Finding

The Notion connector can read the database and confirmed the title:

`LinkedIn Content OS`

At fetch time, the database only had one property:

- `Name`

The connector could not update the schema because Notion returned `object_not_found` for the data source update operation. This usually means the integration can read the page/database view but does not have full schema-edit permission for that database/data source.

Four initial content rows were created with the available `Name` property:

| Post | Notion Page |
| --- | --- |
| AI will not fix a broken workflow. | https://app.notion.com/p/3a61ac6e1ea781458a4ad7c3905f54d9 |
| Design systems matter more in the AI era, not less. | https://app.notion.com/p/3a61ac6e1ea781cc9080c30e587db97e |
| Enterprise UX is not about making dashboards pretty. | https://app.notion.com/p/3a61ac6e1ea78125b245c6319c72a174 |
| Figma is no longer just where designers make screens. | https://app.notion.com/p/3a61ac6e1ea7818b81b4f2a1b2551527 |

## Add These Properties Manually In Notion

Add these exact properties to the `LinkedIn Content OS` database.

| Property | Type | Options / Notes |
| --- | --- | --- |
| `Name` | Title | Already exists |
| `Status` | Select | Idea, Draft, Review, Approved, Packaged, Published, Rejected |
| `Post Date` | Date | Planned publish date |
| `Category` | Select | AI Design, UX, Design Systems, Case Study, Leadership, Enterprise UX |
| `Source` | Select | Munim, Group8A, Research, Personal Story, LinkedIn Profile |
| `Repo File` | Text | Relative repo path, for example `linkedin/posts/review/post.md` |
| `LinkedIn URL` | URL | Add after publishing |
| `Approval` | Checkbox | Checked means Mitul approved |
| `Needs Image` | Checkbox | Checked means create image/carousel asset |
| `Package Ready` | Checkbox | Checked after package is generated |
| `Impressions` | Number | Analytics |
| `Reactions` | Number | Analytics |
| `Comments` | Number | Analytics |
| `Saves` | Number | Analytics |

## Recommended Views

Create these views in Notion:

1. `Pipeline Board`
   - Type: Board
   - Group by: `Status`

2. `Calendar`
   - Type: Calendar
   - Date property: `Post Date`

3. `Needs Approval`
   - Type: Table
   - Filter: `Status` is `Review`

4. `Approved`
   - Type: Table
   - Filter: `Status` is `Approved`

5. `Published`
   - Type: Table
   - Filter: `Status` is `Published`

## Status Mapping

```text
Notion: Draft      -> repo: linkedin/posts/drafts/
Notion: Review     -> repo: linkedin/posts/review/
Notion: Approved   -> repo: linkedin/posts/approved/
Notion: Packaged   -> repo: linkedin/posts/packages/
Notion: Published  -> repo: linkedin/posts/published/
Notion: Rejected   -> repo: linkedin/posts/rejected/
```

## Safety Rule

Notion is the approval/status dashboard.

The repo remains the editable source for full markdown post files.
