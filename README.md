# Gemini Enterprise skills catalog

This repository provides a centralized, version-controlled catalog of organization-wide skills for **Gemini Enterprise** and **Google Antigravity**.

---

## What is a Gemini Enterprise skill?

A skill is a modular instruction package that teaches Gemini Enterprise your organization's specific standards, workflows, and editorial rules.

Instead of entering repetitive instructions in every prompt, you can install a skill once. Gemini Enterprise then applies those guidelines automatically whenever you work on relevant tasks.

---

## Available skills in this catalog

The following table lists the production skills maintained in this repository:

| Skill name | Description | Target audience | Status | Source directory |
| :--- | :--- | :--- | :--- | :--- |
| `google-developer-documentation-style` | Formats and audits technical guides, API documentation, CLI manuals, and READMEs according to the [Google Developer Documentation Style Guide](https://developers.google.com/style). | Technical writers, software engineers, DevOps engineers, and QA analysts | Production (`v1.0.0`) | [`skills/google-developer-documentation-style`](skills/google-developer-documentation-style) |

---

## Quick start for semi-technical users and content teams

You do not need programming or command-line experience to install or use these skills in the Gemini Enterprise web console.

### Prerequisites

Before you install a skill across your organization, ensure that you have one of the following access levels:

* **Gemini Enterprise Administrator** permissions to publish skills across organizational units.
* Standard workspace permissions to upload skills for personal or team use.

### Install the skill in Gemini Enterprise

To download and install a skill package through the web interface, complete the following steps:

1. Open the [GitHub Releases page](https://github.com/markattwood12/gemini-enterprise-skills/releases) for this repository.
2. Under the latest release, click `google-developer-documentation-style.zip`. Your browser downloads the archive to your computer. Do not extract or unzip the downloaded file.
3. Open your agency's **Gemini Enterprise** web console.
4. In the left navigation menu, click **Skills**.
5. Click **Create Skill** (or **Add Skill**). The skill creation dialog opens.
6. Select **Upload Skill**, and then select the `google-developer-documentation-style.zip` file from your computer.
7. In the **Sharing and Visibility** section, select one of the following access options:
   * **Share with Organization**: Grants access to all users in your agency.
   * **Share with Groups**: Restricts access to specific Google Groups (such as technical writing or engineering teams).
8. Click **Save**.

### Verify the installation

To confirm that the skill is active in your workspace, complete the following steps:

1. Open a new chat session in **Gemini Enterprise**.
2. In the chat composer field, enter `/`. A menu of installed skills opens.
3. Verify that `/google-developer-documentation-style` appears in the list.

---

## How to use the skill in your daily work

After the skill is installed in your Gemini Enterprise workspace, you can invoke it in any conversation by using one of the following three methods:

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

Because Gemini Enterprise evaluates the semantic context of your prompt, you can also enter your request directly without a command prefix:

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

The following table illustrates how the skill edits common technical writing issues:

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

## Developer and administrator guide

This section provides instructions for engineers and administrators who manage the repository, run automated validation scripts, or publish skills to the **Google Cloud Skill Registry**.

### Prerequisites

To run the validation and publishing tools locally, install the following software:

* Python 3.10 or later
* Git 2.30 or later
* Google Cloud CLI (`gcloud`), if you publish directly to the Google Cloud Skill Registry

### Set up your local environment

To clone the repository and navigate to the project root, run the following commands:

```bash
git clone https://github.com/markattwood12/gemini-enterprise-skills.git
cd gemini-enterprise-skills
```

### Validate skill packages

To verify that all skills conform to YAML frontmatter rules, link integrity, and the **10-file Gemini Enterprise limit**, run the validation script:

```bash
python3 scripts/validate_skills.py
```

### Publish directly to the Google Cloud Skill Registry

To publish a skill directly to your Google Cloud project's **Skill Registry** (`projects/<PROJECT_ID>/locations/<LOCATION>/skills/<SKILL_NAME>`) without handling local `.zip` files, complete the following steps:

1. Authenticate with Google Cloud:
   ```bash
   gcloud auth login
   ```
2. Run the publishing script:
   ```bash
   python3 scripts/publish_to_skill_registry.py \
     --project <PROJECT_ID> \
     --location global \
     --skill google-developer-documentation-style
   ```
   The script validates the skill, packages it in memory, uploads the payload to the Discovery Engine API, and creates a new immutable skill revision.

### Create a new skill

To author and validate a new skill in this repository, complete the following steps:

1. Copy the starter template directory to a new folder under `skills/`:
   ```bash
   cp -r templates/skill-template skills/<YOUR_SKILL_NAME>
   ```
2. Open `skills/<YOUR_SKILL_NAME>/SKILL.md` and update the YAML frontmatter:
   * Set `name` to match your directory name (lowercase letters, numbers, and hyphens).
   * Set `description` and include explicit `USE FOR:` and `DO NOT USE FOR:` scope boundaries.
3. Write the core rules in `SKILL.md` and place supporting guides in `skills/<YOUR_SKILL_NAME>/references/`.
4. Run the validation script to confirm compliance:
   ```bash
   python3 scripts/validate_skills.py
   ```
5. Commit your changes and open a pull request.

---

## Governance and review

All additions and modifications to this catalog are governed by [`.github/CODEOWNERS`](.github/CODEOWNERS) and require peer review from designated administrators before merging into the `main` branch.

---

## Enterprise operations and deployment manual

For detailed architecture specifications, IAM requirements, semantic versioning conventions, and CI/CD pipelines, see the [Deployment, governance, and operations guide](DEPLOYMENT_AND_GOVERNANCE.md):

* **System and IAM requirements**: Required Google Cloud Discovery Engine roles, Workspace Admin permissions, and GitHub branch protection rules.
* **Skill architecture standards**: The 10-file limit, progressive disclosure patterns, and negative scope boundaries.
* **Semantic versioning strategy**: Rules for `MAJOR.MINOR.PATCH` increments and monorepo Git tags (`<skill-name>@v<X.Y.Z>`).
* **Deployment methodologies**: Automated zero-click CI/CD pipelines using Workload Identity Federation (WIF) and staged pilot-group rollouts.
* **Rollback and incident management**: Emergency disablement and prior-revision restoration procedures.
