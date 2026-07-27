"""Upload an approved asset to Cloudinary using local .env credentials.

This helper intentionally refuses to run without CLOUDINARY_API_SECRET because
signed uploads are the safest server-side default for this repo.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import time
import urllib.request
from pathlib import Path
from uuid import uuid4


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def sign(params: dict[str, str], api_secret: str) -> str:
    payload = "&".join(f"{key}={params[key]}" for key in sorted(params) if params[key])
    return hashlib.sha1(f"{payload}{api_secret}".encode("utf-8")).hexdigest()


def multipart_form(fields: dict[str, str], file_path: Path) -> tuple[bytes, str]:
    boundary = f"----codex-cloudinary-{uuid4().hex}"
    content_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    chunks: list[bytes] = []

    for key, value in fields.items():
        chunks.append(f"--{boundary}\r\n".encode())
        chunks.append(f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode())
        chunks.append(f"{value}\r\n".encode())

    chunks.append(f"--{boundary}\r\n".encode())
    chunks.append(
        (
            f'Content-Disposition: form-data; name="file"; filename="{file_path.name}"\r\n'
            f"Content-Type: {content_type}\r\n\r\n"
        ).encode()
    )
    chunks.append(file_path.read_bytes())
    chunks.append(f"\r\n--{boundary}--\r\n".encode())
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Upload an approved LinkedIn asset to Cloudinary.")
    parser.add_argument("asset", help="Path to the approved image or document asset.")
    parser.add_argument("--public-id", help="Optional Cloudinary public ID.")
    parser.add_argument("--dry-run", action="store_true", help="Validate configuration without uploading.")
    args = parser.parse_args()

    load_dotenv(Path(".env"))

    asset = Path(args.asset)
    if not asset.exists():
        raise SystemExit(f"Asset not found: {asset}")

    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME")
    api_key = os.getenv("CLOUDINARY_API_KEY")
    api_secret = os.getenv("CLOUDINARY_API_SECRET")
    folder = os.getenv("CLOUDINARY_FOLDER", "Linkedin Automation")

    missing = [
        name
        for name, value in {
            "CLOUDINARY_CLOUD_NAME": cloud_name,
            "CLOUDINARY_API_KEY": api_key,
            "CLOUDINARY_API_SECRET": api_secret,
        }.items()
        if not value
    ]
    if missing:
        raise SystemExit(f"Missing required environment values: {', '.join(missing)}")

    timestamp = str(int(time.time()))
    params = {
        "folder": folder,
        "public_id": args.public_id or asset.stem,
        "timestamp": timestamp,
    }
    signature = sign(params, api_secret or "")

    if args.dry_run:
        print(
            json.dumps(
                {
                    "ready": True,
                    "asset": str(asset),
                    "cloud_name": cloud_name,
                    "folder": folder,
                    "public_id": params["public_id"],
                },
                indent=2,
            )
        )
        return 0

    fields = {
        **params,
        "api_key": api_key or "",
        "signature": signature,
    }
    body, content_type = multipart_form(fields, asset)
    request = urllib.request.Request(
        f"https://api.cloudinary.com/v1_1/{cloud_name}/auto/upload",
        data=body,
        headers={"Content-Type": content_type},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        print(response.read().decode("utf-8"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
