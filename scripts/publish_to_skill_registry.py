#!/usr/bin/env python3
"""
Publishes skills directly to the Google Cloud Skill Registry in Gemini Enterprise Agent Platform.
Resource hierarchy: projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}

Also supports --export-zip for air-gapped environments that require a standalone archive.
"""

import argparse
import base64
import io
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

DEFAULT_LOCATION = "global"
MAX_FILES_LIMIT = 10


def get_access_token() -> str:
    """Retrieves an access token using gcloud or GOOGLE_OAUTH_ACCESS_TOKEN."""
    token = os.environ.get("GOOGLE_OAUTH_ACCESS_TOKEN") or os.environ.get("CLOUDSDK_AUTH_ACCESS_TOKEN")
    if token:
        return token.strip()
    try:
        result = subprocess.run(
            ["gcloud", "auth", "print-access-token"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception as e:
        raise RuntimeError(
            "Could not obtain Google Cloud access token. Run 'gcloud auth login' or set GOOGLE_OAUTH_ACCESS_TOKEN."
        ) from e


def build_zip_payload(skill_dir: Path) -> bytes:
    """Builds an in-memory zip archive of the skill directory with SKILL.md at root."""
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        raise FileNotFoundError(f"Missing root SKILL.md in {skill_dir}")

    files_to_pack = [
        f for f in skill_dir.rglob("*")
        if f.is_file() and not f.name.startswith(".") and not f.name.endswith(".pyc")
    ]
    if len(files_to_pack) > MAX_FILES_LIMIT:
        raise ValueError(
            f"Skill '{skill_dir.name}' contains {len(files_to_pack)} files, exceeding the limit of {MAX_FILES_LIMIT}."
        )

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_pack:
            arcname = file.relative_to(skill_dir)
            zipf.write(file, arcname)
    return buffer.getvalue()


def parse_frontmatter(skill_dir: Path) -> tuple[str, str]:
    """Extracts skill name and description from SKILL.md frontmatter."""
    content = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Malformed YAML frontmatter in SKILL.md")
    frontmatter = parts[1]

    name_match = re.search(r"^name:\s*([\w\.\-]+)", frontmatter, re.MULTILINE)
    desc_match = re.search(r"^description:\s*(?:>-\s*|\s*)(.+?)(?=\n\w+:|$)", frontmatter, re.MULTILINE | re.DOTALL)

    name = name_match.group(1).strip() if name_match else skill_dir.name
    desc = desc_match.group(1).strip() if desc_match else ""
    return name, desc


def publish_skill(
    skill_dir: Path,
    project: str | None = None,
    location: str = DEFAULT_LOCATION,
    export_zip_dir: Path | None = None,
    dry_run: bool = False,
):
    skill_id, description = parse_frontmatter(skill_dir)
    zip_bytes = build_zip_payload(skill_dir)

    if export_zip_dir:
        export_zip_dir.mkdir(parents=True, exist_ok=True)
        out_path = export_zip_dir / f"{skill_id}.zip"
        out_path.write_bytes(zip_bytes)
        print(f"✅ Exported archive: {out_path} ({len(zip_bytes) / 1024:.1f} KB)")
        if not project:
            return

    if not project:
        raise ValueError("Provide --project to publish to Google Cloud Skill Registry, or --export-zip to export locally.")

    encoded_content = base64.b64encode(zip_bytes).decode("utf-8")
    parent = f"projects/{project}/locations/{location}"
    skill_resource = f"{parent}/skills/{skill_id}"
    api_endpoint = f"https://discoveryengine.googleapis.com/v1beta1/{parent}/skills?skillId={skill_id}"

    payload = {
        "displayName": skill_id,
        "description": description,
        "content": encoded_content,
        "labels": {
            "managed-by": "gemini-enterprise-skills-catalog",
            "source-repo": "github",
        },
    }

    print(f"📦 Publishing '{skill_id}' to Skill Registry:")
    print(f"   Target: {skill_resource}")
    print(f"   Bundle Size: {len(zip_bytes) / 1024:.1f} KB")

    if dry_run:
        print("   🔍 Dry-run mode: Payload validated and prepared in memory. Skipping API request.")
        return

    token = get_access_token()
    req = urllib.request.Request(
        api_endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Goog-User-Project": project,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"   ✅ Registered skill: {data.get('name', skill_resource)}")
            if "revision" in data:
                print(f"   📌 Immutable Revision: {data['revision']}")
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8")
        if e.code == 409:
            print(f"   ℹ️ Skill '{skill_id}' exists. Updating content and creating new revision...")
            update_endpoint = f"https://discoveryengine.googleapis.com/v1beta1/{skill_resource}?updateMask=content,description"
            patch_req = urllib.request.Request(
                update_endpoint,
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "X-Goog-User-Project": project,
                },
                method="PATCH",
            )
            with urllib.request.urlopen(patch_req) as patch_resp:
                patch_data = json.loads(patch_resp.read().decode("utf-8"))
                print(f"   ✅ Updated skill: {patch_data.get('name', skill_resource)}")
                if "revision" in patch_data:
                    print(f"   📌 New Immutable Revision: {patch_data['revision']}")
        else:
            print(f"   ❌ HTTP {e.code} Error: {err_body}", file=sys.stderr)
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Publish skills to Google Cloud Skill Registry.")
    parser.add_argument("--project", help="Google Cloud project ID")
    parser.add_argument("--location", default=DEFAULT_LOCATION, help=f"Google Cloud location (default: {DEFAULT_LOCATION})")
    parser.add_argument("--skill", help="Specific skill name in skills/ to publish (default: all)")
    parser.add_argument("--export-zip", type=Path, help="Optional directory to export standalone .zip archive for manual upload")
    parser.add_argument("--dry-run", action="store_true", help="Validate and build payload in memory without calling the API")
    args = parser.parse_args()

    if not args.project and not args.export_zip:
        parser.error("Specify --project (for Skill Registry publishing) or --export-zip (for standalone archive export).")

    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"

    if args.skill:
        target = skills_dir / args.skill
        if not target.exists() or not target.is_dir():
            print(f"Error: skill '{args.skill}' not found in {skills_dir}", file=sys.stderr)
            sys.exit(1)
        skills = [target]
    else:
        skills = [d for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith(".")]

    for s in skills:
        publish_skill(
            s,
            project=args.project,
            location=args.location,
            export_zip_dir=args.export_zip,
            dry_run=args.dry_run,
        )

    print("\n🎉 Operation completed.")


if __name__ == "__main__":
    main()
