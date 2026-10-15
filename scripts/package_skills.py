#!/usr/bin/env python3
"""
Packages skills into clean, compliant ZIP archives ready for upload to Gemini Enterprise.
Rules:
- SKILL.md MUST reside at the root of the ZIP file.
- Total files inside the ZIP must not exceed 10.
- Output archives are written to dist/<skill_name>.zip.
"""

import sys
import argparse
import zipfile
from pathlib import Path

MAX_FILES_LIMIT = 10

def package_skill(skill_dir: Path, output_dir: Path) -> Path:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        raise FileNotFoundError(f"{skill_dir.name} is missing SKILL.md at root.")

    files_to_pack = [
        f for f in skill_dir.rglob("*")
        if f.is_file() and not f.name.startswith(".") and not f.name.endswith(".pyc")
    ]

    if len(files_to_pack) > MAX_FILES_LIMIT:
        raise ValueError(
            f"Cannot package {skill_dir.name}: has {len(files_to_pack)} files, exceeding Gemini Enterprise limit of {MAX_FILES_LIMIT}."
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / f"{skill_dir.name}.zip"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_pack:
            # relative path inside the zip archive ensures SKILL.md is at root
            arcname = file.relative_to(skill_dir)
            zipf.write(file, arcname)

    return zip_path

def main():
    parser = argparse.ArgumentParser(description="Package skills for Gemini Enterprise upload.")
    parser.add_argument("--skill", help="Name of a specific skill to package (default: all)")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"
    dist_dir = repo_root / "dist"

    if args.skill:
        target = skills_dir / args.skill
        if not target.exists() or not target.is_dir():
            print(f"Error: skill '{args.skill}' not found in {skills_dir}", file=sys.stderr)
            sys.exit(1)
        skills = [target]
    else:
        skills = [d for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith(".")]

    print(f"📦 Packaging {len(skills)} skill(s) into {dist_dir}...")
    for s in skills:
        try:
            zip_out = package_skill(s, dist_dir)
            file_size_kb = zip_out.stat().st_size / 1024
            print(f"  ✅ Built: {zip_out.name} ({file_size_kb:.1f} KB)")
        except Exception as e:
            print(f"  ❌ Failed to package {s.name}: {e}", file=sys.stderr)
            sys.exit(1)

    print("\n🎉 Packaging complete! ZIP files are ready for upload to Gemini Enterprise.")

if __name__ == "__main__":
    main()
