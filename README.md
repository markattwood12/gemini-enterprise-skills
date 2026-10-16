# Gemini Enterprise skills catalog

This repository is the central monorepo for authoring, validating, versioning, and publishing organization-wide skills to the **Google Cloud Skill Registry** for **Gemini Enterprise** and **Google Antigravity**.

---

## Overview

A **skill** is a modular instruction package (`SKILL.md` and optional `references/` files) that teaches Gemini Enterprise your organization's domain-specific standards, workflows, and policies.

Instead of maintaining separate repositories for individual skills, teams across the organization use this monorepo to:

* **Collaborate and review**: Author domain skills (such as cloud architecture reviews, security compliance checks, data pipeline runbooks, or editorial guides) through pull requests governed by [`.github/CODEOWNERS`](.github/CODEOWNERS).
* **Validate automatically**: Enforce YAML frontmatter schemas, explicit scope boundaries, link integrity, and the 10-file Gemini Enterprise limit by using [`scripts/validate_skills.py`](scripts/validate_skills.py) and GitHub Actions CI.
* **Publish to the Google Cloud Skill Registry**: Deploy validated skills directly to `projects/<PROJECT_ID>/locations/<LOCATION>/skills/<SKILL_NAME>` as immutable revisions by using [`scripts/publish_to_skill_registry.py`](scripts/publish_to_skill_registry.py) or automated release tags.

---

## Repository structure and reference skill

The repository is organized as follows:

```text
gemini-enterprise-skills/
├── .github/
│   ├── CODEOWNERS                          # Designates required governance reviewers
│   └── workflows/
│       ├── publish-skill-registry.yaml     # Publishes skills to Skill Registry on tag push
│       └── validate-skills.yaml            # Runs schema and dry-run checks on every PR
├── DEPLOYMENT_AND_GOVERNANCE.md            # Enterprise architecture, IAM, and rollback manual
├── README.md                               # Catalog overview and authoring guide
├── scripts/
│   ├── publish_to_skill_registry.py        # Publishes skills to Google Cloud Skill Registry
│   └── validate_skills.py                  # Validates YAML frontmatter, links, and file limits
├── skills/                                 # Production skills catalog
│   └── google-developer-documentation-style/ # Reference skill implementation
└── templates/
    └── skill-template/                     # Starter scaffold for creating new skills
```

### Included reference skill

This repository includes [`skills/google-developer-documentation-style`](skills/google-developer-documentation-style) as a complete reference implementation and test target. Use this skill to:

* **Inspect best-practice structure**: Review how a production [`SKILL.md`](skills/google-developer-documentation-style/SKILL.md) uses `USE FOR:` and `DO NOT USE FOR:` scope boundaries, an agency precedence clause, and progressive disclosure across six files in [`references/`](skills/google-developer-documentation-style/references).
* **Test the validation and publishing pipeline**: Run the local validation and dry-run commands against a known-good skill package before authoring your own.

---

## Quick start for semi-technical users and workspace administrators

When maintainers publish skills from this repository to your agency's **Google Cloud Skill Registry**, those skills become available in your **Gemini Enterprise** workspace without requiring command-line tools or manual file uploads.

### Enable and share a skill in Gemini Enterprise

To verify that a published skill is enabled and shared with the appropriate teams in Gemini Enterprise, complete the following steps:

1. Open your agency's **Gemini Enterprise** web console.
2. In the left navigation menu, click **Skills**. The workspace catalog opens and lists all skills federated from your agency's **Google Cloud Skill Registry**.
3. Select the target skill from the catalog and verify that its status is **Enabled**.
4. If you are a **Gemini Enterprise Administrator** configuring access permissions, open **Sharing and Visibility** and select one of the following options:
   * **Share with Organization**: Grants access to all users across your agency.
   * **Share with Groups**: Restricts access to specific Google Groups or organizational units (such as engineering, security, legal, or technical writing teams).
5. Click **Save**.

### Invoke a skill in conversation

After a skill is enabled in your workspace, you can apply it in any Gemini Enterprise chat session by using one of three methods:

