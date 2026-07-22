from pathlib import Path


CHECKS = {
    "intake/master-career-intake.md": [
        "Current role/title:",
        "Years of experience:",
        "Target roles:",
        "Strongest Skills",
        "Portfolio:",
        "Topics you want to be known for:",
    ],
    "intake/linkedin-profile-intake.md": [
        "Current Headline",
        "Current About Section",
        "What should people hire you for?",
        "SEO Keywords",
        "Featured Section Candidates",
    ],
    "intake/writing-voice-intake.md": [
        "How do you usually explain design?",
        "Example Posts You Like",
        "Your Stories",
        "Approved Phrases",
        "Avoid Phrases",
    ],
}


PLACEHOLDERS = {"TODO", "todo", "- TODO", ""}


def section_has_content(text: str, marker: str) -> bool:
    index = text.find(marker)
    if index == -1:
        return False

    if marker.endswith(":"):
        line_end = text.find("\n", index)
        line = text[index: line_end if line_end != -1 else len(text)]
        value = line.split(":", 1)[1].strip()
        return bool(value and value not in PLACEHOLDERS)

    remaining = text[index + len(marker):]
    next_heading = remaining.find("\n##")
    section = remaining if next_heading == -1 else remaining[:next_heading]

    cleaned_lines = [
        line.strip()
        for line in section.splitlines()
        if line.strip() and line.strip() not in PLACEHOLDERS
    ]
    return bool(cleaned_lines)


def main() -> None:
    missing = []

    for file_name, markers in CHECKS.items():
        path = Path(file_name)
        if not path.exists():
            missing.append(f"{file_name}: file missing")
            continue

        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if not section_has_content(text, marker):
                missing.append(f"{file_name}: fill `{marker}`")

    project_files = [
        path
        for path in Path("intake").glob("project-*.md")
        if path.name != "project-intake-template.md"
    ]

    if len(project_files) < 2:
        missing.append(
            "intake/: add at least 2 project intake files copied from project-intake-template.md"
        )

    if missing:
        print("Career intake is not complete yet.\n")
        for item in missing:
            print(f"- {item}")
        raise SystemExit(1)

    print("Career intake looks ready for LinkedIn profile optimization.")


if __name__ == "__main__":
    main()
