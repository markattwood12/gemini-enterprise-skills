#!/usr/bin/env python3
"""Publishes skills to the Google Cloud Skill Registry (or exports standalone .zip archives)."""

import argparse
import base64
import io
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

from validate_skills import get_skill_files, parse_frontmatter, validate_skill

API_BASE = "https://discoveryengine.googleapis.com/v1beta1"


def get_access_token() -> str:
    """Retrieves an access token from environment or gcloud CLI."""
    if token := (os.environ.get("GOOGLE_OAUTH_ACCESS_TOKEN") or os.environ.get("CLOUDSDK_AUTH_ACCESS_TOKEN")):
        return token.strip()
    res = subprocess.run(["gcloud", "auth", "print-access-token"], capture_output=True, text=True, check=True)
    return res.stdout.strip()


def build_zip_bytes(skill_dir: Path) -> bytes:
    """Validates and packs a skill directory into an in-memory ZIP archive."""
    if errs := validate_skill(skill_dir):
        raise ValueError("; ".join(errs))

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in get_skill_files(skill_dir):
            zf.write(f, f.relative_to(skill_dir))
    return buf.getvalue()


def api_request(method: str, url: str, project: str, token: str, payload: dict) -> dict:
    """Sends an authenticated JSON request to the Discovery Engine API."""
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Goog-User-Project": project,
        },
        method=method,
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def publish_skill(skill_dir: Path, project: str | None, location: str, export_zip: Path | None, dry_run: bool):
    skill_id, description = parse_frontmatter(skill_dir)
    zip_bytes = build_zip_bytes(skill_dir)

    if export_zip:
        export_zip.mkdir(parents=True, exist_ok=True)
        out = export_zip / f"{skill_id}.zip"
        out.write_bytes(zip_bytes)
        print(f"✅ Exported {out} ({len(zip_bytes) / 1024:.1f} KB)")
        if not project:
            return

    parent = f"projects/{project}/locations/{location}"
    resource = f"{parent}/skills/{skill_id}"
    payload = {
        "displayName": skill_id,
        "description": description,
        "content": base64.b64encode(zip_bytes).decode("utf-8"),
        "labels": {"managed-by": "gemini-enterprise-skills-catalog"},
    }

    print(f"📦 Publishing '{skill_id}' -> {resource} ({len(zip_bytes) / 1024:.1f} KB)")
    if dry_run:
        print("   🔍 Dry-run: payload validated in memory.")
        return

    token = get_access_token()
    try:
        data = api_request("POST", f"{API_BASE}/{parent}/skills?skillId={skill_id}", project, token, payload)
    except urllib.error.HTTPError as e:
        if e.code != 409:
            sys.exit(f"   ❌ HTTP {e.code}: {e.read().decode('utf-8')}")
        print(f"   ℹ️ Skill '{skill_id}' exists; creating new revision...")
        data = api_request("PATCH", f"{API_BASE}/{resource}?updateMask=content,description", project, token, payload)

    print(f"   ✅ Published: {data.get('name', resource)} (Revision: {data.get('revision', 'latest')})")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--project", help="Google Cloud project ID")
    p.add_argument("--location", default="global", help="Google Cloud location (default: global)")
    p.add_argument("--skill", help="Specific skill folder name (default: all)")
    p.add_argument("--export-zip", type=Path, help="Directory to export standalone .zip archive")
    p.add_argument("--dry-run", action="store_true", help="Validate and build payload without calling the API")
    args = p.parse_args()

    if not args.project and not args.export_zip:
        p.error("Specify --project or --export-zip.")

    skills_dir = Path(__file__).resolve().parent.parent / "skills"
    skills = [skills_dir / args.skill] if args.skill else sorted(
        d for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith(".")
    )

    for s in skills:
        publish_skill(s, args.project, args.location, args.export_zip, args.dry_run)


if __name__ == "__main__":
    main()
