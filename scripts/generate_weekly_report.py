import csv
from collections import defaultdict
from datetime import date
from pathlib import Path


METRICS_FILE = Path("analytics/linkedin_metrics.csv")
REPORT_DIR = Path("analytics/reports")


def to_int(value: str) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def main() -> None:
    if not METRICS_FILE.exists():
        raise SystemExit("Missing analytics/linkedin_metrics.csv")

    with METRICS_FILE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        raise SystemExit("No metric rows found")

    totals = defaultdict(int)
    by_category = defaultdict(lambda: defaultdict(int))

    metric_fields = [
        "impressions",
        "reactions",
        "comments",
        "shares",
        "saves",
        "profile_views",
        "connection_requests",
    ]

    for row in rows:
        category = row.get("category", "Uncategorized") or "Uncategorized"
        for field in metric_fields:
            value = to_int(row.get(field, "0"))
            totals[field] += value
            by_category[category][field] += value

    best_post = max(rows, key=lambda row: to_int(row.get("impressions", "0")))
    best_category = max(
        by_category.items(),
        key=lambda item: item[1]["impressions"],
    )[0]

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / f"weekly-report-{date.today().isoformat()}.md"

    lines = [
        f"# Weekly Analytics Report: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Posts tracked: {len(rows)}",
        f"- Total impressions: {totals['impressions']}",
        f"- Total reactions: {totals['reactions']}",
        f"- Total comments: {totals['comments']}",
        f"- Total shares: {totals['shares']}",
        f"- Total saves: {totals['saves']}",
        f"- Profile views: {totals['profile_views']}",
        f"- Connection requests: {totals['connection_requests']}",
        "",
        "## Best Performing Post",
        "",
        f"- Post ID: {best_post.get('post_id', '')}",
        f"- Category: {best_post.get('category', '')}",
        f"- Hook: {best_post.get('hook', '')}",
        f"- Impressions: {best_post.get('impressions', '0')}",
        "",
        "## Best Category",
        "",
        f"- {best_category}",
        "",
        "## Recommendations",
        "",
        "- Repurpose the best post into a carousel or case-study thread.",
        "- Write one follow-up post that expands the strongest comment discussion.",
        "- Test one new CTA next week and compare profile views.",
        "",
        "## Category Breakdown",
        "",
    ]

    for category, metrics in sorted(by_category.items()):
        lines.extend(
            [
                f"### {category}",
                "",
                f"- Impressions: {metrics['impressions']}",
                f"- Reactions: {metrics['reactions']}",
                f"- Comments: {metrics['comments']}",
                f"- Saves: {metrics['saves']}",
                "",
            ]
        )

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Created {report_path}")


if __name__ == "__main__":
    main()

