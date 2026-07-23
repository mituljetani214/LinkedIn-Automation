from pathlib import Path


POST_ROOT = Path("linkedin/posts")
FOLDERS = ["drafts", "review", "approved", "published", "rejected"]


def count_markdown(folder: Path) -> int:
    if not folder.exists():
        return 0
    return len([path for path in folder.glob("*.md") if path.is_file()])


def main() -> None:
    print("LinkedIn content status\n")
    total = 0
    for folder_name in FOLDERS:
        folder = POST_ROOT / folder_name
        count = count_markdown(folder)
        total += count
        print(f"- {folder_name}: {count}")
    print(f"\nTotal tracked post files: {total}")

    approved = count_markdown(POST_ROOT / "approved")
    if approved:
        print("\nApproved posts are ready for manual LinkedIn publishing.")
    else:
        print("\nNo approved posts yet. Move reviewed posts into linkedin/posts/approved/ after approval.")


if __name__ == "__main__":
    main()

