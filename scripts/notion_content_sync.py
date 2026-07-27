import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
POST_ROOT = ROOT / "linkedin" / "posts"
FOLDERS = {
    "drafts": "Draft",
    "review": "Review",
    "approved": "Approved",
    "published": "Published",
    "rejected": "Rejected",
}
STATUS_TO_FOLDER = {value: key for key, value in FOLDERS.items()}
NOTION_VERSION = "2022-06-28"
DEFAULT_DATABASE_ID = "3a61ac6e1ea78070a906d645e0bf1e77"


def load_env() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def read_post(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    title = text.splitlines()[0].lstrip("# ").strip() if text.splitlines() else path.stem
    hook = find_section(text, "Hook") or title
    category = normalize_category(find_section(text, "Category") or infer_category(path.name))
    scheduled = find_field(text, "Scheduled for") or find_field(text, "Post Date")
    status = find_field(text, "Status") or FOLDERS.get(path.parent.name, "Draft")
    status = normalize_status(status)
    source = infer_source(text)
    needs_image = "__YES__" if "Visual / Carousel Idea" in text else "__NO__"
    return {
        "title": title,
        "hook": hook,
        "category": category,
        "scheduled": scheduled,
        "status": status,
        "source": source,
        "repo_file": str(path.relative_to(ROOT)).replace("\\", "/"),
        "needs_image": needs_image,
        "content": text,
    }


def find_field(text: str, field: str) -> str:
    match = re.search(rf"^{re.escape(field)}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def find_section(text: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if not match:
        return ""
    section = match.group(1).strip()
    return section.splitlines()[0].strip() if section else ""


def normalize_status(status: str) -> str:
    value = status.strip().lower().replace("_", " ")
    mapping = {
        "idea": "Idea",
        "draft": "Draft",
        "needs review": "Review",
        "review": "Review",
        "approved": "Approved",
        "packaged": "Packaged",
        "published": "Published",
        "rejected": "Rejected",
    }
    return mapping.get(value, status.strip().title())


def infer_category(name: str) -> str:
    lowered = name.lower()
    if "design-system" in lowered:
        return "Design Systems"
    if "enterprise" in lowered:
        return "Enterprise UX"
    if "ai" in lowered or "figma" in lowered:
        return "AI Design"
    return "UX"


def normalize_category(category: str) -> str:
    lowered = category.lower()
    if "design system" in lowered:
        return "Design Systems"
    if "enterprise" in lowered:
        return "Enterprise UX"
    if "leadership" in lowered:
        return "Leadership"
    if "case" in lowered:
        return "Case Study"
    if "ai" in lowered or "figma" in lowered:
        return "AI Design"
    return "UX"


def infer_source(text: str) -> str:
    if "research/daily" in text:
        return "Research"
    has_group8a = "Group8A" in text
    has_munim = "Munim" in text
    if has_group8a and not has_munim:
        return "Group8A"
    if has_munim and not has_group8a:
        return "Munim"
    return "Research"


def iter_posts() -> list[Path]:
    paths: list[Path] = []
    for folder in FOLDERS:
        folder_path = POST_ROOT / folder
        if folder_path.exists():
            paths.extend(path for path in folder_path.glob("*.md") if path.name != ".gitkeep")
    return sorted(paths)


def notion_headers() -> dict:
    token = os.environ.get("NOTION_API_KEY", "")
    if not token:
        raise SystemExit("Missing NOTION_API_KEY. Add it to .env or run with --dry-run.")
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }


def notion_request(method: str, url: str, payload: dict | None = None) -> dict:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = Request(url, data=data, headers=notion_headers(), method=method)
    try:
        with urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Notion API error {exc.code}: {body}") from exc
    except URLError as exc:
        raise SystemExit(f"Notion API network error: {exc}") from exc


def notion_query_by_repo_file(database_id: str, repo_file: str) -> str:
    payload = {
        "filter": {
            "property": "Repo File",
            "rich_text": {"equals": repo_file},
        }
    }
    result = notion_request("POST", f"https://api.notion.com/v1/databases/{database_id}/query", payload)
    matches = result.get("results", [])
    return matches[0]["id"] if matches else ""


def notion_page_payload(database_id: str, post: dict) -> dict:
    properties = {
        "Name": {"title": [{"text": {"content": post["hook"][:180]}}]},
        "Status": {"select": {"name": post["status"]}},
        "Category": {"select": {"name": post["category"]}},
        "Source": {"select": {"name": post["source"]}},
        "Repo File": {"rich_text": [{"text": {"content": post["repo_file"]}}]},
        "Approval": {"checkbox": post["status"] in {"Approved", "Packaged", "Published"}},
        "Needs Image": {"checkbox": post["needs_image"] == "__YES__"},
        "Package Ready": {"checkbox": post["status"] in {"Packaged", "Published"}},
    }
    if post["scheduled"]:
        properties["Post Date"] = {"date": {"start": post["scheduled"]}}
    return {
        "parent": {"database_id": database_id},
        "properties": properties,
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Full draft lives in the repo file: "
                                + post["repo_file"]
                            },
                        }
                    ]
                },
            }
        ],
    }


def export_posts(dry_run: bool) -> None:
    load_env()
    database_id = os.environ.get("NOTION_LINKEDIN_CONTENT_DATABASE_ID", DEFAULT_DATABASE_ID)
    if not database_id:
        raise SystemExit("Missing NOTION_LINKEDIN_CONTENT_DATABASE_ID.")
    posts = [read_post(path) for path in iter_posts()]
    if dry_run:
        print(json.dumps(posts, indent=2))
        return
    for post in posts:
        page_id = notion_query_by_repo_file(database_id, post["repo_file"])
        payload = notion_page_payload(database_id, post)
        if page_id:
            notion_request("PATCH", f"https://api.notion.com/v1/pages/{page_id}", {"properties": payload["properties"]})
            print(f"Updated Notion row: {post['repo_file']}")
        else:
            notion_request("POST", "https://api.notion.com/v1/pages", payload)
            print(f"Created Notion row: {post['repo_file']}")


def import_statuses(dry_run: bool) -> None:
    load_env()
    database_id = os.environ.get("NOTION_LINKEDIN_CONTENT_DATABASE_ID", DEFAULT_DATABASE_ID)
    if not database_id:
        raise SystemExit("Missing NOTION_LINKEDIN_CONTENT_DATABASE_ID.")
    result = notion_request("POST", f"https://api.notion.com/v1/databases/{database_id}/query", {})
    for page in result.get("results", []):
        props = page.get("properties", {})
        repo_file = rich_text_value(props.get("Repo File", {}))
        status = select_value(props.get("Status", {}))
        if not repo_file or status not in STATUS_TO_FOLDER:
            continue
        source = ROOT / repo_file
        if not source.exists():
            continue
        target_folder = POST_ROOT / STATUS_TO_FOLDER[status]
        target = target_folder / source.name
        if source == target:
            continue
        print(f"{source.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        if not dry_run:
            target_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(target))


def rich_text_value(prop: dict) -> str:
    return "".join(item.get("plain_text", "") for item in prop.get("rich_text", []))


def select_value(prop: dict) -> str:
    selected = prop.get("select")
    return selected.get("name", "") if selected else ""


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync LinkedIn post files with Notion.")
    parser.add_argument("mode", choices=["export", "import"], help="export posts to Notion or import statuses from Notion")
    parser.add_argument("--dry-run", action="store_true", help="Print planned changes without writing")
    args = parser.parse_args()
    if args.mode == "export":
        export_posts(args.dry_run)
    else:
        import_statuses(args.dry_run)


if __name__ == "__main__":
    main()
