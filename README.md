# Gemini Enterprise skills catalog

This repository provides a centralized, version-controlled catalog of organization-wide skills for **Gemini Enterprise** and **Google Antigravity**, backed by the **Google Cloud Skill Registry**.

---

## What is a Gemini Enterprise skill?

A skill is a modular instruction package that teaches Gemini Enterprise your organization's specific standards, workflows, and editorial rules.

When maintainers publish a skill from this repository to your agency's **Google Cloud Skill Registry**, the skill becomes available across your Gemini Enterprise workspace. Instead of entering repetitive instructions in every prompt, Gemini Enterprise applies the skill's guidelines automatically whenever you work on relevant tasks.

---

## Available skills in this catalog

The following table lists the production skills maintained in this repository:

| Skill name | Description | Target audience | Status | Source directory |
| :--- | :--- | :--- | :--- | :--- |
| `google-developer-documentation-style` | Formats and audits technical guides, API documentation, CLI manuals, and READMEs according to the [Google Developer Documentation Style Guide](https://developers.google.com/style). | Technical writers, software engineers, DevOps engineers, and QA analysts | Production (`v1.0.0`) | [`skills/google-developer-documentation-style`](skills/google-developer-documentation-style) |

---

## Quick start for semi-technical users and content teams

Because skills in this repository are published directly to your agency's **Google Cloud Skill Registry**, you do not need programming experience, command-line tools, or manual file uploads to use them in Gemini Enterprise.

### Enable and verify a skill in Gemini Enterprise

To confirm that a published skill is enabled in your Gemini Enterprise workspace, complete the following steps:

1. Open your agency's **Gemini Enterprise** web console.
2. In the left navigation menu, click **Skills**. The workspace skills catalog opens, listing all skills federated from your agency's **Google Cloud Skill Registry**.
3. Locate `google-developer-documentation-style` in the catalog and verify that its status is **Enabled**.
4. If you are a **Gemini Enterprise Administrator** configuring access for your agency, click the skill name, open **Sharing and Visibility**, and select one of the following options:
   * **Share with Organization**: Grants access to all users in your agency.
   * **Share with Groups**: Restricts access to specific Google Groups (such as technical writing or engineering teams).
5. Open a new chat session in **Gemini Enterprise** and enter `/` in the chat composer field. A menu of active skills opens, confirming that `/google-developer-documentation-style` is ready for use.

---

## How to use a skill in your daily work

After a skill is enabled in your Gemini Enterprise workspace, you can invoke it in any conversation by using one of the following three methods:

### Use a slash command

To explicitly activate the skill for a prompt, enter `/` in the chat field, select `/google-developer-documentation-style`, and enter your instructions:

```text
/google-developer-documentation-style Review the following installation steps for our data pipeline:
[Paste your draft here]
```

### Use a direct mention

To reference the skill inline, enter `@` followed by the skill name:

```text
@google-developer-documentation-style Edit this API error troubleshooting guide to follow standard Google style.
[Paste your draft here]
```

### Use natural language

Because Gemini Enterprise evaluates the semantic context of your prompt against the skill descriptions in the registry, you can also enter your request directly without a command prefix:

```text
Review this draft README against developer documentation standards. Focus on active voice, sentence-case headings, and imperative procedural steps.
[Paste your draft here]
```

---

## Example prompts to copy and paste

You can copy and adapt the following prompt templates for common documentation tasks:

* **Polish a rough technical draft**:
  > *"Use `/google-developer-documentation-style` to rewrite these release notes into developer documentation. Put conditions before instructions, and format all headings in sentence case."*
* **Audit a step-by-step procedure**:
  > *"Audit these installation instructions. Verify that every numbered step starts with an imperative verb, that user actions are separated from system results, and that UI elements appear in bold text while commands appear in code font."*
* **Convert passive voice to active voice**:
  > *"Review this architecture overview and convert passive-voice sentences into active voice. Remove minimizing words such as 'simply', 'just', and 'obviously'."*
* **Format API parameter tables**:
  > *"Review this table of API parameters. Format parameter names in code font, state whether each parameter is required or optional, specify default values, and format descriptions according to the reference documentation guidelines."*

---

## Before and after examples

The following table illustrates how the documentation style skill edits common technical writing issues:

| Unedited draft | Revised version | Rationale |
| :--- | :--- | :--- |
| *Clicking on the **Submit** button will send your request to the server.* | *Click **Submit**. The server processes the request.* | Uses present tense and imperative mood, and separates the user action from the system result. |
| *It's easy! Simply enter `gcloud auth login` to log in.* | *To log in to your account, run `gcloud auth login`.* | Removes condescending language (*easy*, *simply*), eliminates the exclamation mark, and front-loads the goal. |
| *Open the IAM menu if you want to create a key.* | *To create a key, open the **IAM** page.* | Places the condition before the instruction so the reader immediately knows if the step applies to them. |
| *Click `Deploy` on the top bar.* | *Click **Deploy**.* | Formats visible UI buttons in **bold** instead of monospace code font. |
| *Verify by checking the whitelist and running a sanity check.* | *Verify by checking the **allowlist** and running a **coherence check**.* | Replaces non-inclusive idioms with precise, standard technical terminology. |

---

## Frequently asked questions

### Does this skill alter programming code or technical logic?

No. The skill only audits and revises prose, formatting, tone, organization, and terminology. It does not change your programming code, architectural designs, or security configurations.

### What happens if an agency rule conflicts with the Google style guide?

The skill includes an embedded **Precedence Clause**. If your agency follows a specific statutory standard, the GPO Style Manual, or an internal naming convention, state that requirement in your prompt:

> *"Follow our internal agency standard for agency acronyms, and apply Google style for all other formatting and tone."*

Your project-specific instruction overrides the default rule in the skill.

### Should I use this skill on executive memos, policy letters, or emails?

No. This skill is scoped strictly for software and developer documentation (such as READMEs, API references, and CLI guides). Applying it to general business correspondence removes conversational phrases (such as "please") and enforces technical formatting that is inappropriate for memos or emails.

### How can I confirm that the skill activated during a chat?

When Gemini Enterprise applies a skill to your prompt, the chat interface displays a badge indicating the active skill name on the response card.

---

## How to write and publish a new skill to the Skill Registry

This section describes the end-to-end process for authoring, validating, versioning, and publishing a new skill to the **Google Cloud Skill Registry** (`projects/<PROJECT_ID>/locations/<LOCATION>/skills/<SKILL_NAME>`).

### Prerequisites

To author and publish skills from your workstation, ensure that you have the following tools and permissions:

* Python 3.10 or later
* Git 2.30 or later
* Google Cloud CLI (`gcloud`), authenticated to a project where you hold the `roles/discoveryengine.editor` or `roles/discoveryengine.admin` IAM role

### Step 1: Scaffold the new skill from the template

To create the directory structure for a new skill, run the following commands from the repository root:

```bash
git clone https://github.com/markattwood12/gemini-enterprise-skills.git
cd gemini-enterprise-skills
cp -r templates/skill-template skills/<YOUR_SKILL_NAME>
```

### Step 2: Author the skill and reference files

To write your skill instructions so that they comply with Gemini Enterprise architecture standards, complete the following steps:

1. Open `skills/<YOUR_SKILL_NAME>/SKILL.md` and configure the YAML frontmatter:
   * Set `name` to match your folder name (using lowercase letters, numbers, and hyphens, such as `cloud-security-review`).
   * Set `description` and include explicit `USE FOR:` and `DO NOT USE FOR:` clauses so Gemini Enterprise does not trigger the skill on unrelated topics.
2. Write the core rules and review checklist in `skills/<YOUR_SKILL_NAME>/SKILL.md`. Keep the root `SKILL.md` concise so Gemini Enterprise can answer routine requests with low latency.
3. Place detailed specifications, edge cases, and examples in `skills/<YOUR_SKILL_NAME>/references/` (progressive disclosure).
4. Ensure that the skill directory contains **no more than 10 files** in total (`SKILL.md` plus up to nine files in `references/`), and that every file in `references/` is linked from the routing table in `SKILL.md`.

### Step 3: Validate and dry-run test locally

To verify that your new skill meets all schema, link-integrity, and file-count requirements before committing, run the validation and dry-run commands:

1. Run the schema and link validator:
   ```bash
   python3 scripts/validate_skills.py
   ```
   The script verifies the YAML frontmatter, confirms that `USE FOR:` and `DO NOT USE FOR:` are present, checks all internal links, and verifies the 10-file limit.
2. Run an in-memory packaging dry run:
   ```bash
   python3 scripts/publish_to_skill_registry.py \
     --project ci-validation \
     --skill <YOUR_SKILL_NAME> \
     --dry-run
   ```
   The script packs the skill into an in-memory ZIP payload and confirms the bundle size without making network calls.

### Step 4: Publish the skill to the Google Cloud Skill Registry

You can publish your validated skill to the Google Cloud Skill Registry either automatically through **GitHub Actions CI/CD** (recommended for production) or directly from the **command line**.

#### Option A: Automated publishing through GitHub Actions (recommended)

The repository includes [`.github/workflows/publish-skill-registry.yaml`](.github/workflows/publish-skill-registry.yaml), which publishes skills to the Google Cloud Skill Registry whenever a maintainer pushes a version tag matching `*@v*`.

To publish through CI/CD, complete the following steps:

1. In your GitHub repository settings (**Settings** > **Secrets and variables** > **Actions** > **Variables**), ensure that the following repository variables are configured for Workload Identity Federation:
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
2. Run `scripts/publish_to_skill_registry.py` with your target project ID:
   ```bash
   python3 scripts/publish_to_skill_registry.py \
     --project <PROJECT_ID> \
     --location global \
     --skill <YOUR_SKILL_NAME>
   ```
   If the skill does not yet exist in the registry, the script sends a `POST` request to create it. If the skill already exists, the script automatically sends a `PATCH` request to update the content and create a new immutable skill revision.

#### Option C: Standalone `.zip` export for air-gapped environments

If your target environment is air-gapped and requires manual console upload instead of direct API publishing, export a compliant `.zip` archive locally:

```bash
python3 scripts/publish_to_skill_registry.py \
  --skill <YOUR_SKILL_NAME> \
  --export-zip dist
```

The script validates the skill and writes `dist/<YOUR_SKILL_NAME>.zip` with `SKILL.md` at the archive root.

---

## Governance and operations manual

All additions and modifications to this catalog are governed by [`.github/CODEOWNERS`](.github/CODEOWNERS). For detailed architecture specifications, IAM roles, semantic versioning rules, and incident rollback procedures, see the [Deployment, governance, and operations guide](DEPLOYMENT_AND_GOVERNANCE.md).
