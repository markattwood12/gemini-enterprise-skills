# Formatting and organization (Google style guide)

Reference: [Google Developer Documentation Style Guide - Headings, lists, and tables](https://developers.google.com/style/headings)

## 1. Document titles and headings

### Use sentence case

Use **sentence case** for all document titles, section headings, and table column headers:

* Capitalize only the first word and proper nouns.
* Do not use title case or all-uppercase letters for headings.

| Avoid (title case) | Recommended (sentence case) |
| :--- | :--- |
| Configuring Your Google Cloud Service Account | Configuring your Google Cloud service account |
| Best Practices For API Design | Best practices for API design |

### Punctuation in headings

Observe the following punctuation rules in headings:

* Never end a heading with a period, colon, or exclamation mark.
* Use a question mark only if the heading is an explicit question (such as in an FAQ).

### Phrasing headings

Phrase headings according to the content type:

* Use a **gerund** (an *-ing* verb) or an imperative verb for task-based sections (for example, *Deploying an agent engine* or *Troubleshoot connection errors*).
* Use a direct noun phrase for reference topics (for example, *API reference* or *Parameter reference*).
* Qualify generic terms such as "Overview" or "Introduction" (for example, *Architectural overview*).

---

## 2. Lists

### General list rules

Follow these structural rules for all lists:

* Never create a list with only one item. Incorporate a single item into the surrounding paragraph.
* Introduce every list with a **lead-in sentence ending with a colon (`:`)**.
* Maintain **parallel grammatical structure** across all items in a list.

### Numbered lists

Use numbered lists only when sequence, rank, or step-by-step chronology matters:

```markdown
To create a service account, complete the following steps:

1. In the Google Cloud console, open the **IAM & Admin** page.
2. Click **Create Service Account**.
3. Enter a descriptive service account name.
4. Click **Create and Continue**.
```

### Bulleted lists

Use bulleted lists for unordered collections, alternative choices, or non-sequential items:

```markdown
The deployment supports the following runtime targets:

* Vertex AI Reasoning Engine
* Standalone Cloud Run container
* Local development server
```

### Punctuation of list items

Punctuate list items consistently:

* If list items are **complete sentences**, end each item with a period.
* If list items are **short fragments or noun phrases**, omit terminal punctuation.

### Description lists

Use bold term prefixes followed by a colon for glossary terms or configuration parameters:

```markdown
* **`project_id`**: The unique identifier of your Google Cloud project.
* **`region`**: The Google Cloud compute region where resources are provisioned.
* **`model`**: The foundational model identifier (for example, `gemini-3.8-flash`).
```

---

## 3. Punctuation and conventions

### Serial (Oxford) comma

Always include a serial comma before the coordinating conjunction in a series of three or more items:

* **Recommended**: *Python, Go, and TypeScript.*
* **Avoid**: *Python, Go and TypeScript.*

### Numbers and units

Format numbers and measurements consistently:

* Spell out numbers from **zero through nine** in prose (*five instances*, *three parameters*).
* Use numerals for numbers **10 and above** (*15 minutes*, *100 requests*).
* Always use numerals with units of measurement or technical values (*5 MB*, *3 seconds*, *8 kHz*).
* Include a space between the number and unit (*10 GB*, not *10GB*), except for percentages (*10%*) and currencies (*\$50*).

---

## 4. Notices and callouts

Notices draw attention to critical information outside the normal flow of text. Use notices sparingly, and never stack two notices consecutively.

### Types of notices

Select the callout type that matches the severity of the information:

* **Note** (`> [!NOTE]`): Supplementary background, tips, or edge-case explanations.
* **Caution** (`> [!CAUTION]`): Guidance to proceed carefully to prevent unexpected behavior or minor errors.
* **Warning** (`> [!WARNING]`): Critical alerts where ignoring the notice can lead to permanent data loss, security vulnerabilities, or unexpected billing charges.

---

## 5. Cross-references and link text

### Write descriptive link text

Always write specific, descriptive link text that communicates the destination topic:

* Never use generic anchor text such as **click here**, **here**, **link**, **learn more**, or **this document**.
* Never display a raw URL as link text in prose.
* Ensure link text is meaningful when read out of context.

| Avoid | Recommended |
| :--- | :--- |
| For details on IAM permissions, click [here](https://cloud.google.com/iam/docs). | For details, see the [IAM permissions documentation](https://cloud.google.com/iam/docs). |
| You can find the source code at https://github.com/example/repo. | You can review the code in the [GitHub sample repository](https://github.com/example/repo). |
| [Learn more](https://cloud.google.com/run). | See the [Cloud Run documentation](https://cloud.google.com/run) for deployment guides. |
