from notion_content_sync import import_statuses


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Import Notion statuses and move local post files.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    import_statuses(args.dry_run)

