from datetime import date, timedelta
from pathlib import Path


THEMES = [
    ("Monday", "Design Systems"),
    ("Tuesday", "UX Psychology"),
    ("Wednesday", "AI"),
    ("Thursday", "Case Study"),
    ("Friday", "Career"),
    ("Saturday", "Portfolio"),
    ("Sunday", "Personal Story"),
]


def next_monday(today: date) -> date:
    days_ahead = (0 - today.weekday()) % 7
    return today + timedelta(days=days_ahead)


def main() -> None:
    start = next_monday(date.today())
    output_dir = Path("linkedin/posts")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"content-calendar-{start.isoformat()}.md"

    lines = [
        f"# Weekly LinkedIn Content Calendar: {start.isoformat()}",
        "",
        "Status: draft",
        "",
    ]

    for index, (day_name, theme) in enumerate(THEMES):
        post_date = start + timedelta(days=index)
        lines.extend(
            [
                f"## {day_name}, {post_date.isoformat()}: {theme}",
                "",
                "- Hook:",
                "- Story / context:",
                "- Practical takeaway:",
                "- CTA:",
                "- Source material:",
                "- Approval status: draft",
                "",
            ]
        )

    output_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"Created {output_file}")


if __name__ == "__main__":
    main()

