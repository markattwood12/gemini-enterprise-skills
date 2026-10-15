# Gemini Enterprise Skills Catalog

An enterprise repository for managing, validating, and versioning organization-wide skills for Gemini Enterprise and Google Antigravity.

---

## Catalog Overview

This repository serves as the central source of truth for custom skills distributed across our Gemini Enterprise environment.

| Skill Name | Description | Status | Package |
| :--- | :--- | :--- | :--- |
| **`google-developer-documentation-style`** | Enforces the official Google Developer Documentation Style Guide across software docs, API references, CLI guides, and READMEs. | Production (v1.0.0) | `dist/google-developer-documentation-style.zip` |

---

## Prerequisites

To package or validate skills locally, ensure your environment meets the following requirements:

* Python 3.10 or higher
* Git 2.30 or higher

---

## Installing a Skill in Gemini Enterprise

To upload a skill package to your Gemini Enterprise workspace:

1. Download or locate the target skill `.zip` archive from the `dist/` directory (for example, `dist/google-developer-documentation-style.zip`).
2. Open the **Gemini Enterprise** web console.
3. In the left navigation pane, select **Skills**.
4. Click **Create Skill** (or **Add Skill**).
5. Select **Upload Skill** and upload the `.zip` archive.
6. Verify that the skill appears in your workspace catalog.
7. Configure access permissions:
   * Select **Share with Organization** to distribute the skill to all enterprise users.
   * Alternatively, assign the skill to specific organizational groups or departments.

---

## Using Skills in Conversation

Once a skill is installed, users can trigger it using three methods:

* **Slash commands**: Enter `/` in the chat composer to view installed skills, and select the skill name (for example, `/google-developer-documentation-style`).
* **Direct mentions**: Enter `@SkillName` followed by your prompt (for example, `@GoogleDocsStyle Review this API reference`).
* **Dynamic detection**: Ask Gemini Enterprise a relevant technical question (for example, *"Audit this README according to developer documentation guidelines"*). Gemini Enterprise automatically activates the skill based on semantic matching with the skill description.

---

## Creating a New Skill

To add a new skill to this repository:

1. Copy the starter template directory:
   ```bash
   cp -r templates/skill-template skills/<YOUR_SKILL_NAME>
   ```
2. Open `skills/<YOUR_SKILL_NAME>/SKILL.md` and edit the YAML frontmatter:
   * Specify a descriptive `name` (use lowercase alphanumeric characters and hyphens).
   * Specify a `description` containing explicit `USE FOR:` and `DO NOT USE FOR:` scope boundaries to avoid accidental invocation.
3. Author your core guidelines in `SKILL.md`.
4. Place detailed guidance, examples, or checklists into the `references/` directory.
5. Verify compliance using the local validation tool:
   ```bash
   python3 scripts/validate_skills.py
   ```
6. Package the skill:
   ```bash
   python3 scripts/package_skills.py --skill <YOUR_SKILL_NAME>
   ```
7. Update `catalog.json` with the new skill metadata.
8. Submit a pull request for review.

---

## Repository Structure

```text
gemini-enterprise-skills/
├── .github/
│   ├── CODEOWNERS                      # Designates governance reviewers
│   └── workflows/
│       ├── validate-skills.yaml        # CI check: validates schema, links, and limits
│       └── package-releases.yaml       # CD: creates release archives on git tags
├── catalog.json                        # Machine-readable registry catalog
├── dist/                               # Prebuilt .zip archives ready for upload
├── scripts/
│   ├── package_skills.py               # Generates Gemini Enterprise-compliant ZIPs
│   └── validate_skills.py              # Validates YAML schema and file count limits
├── templates/
│   └── skill-template/                 # Scaffold template for authoring new skills
└── skills/
    └── google-developer-documentation-style/
        ├── SKILL.md                    # Core orchestrator and golden rules
        └── references/
            ├── api-and-reference-docs.md
            ├── code-and-ui.md
            ├── formatting-and-organization.md
            ├── procedures-and-instructions.md
            ├── voice-and-tone.md
            └── word-list-and-inclusive.md
```

---

## Technical Constraints and Limits

When authoring skills for Gemini Enterprise, observe the following constraints:

* **File count limit**: A skill package must contain **no more than 10 files** total (including `SKILL.md`).
* **Root orchestrator**: `SKILL.md` must be located at the root of the ZIP archive.
* **Progressive disclosure**: Keep routine rules in `SKILL.md` to minimize latency, and delegate deep domain lookups to the `references/` directory.
