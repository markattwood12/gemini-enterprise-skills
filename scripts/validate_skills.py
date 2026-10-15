#!/usr/bin/env python3
"""
Validates skill packages for Gemini Enterprise compliance.
Checks:
1. SKILL.md exists in root.
2. YAML frontmatter contains required fields ('name', 'description').
3. Frontmatter description contains scoping bounds ('USE FOR:', 'DO NOT USE FOR:').
4. Total file count does not exceed 10 files (Gemini Enterprise limit).
5. All references cited in SKILL.md exist on disk.
"""

import sys
import re
from pathlib import Path

MAX_FILES_PER_SKILL = 10

def validate_skill(skill_dir: Path) -> list[str]:
    errors = []
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        return [f"{skill_dir.name}: Missing root SKILL.md"]

    # Check total files count
    all_files = [f for f in skill_dir.rglob("*") if f.is_file() and not f.name.startswith(".")]
    if len(all_files) > MAX_FILES_PER_SKILL:
        errors.append(
            f"{skill_dir.name}: Contains {len(all_files)} files, which exceeds the Gemini Enterprise limit of {MAX_FILES_PER_SKILL} files."
        )

    content = skill_file.read_text(encoding="utf-8")

    # Frontmatter check
    if not content.startswith("---"):
        errors.append(f"{skill_dir.name}: SKILL.md missing opening YAML frontmatter '---'")
        return errors

    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{skill_dir.name}: SKILL.md has malformed YAML frontmatter")
        return errors

    frontmatter = parts[1]

    # Check required fields
    if not re.search(r"^name:\s*[\w\.\-]+", frontmatter, re.MULTILINE):
        errors.append(f"{skill_dir.name}: Missing or invalid 'name' in YAML frontmatter")

    if not re.search(r"^description:", frontmatter, re.MULTILINE):
        errors.append(f"{skill_dir.name}: Missing 'description' in YAML frontmatter")
    else:
        if "USE FOR:" not in frontmatter or "DO NOT USE FOR:" not in frontmatter:
            errors.append(
                f"{skill_dir.name}: Description should include explicit 'USE FOR:' and 'DO NOT USE FOR:' scope boundaries."
            )

    # Check reference links
    ref_links = re.findall(r"\[.*?\]\((references/[^\)]+)\)", content)
    for link in ref_links:
        target = skill_dir / link
        if not target.exists():
            errors.append(f"{skill_dir.name}: Broken reference link in SKILL.md -> {link}")

    return errors

def main():
    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"

    if not skills_dir.exists():
        print(f"Error: skills directory not found at {skills_dir}", file=sys.stderr)
        sys.exit(1)

    skill_folders = [d for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith(".")]
    if not skill_folders:
        print("No skills found to validate.")
        sys.exit(0)

    total_errors = []
    print(f"🔍 Validating {len(skill_folders)} skill package(s)...")

    for skill in skill_folders:
        errs = validate_skill(skill)
        if errs:
            for e in errs:
                print(f"  ❌ {e}", file=sys.stderr)
            total_errors.extend(errs)
        else:
            files_count = len([f for f in skill.rglob('*') if f.is_file() and not f.name.startswith('.')])
            print(f"  ✅ {skill.name} (Valid: {files_count}/{MAX_FILES_PER_SKILL} files)")

    if total_errors:
        print(f"\n❌ Validation failed with {len(total_errors)} error(s).", file=sys.stderr)
        sys.exit(1)
    else:
        print("\n🎉 All skills passed validation successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