* **Slash command (explicit activation)**: Enter `/` in the chat composer field to open the menu of enabled skills, select `/<skill-name>`, and enter your prompt:
  ```text
  /<skill-name> [Enter your task or paste your content here]
  ```
* **Direct mention**: Enter `@` followed by the skill name in your prompt:
  ```text
  @<skill-name> [Enter your task or paste your content here]
  ```
* **Natural language (automatic activation)**: Enter your request directly. Gemini Enterprise compares the semantic context of your prompt against the `description` field of each enabled skill and activates matching skills automatically. When a skill activates, the chat interface displays a badge with the active skill name on the response card.

---

## How to write and publish a new skill to the Skill Registry

Follow this four-step workflow to author, validate, and publish a new skill for your team or agency.

### Prerequisites

Before you author or publish skills from your workstation, ensure that you have the following tools and permissions:

* Python 3.10 or later
* Git 2.30 or later
* Google Cloud CLI (`gcloud`), authenticated to a project where you hold the `roles/discoveryengine.editor` or `roles/discoveryengine.admin` IAM role

### Step 1: Scaffold the new skill from the template

To create a new skill folder from the starter template, run the following commands from the repository root:

```bash
git clone https://github.com/markattwood12/gemini-enterprise-skills.git
cd gemini-enterprise-skills
cp -r templates/skill-template skills/<YOUR_SKILL_NAME>
```

### Step 2: Author the skill and reference files

To write your skill instructions so that they comply with Gemini Enterprise architecture standards, complete the following steps:

1. Open `skills/<YOUR_SKILL_NAME>/SKILL.md` and update the YAML frontmatter:
   * Set `name` to match your folder name (using lowercase letters, numbers, and hyphens, such as `cloud-architecture-review` or `procurement-compliance`).
   * Set `description` and include explicit `USE FOR:` and `DO NOT USE FOR:` clauses. Gemini Enterprise uses this description for semantic routing; clear negative boundaries prevent the skill from activating on unrelated prompts.
2. Write the core principles, high-frequency rules, and review checklist in `skills/<YOUR_SKILL_NAME>/SKILL.md`. Keep the root file focused so Gemini Enterprise can answer routine requests without loading secondary files.
3. Place detailed domain specifications, edge cases, and examples in `skills/<YOUR_SKILL_NAME>/references/` (progressive disclosure).
4. Verify that your skill directory contains **no more than 10 files** in total (`SKILL.md` plus up to nine files in `references/`), and that every file in `references/` is linked in the routing table inside `SKILL.md`.

> [!TIP]
> Refer to [`skills/google-developer-documentation-style`](skills/google-developer-documentation-style) as a working example of how to structure frontmatter boundaries, routing tables, and modular reference files.

### Step 3: Validate and dry-run test locally

To verify that your skill meets all schema, link-integrity, and file-count requirements before opening a pull request, complete the following steps:

1. Run the validation script:
   ```bash
   python3 scripts/validate_skills.py
   ```
   The script checks every folder in `skills/`, validates the YAML frontmatter, verifies that `USE FOR:` and `DO NOT USE FOR:` are defined, checks all `references/` links, and enforces the 10-file limit.
2. Run an in-memory packaging dry run:
   ```bash
   python3 scripts/publish_to_skill_registry.py \
     --project ci-validation \
     --skill <YOUR_SKILL_NAME> \
     --dry-run
   ```
   The script validates and packs the skill into an in-memory ZIP payload without making network calls.

### Step 4: Publish the skill to the Google Cloud Skill Registry

You can publish validated skills to the Google Cloud Skill Registry through **GitHub Actions CI/CD** (recommended for production) or directly from the **command line**.

#### Option A: Automated publishing through GitHub Actions (recommended)

The [`.github/workflows/publish-skill-registry.yaml`](.github/workflows/publish-skill-registry.yaml) workflow publishes skills to the Google Cloud Skill Registry whenever a maintainer pushes a version tag matching `*@v*`.

