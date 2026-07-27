from notion_content_sync import export_posts


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Export LinkedIn post files to Notion.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    export_posts(args.dry_run)

