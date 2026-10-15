# Gemini Enterprise Skills Catalog

A centralized, version-controlled repository of organization-wide skills for **Gemini Enterprise** and **Google Antigravity**.

---

## 📖 What Is a Gemini Enterprise Skill? (Plain English Overview)

Think of a **Skill** as a specialized playbook or digital assistant add-on. When installed in Gemini Enterprise, it teaches the AI your organization's exact standards, workflows, and editorial rules.

Instead of typing long, repetitive instructions like *"Please write in active voice, use sentence case, bold the UI buttons, and avoid words like 'simply'"* every single time you chat, a Skill gives Gemini those instructions automatically whenever you work on relevant tasks.

---

## 📚 Available Skills in This Catalog

| Skill Name | What It Does | Who Should Use It | Status | Ready-to-Use Package |
| :--- | :--- | :--- | :--- | :--- |
| **`google-developer-documentation-style`** | Automatically formats and audits technical guides, API docs, CLI references, and READMEs to match the official [Google Developer Documentation Style Guide](https://developers.google.com/style). | Technical writers, developers, DevOps engineers, and QA analysts. | **v1.0.0 (Production)** | [Download ZIP (v1.0.0)](https://github.com/markattwood12/gemini-enterprise-skills/releases/download/google-developer-documentation-style%40v1.0.0/google-developer-documentation-style.zip) |

---

## ⚡ Quick Start for Semi-Technical Users & Content Teams

**No programming or terminal knowledge is required to install or use these skills.**

### Step 1: Download the Skill Package
1. Go to the [GitHub Releases Page](https://github.com/markattwood12/gemini-enterprise-skills/releases).
2. Click on the latest release of `google-developer-documentation-style.zip` to download it to your computer.
3. **Do not unzip the file.** Gemini Enterprise requires the `.zip` archive as-is.

### Step 2: Upload to Gemini Enterprise
*(Note: Depending on your agency's permissions, this step is performed either by you or by your designated Gemini Workspace Administrator).*

1. Open your browser and navigate to your agency's **Gemini Enterprise** portal.
2. In the left navigation menu, click **Skills**.
3. In the top right corner, click **+ Create Skill** (or **Add Skill**).
4. Select the **Upload Skill** option.
5. Choose the downloaded `google-developer-documentation-style.zip` file from your computer.
6. Under **Sharing & Visibility**, choose:
   * **Share with Organization**: Makes the skill available to all team members across your agency.
   * **Share with Groups**: Restricts the skill to specific teams (for example, the Technical Writing or Cloud Engineering teams).
7. Click **Save** (or **Publish**).

---

## 💬 How to Use the Skill in Your Daily Work

Once the skill is active in your Gemini Enterprise workspace, you can use it in any conversation using three simple methods:

### Method 1: The Slash Command (Most Reliable)
In the chat prompt box, type a forward slash (`/`). A popup list of your agency's installed skills will appear. Click `/google-developer-documentation-style` and then type your request:
```text
/google-developer-documentation-style Please review the following installation steps for our new data pipeline:
[paste your draft here]
```

### Method 2: The Direct Mention
Type `@` followed by the skill name:
```text
@google-developer-documentation-style Edit this API error troubleshooting guide to ensure it follows standard Google style.
[paste your draft here]
```

### Method 3: Natural Language
Gemini Enterprise recognizes the context of developer documentation automatically. You can simply ask:
```text
Review this draft README against developer documentation standards. Focus on active voice, sentence case headings, and clear procedural steps.
[paste your draft here]
```

---

## 📝 Example Prompts You Can Copy and Paste

Here are real-world prompt templates you can copy, paste, and adapt immediately:

### Example 1: Polishing a Rough Technical Draft
> *"I have drafted notes for our software release. Use `/google-developer-documentation-style` to rewrite this into polished developer documentation. Ensure conditions come before instructions and all headings use sentence case."*

### Example 2: Auditing a Step-by-Step Procedure
> *"Audit these step-by-step instructions. Check that every step begins with an imperative verb (like Click, Run, Select), that actions are separated from system results, and that visible UI buttons are bolded while commands are in code font."*

### Example 3: Converting Passive Voice to Active Voice
> *"Review this architecture overview and convert all passive voice sentences into active voice where the actor is clear. Eliminate minimizing words like 'simply', 'just', and 'obviously'."*

### Example 4: Reviewing API and Parameter Tables
> *"Review this table of API parameters. Ensure all parameter names are in backticks, types are clearly identified, optional fields include default values, and parameter descriptions follow standard style conventions."*

---

## 🔍 Before & After Examples: What the Skill Does

To help you understand how the skill improves documentation, here is a side-by-side comparison of common edits:

| Rough / Unedited Draft | How the Skill Rewrites It | Why It Was Changed |
| :--- | :--- | :--- |
| *Clicking on the **Submit** button will send your request to the server.* | *Click **Submit**. The server processes the request.* | **Present tense & imperative mood:** Steps must be direct commands, and system reactions belong in a separate sentence. |
| *It's easy! Simply enter `gcloud auth login` to log in.* | *To log in to your account, run `gcloud auth login`.* | **Removes condescending words:** Words like *simply* and *easy* are removed; front-loads the condition/goal. |
| *Open the IAM menu if you want to create a key.* | *To create a key, open the **IAM** page.* | **Front-loads condition:** Puts the user's goal *before* the action so they know if the step applies to them. |
| *Click `Deploy` on the top bar.* | *Click **Deploy**.* | **UI vs. Code distinction:** Visible buttons and menus must be in **bold**, not code font. |
| *Verify by checking whitelist and running sanity check.* | *Verify by checking the **allowlist** and running a **coherence check**.* | **Inclusive terminology:** Replaces outdated idioms with modern, precise technical language. |

---

## ❓ Frequently Asked Questions (FAQ)

### Will this skill change my actual code or technical logic?
**No.** The skill only audits and rewrites prose, formatting, tone, organization, and terminology. It does not alter your underlying programming code, architectural diagrams, or business requirements.

### What if my agency has a rule that conflicts with Google's style guide?
The skill includes an embedded **Precedence Clause**. If your agency has a specific statutory guideline, GPO standard, or internal style convention (such as specific capitalizations or acronyms), you can simply tell Gemini in your prompt:
> *"Follow our internal agency standard for agency acronyms, but apply Google style for all other formatting and tone."*
Your project-specific instruction will always override the default skill rule.

### Can I use this skill on executive memos, policy letters, or emails?
**No, and you shouldn't.** This skill is strictly scoped for software and developer documentation (READMEs, API references, CLI guides). If applied to executive memos or formal correspondence, it will inappropriately remove polite phrases (like "please") and enforce technical monospace formatting. Use standard Gemini Enterprise for general business writing.

### How do I know the skill actually activated?
When a skill activates in Gemini Enterprise, you will see a badge or indicator showing the skill name at the top or bottom of the response, confirming that its guidelines were applied.

---

## 🛠️ For Developers & Platform Administrators

*(This section is for engineers who want to clone the repo, run automated validation, or author new skills).*

### Prerequisites
* Python 3.10+
* Git 2.30+

### Local Setup
```bash
git clone https://github.com/markattwood12/gemini-enterprise-skills.git
cd gemini-enterprise-skills
```

### Validating Skill Packages
To ensure skill files conform to YAML frontmatter rules and stay within the **10-file Gemini Enterprise limit**:
```bash
python3 scripts/validate_skills.py
```

### Packaging Skills into Upload-Ready ZIPs
To compile one or all skills into `dist/<skill-name>.zip` with `SKILL.md` at the root of the archive:
```bash
# Package all skills
python3 scripts/package_skills.py

# Package a specific skill
python3 scripts/package_skills.py --skill google-developer-documentation-style
```

### Creating a New Skill
1. Copy the starter template:
   ```bash
   cp -r templates/skill-template skills/<YOUR_SKILL_NAME>
   ```
2. Edit `skills/<YOUR_SKILL_NAME>/SKILL.md` (ensure `USE FOR:` and `DO NOT USE FOR:` are defined).
3. Add supporting markdown guides into `references/`.
4. Validate and package:
   ```bash
   python3 scripts/validate_skills.py
   python3 scripts/package_skills.py --skill <YOUR_SKILL_NAME>
   ```
5. Update `catalog.json` and submit a Pull Request.

---

## 🏛️ Governance and Review

All skill additions or updates to this catalog are governed by `.github/CODEOWNERS` and require review and approval from designated enterprise administrators before being merged or tagged for release.

---

## 📘 Enterprise Operations and Deployment Manual

For complete architecture, access requirements, versioning conventions, and deployment pipelines, see the dedicated [Deployment, Governance, and Operations Guide](DEPLOYMENT_AND_GOVERNANCE.md):

* **System & IAM Requirements**: Roles for Google Cloud Discovery Engine, Workspace Admin, and GitHub.
* **Architecture Best Practices**: 10-file ceiling rules, progressive disclosure, and boundary scoping.
* **Semantic Versioning Strategy**: Rules for `MAJOR.MINOR.PATCH` and monorepo Git tagging (`skill-name@vX.Y.Z`).
* **Deployment Methodologies**: Step-by-step procedures for Admin UI rollouts (Canary / Pilot Groups) and automated CI/CD pipelines via Google Cloud APIs / WIF.
* **Rollback & Incident Management**: Sub-2-minute emergency killswitch and prior-version restoration procedures.