To publish through CI/CD, complete the following steps:

1. In your GitHub repository settings (**Settings** > **Secrets and variables** > **Actions** > **Variables**), verify that the following repository variables are configured for Workload Identity Federation:
   * `GCP_PROJECT_ID`: Your target Google Cloud project ID.
   * `GCP_LOCATION`: The registry location (defaults to `global`).
   * `GCP_WORKLOAD_IDENTITY_PROVIDER`: The full resource name of your Workload Identity Provider.
   * `GCP_SERVICE_ACCOUNT`: The service account email with `roles/discoveryengine.editor`.
2. Commit your new skill, open a pull request, and merge it into `main` after `validate-skills.yaml` passes and [`.github/CODEOWNERS`](.github/CODEOWNERS) approves.
3. Tag the release by using the `<SKILL_NAME>@v<MAJOR>.<MINOR>.<PATCH>` convention and push the tag:
   ```bash
   git tag -a <YOUR_SKILL_NAME>@v1.0.0 -m "Initial release of <YOUR_SKILL_NAME>"
   git push origin <YOUR_SKILL_NAME>@v1.0.0
   ```
   GitHub Actions validates the repository, authenticates with Google Cloud, and publishes the skill to the Skill Registry as a new immutable revision.

#### Option B: Direct CLI publishing from a workstation

To publish or update a skill directly from your terminal to the Google Cloud Skill Registry, complete the following steps:

1. Authenticate with Google Cloud:
   ```bash
   gcloud auth login
   ```
2. Run `scripts/publish_to_skill_registry.py` with your target project ID (omit `--skill` to publish all skills in `skills/`):
   ```bash
   python3 scripts/publish_to_skill_registry.py \
     --project <PROJECT_ID> \
     --location global \
     --skill <YOUR_SKILL_NAME>
   ```
   If the skill does not yet exist in the registry, the script sends a `POST` request to create it. If the skill already exists, the script sends a `PATCH` request to update the content and create a new immutable skill revision.

#### Option C: Standalone `.zip` export for air-gapped environments

If your target environment is air-gapped and requires manual console upload instead of direct API publishing, export a compliant `.zip` archive locally:

```bash
python3 scripts/publish_to_skill_registry.py \
  --skill <YOUR_SKILL_NAME> \
  --export-zip dist
```

The script validates the skill and writes `dist/<YOUR_SKILL_NAME>.zip` with `SKILL.md` at the archive root.

---

## Frequently asked questions

### Why do we store all skills in a single repository instead of separate repositories?

Most skills consist of lightweight Markdown files (`SKILL.md` and `references/`). Managing them in a single monorepo provides a unified catalog for discovery, a single CI/CD validation and publishing pipeline, and centralized governance through [`.github/CODEOWNERS`](.github/CODEOWNERS).

### How do we prevent a skill from activating on the wrong prompts?

Every skill in this repository must include explicit `USE FOR:` and `DO NOT USE FOR:` clauses in its YAML `description`. Gemini Enterprise uses these boundaries during semantic routing so domain-specific skills activate only on matching tasks. Users can also invoke a specific skill explicitly at any time by typing `/<skill-name>`.

### Why is each skill limited to 10 files?

Gemini Enterprise enforces a maximum of 10 files per skill package. Combine related topics into focused guides inside `references/` (progressive disclosure), and run `python3 scripts/validate_skills.py` to verify that your skill stays within the limit.

### How do we roll back a skill if an update causes unexpected behavior?

A workspace administrator can disable any skill in under two minutes from the **Gemini Enterprise** console (**Skills** > select skill > toggle **Enabled** to **Disabled**), or you can check out the previous `<SKILL_NAME>@v<X.Y.Z>` Git tag and re-run `scripts/publish_to_skill_registry.py` to publish the prior version as the latest revision.

---

## Governance and operations manual

For complete architecture specifications, IAM role definitions, semantic versioning standards, and incident rollback procedures, see the [Deployment, governance, and operations guide](DEPLOYMENT_AND_GOVERNANCE.md).
