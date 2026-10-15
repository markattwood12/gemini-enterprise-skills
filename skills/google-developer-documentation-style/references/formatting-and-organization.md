# Formatting and Organization (Google Style Guide)

Reference: [Google Developer Documentation Style Guide - Headings, Lists, and Tables](https://developers.google.com/style/headings)

## 1. Document Titles and Headings

### Capitalization: Sentence Case
Use **sentence case** for all document titles, section headings, and table column headers:
* Capitalize only the first word and proper nouns.
* Never use Title Case or ALL CAPS for headings.

| Avoid (Title Case) | Recommended (Sentence Case) |
| :--- | :--- |
| Configuring Your Google Cloud Service Account | Configuring your Google Cloud service account |
| Best Practices For API Design | Best practices for API design |

### Punctuation in Headings
* **Never end a heading with a period**, colon, or exclamation mark.
* A question mark is permitted only if the heading is an explicit question (such as in an FAQ).

### Phrasing Headings
* Use a **gerund** (an -ing verb) for task-based or conceptual sections:  
  * *Deploying an agent engine*
  * *Troubleshooting connection errors*
* Use an **imperative verb** or direct noun phrase for reference topics:  
  * *API reference*
  * *Parameter reference*
* Avoid ambiguous terms like "Overview", "Introduction", or "General" on their own; qualify them (e.g., *Architectural overview*).

---

## 2. Lists

### General Rules
* **Never create a list with only one item.** A single item should be incorporated into the surrounding paragraph.
* Always introduce a list with a **lead-in sentence ending with a colon (`:`)**.
* Maintain **parallel grammatical structure** across all items in a list (all starting with an imperative verb, or all noun phrases, or all full sentences).

### Numbered Lists
Use numbered lists **only** when sequence, rank, or step-by-step chronology matters.
```markdown
To create a service account, complete the following steps:

1. In the Google Cloud console, open the **IAM & Admin** page.
2. Click **Create Service Account**.
3. Enter a descriptive service account name.
4. Click **Create and Continue**.
```

### Bulleted Lists
Use bulleted lists for unordered collections, alternative choices, or non-sequential items.
```markdown
The deployment supports the following runtime targets:

* Vertex AI Reasoning Engine
* Standalone Cloud Run container
* Local development server
```

### Punctuation of List Items
* If list items are **full sentences**, end each item with a period.
* If list items are **short fragments or noun phrases**, omit end punctuation.
* If list items complete the grammatical thought of an introductory sentence, punctuate consistently (typically no period unless the item is a complete sentence).

### Description Lists
Use bolded term prefixes for glossary terms or configuration parameters:
```markdown
* **`project_id`**: The unique identifier of your Google Cloud project.
* **`region`**: The GCP compute region where resources are provisioned.
* **`model`**: The foundational LLM identifier (for example, `gemini-3.8-flash`).
```

---

## 3. Punctuation & Conventions

### Serial (Oxford) Comma
Always use the serial comma before the coordinating conjunction in a series of three or more items.
* **Correct**: *Python, Go, and TypeScript.*
* **Incorrect**: *Python, Go and TypeScript.*

### Numbers and Units
* Spell out numbers from **zero through nine** in prose (*five instances*, *three parameters*).
* Use numerals for numbers **10 and above** (*15 minutes*, *100 requests*).
* Always use numerals with units of measurement or technical values (*5 MB*, *3 seconds*, *8 kHz*).
* Include a space between the number and unit (*10 GB*, not *10GB*), except for percentages (*10%*) and currencies (*$50*).

---

## 4. Notices and Callouts

Notices draw attention to critical information outside the normal flow of text. Use notices **sparingly**; if everything is highlighted, nothing stands out. Never stack two notices consecutively.

### Types of Notices
* **Note** (`> [!NOTE]`): Useful context, supplementary background, tips, or edge-case explanations that aren't critical to task completion.
* **Caution** (`> [!CAUTION]`): Informs the reader to proceed carefully to prevent unexpected behavior, confusion, or minor errors.
* **Warning** (`> [!WARNING]`): Critical alerts where ignoring the notice can lead to permanent data loss, security vulnerabilities, irreversible modifications, or unexpected cloud billing charges.

---

## 5. Cross-References and Link Text

### Descriptive Link Text
Always write specific, descriptive link text that clearly communicates the destination page or topic.
* Never use generic links like **click here**, **here**, **link**, **learn more**, or **this document**.
* Never display a raw URL as link text unless explicitly demonstrating an address change.
* Ensure link text is readable and informative when read completely out of context.

| Avoid | Recommended |
| :--- | :--- |
| For details on IAM permissions, click [here](https://cloud.google.com/iam/docs). | For details, see the [IAM permissions documentation](https://cloud.google.com/iam/docs). |
| You can find the source code at https://github.com/example/repo. | You can review the complete code in the [GitHub sample repository](https://github.com/example/repo). |
| [Learn more](https://cloud.google.com/run). | See the [Cloud Run documentation](https://cloud.google.com/run) for deployment guides. |
