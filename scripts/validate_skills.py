#!/usr/bin/env python3
"""Validates skill packages for Gemini Enterprise compliance."""

import re
import sys
from pathlib import Path

MAX_FILES = 10


def get_skill_files(skill_dir: Path) -> list[Path]:
    """Returns all non-hidden files inside a skill directory."""
    return [
        f for f in skill_dir.rglob("*")
        if f.is_file() and not f.name.startswith(".") and not f.name.endswith(".pyc")
    ]


def parse_frontmatter(skill_dir: Path) -> tuple[str, str]:
    """Extracts (name, description) from SKILL.md YAML frontmatter."""
    content = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    if not content.startswith("---"):
        raise ValueError("Missing opening YAML frontmatter '---'")
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Malformed YAML frontmatter")

    fm = parts[1]
    name_m = re.search(r"^name:\s*([\w\.\-]+)", fm, re.MULTILINE)
    desc_m = re.search(r"^description:\s*(?:>-\s*|\s*)(.+?)(?=\n[a-zA-Z0-9_-]+:|\Z)", fm, re.MULTILINE | re.DOTALL)
    if not name_m:
        raise ValueError("Missing or invalid 'name' in YAML frontmatter")
    if not desc_m:
        raise ValueError("Missing 'description' in YAML frontmatter")
    return name_m.group(1).strip(), desc_m.group(1).strip()


def validate_skill(skill_dir: Path) -> list[str]:
    """Returns a list of validation errors for a skill directory (empty if valid)."""
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [f"{skill_dir.name}: Missing root SKILL.md"]

    errors = []
    files = get_skill_files(skill_dir)
    if len(files) > MAX_FILES:
        errors.append(f"{skill_dir.name}: {len(files)} files exceeds limit of {MAX_FILES}")

    try:
        _, desc = parse_frontmatter(skill_dir)
        if "USE FOR:" not in desc or "DO NOT USE FOR:" not in desc:
            errors.append(f"{skill_dir.name}: Description must include 'USE FOR:' and 'DO NOT USE FOR:'")
    except ValueError as e:
        errors.append(f"{skill_dir.name}: {e}")

    content = skill_file.read_text(encoding="utf-8")
    for link in re.findall(r"\[.*?\]\((references/[^\)]+)\)", content):
        if not (skill_dir / link).exists():
            errors.append(f"{skill_dir.name}: Broken reference link -> {link}")

    return errors


def main():
    skills_dir = Path(__file__).resolve().parent.parent / "skills"
    skills = sorted(d for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith("."))

    print(f"🔍 Validating {len(skills)} skill package(s)...")
    all_errors = []
    for s in skills:
        if errs := validate_skill(s):
            all_errors.extend(errs)
            for e in errs:
                print(f"  ❌ {e}", file=sys.stderr)
        else:
            print(f"  ✅ {s.name} ({len(get_skill_files(s))}/{MAX_FILES} files)")

    if all_errors:
        sys.exit(f"\n❌ Validation failed with {len(all_errors)} error(s).")
    print("\n🎉 All skills passed validation!")


if __name__ == "__main__":
    main()
