---
name: google-developer-documentation-style
description: >-
  Applies the official Google Developer Documentation Style Guide (https://developers.google.com/style)
  to write, edit, review, or format developer documentation, API references, CLI manuals, architecture specs,
  READMEs, code comments, and technical tutorials.

  USE FOR: Software developer documentation, API specifications, SDK guides, engineering tutorials,
  architecture decision records (ADRs), and CLI reference manuals.
  DO NOT USE FOR: General business correspondence, policy memos, executive summaries, press releases,
  legal contracts, marketing copy, or casual non-technical communications.
metadata:
  author: Google Developer Documentation Style Guide
  version: 1.0.0
  standard: Google Developer Style Guide (developers.google.com/style)
---

# Google Developer Documentation Style Guide

This skill guides the creation, review, and editing of technical documentation in accordance with the official [Google Developer Documentation Style Guide](https://developers.google.com/style).

---

> [!IMPORTANT]
> **Precedence Clause for Agency Guidelines:**
> If an agency-specific standard, statutory requirement, or project-specific style manual (such as GPO Style Manual or PlainLanguage.gov) conflicts with a rule in this guide, the agency-specific requirement takes precedence.

---

## ⚡ The 10 Golden Rules

1. **Second Person ("You")**: Address the developer directly as *you*. Never use *we*, *I*, or *the user*.
2. **Active Voice**: Make the actor clear (*"The server processes the request"*, not *"The request is processed by the server"*).
3. **Present Tense**: Describe what the software does now, not what it will do (*"Clicking Submit sends..."*, not *"will send"*).
4. **Sentence Case Headings**: Capitalize only the first word and proper nouns in headings and table columns. **Never end a heading with a period**.
5. **Code vs. UI Distinction**:
   * Use code font (`` `monospace` ``) for code, files, CLI commands, flags, parameters, and HTTP methods.
   * Use **bold font** (`**Element**`) for UI buttons, menus, dialog titles, and fields. Never use code font for UI elements.
6. **Task-Oriented Procedures**:
   * Numbered lists for sequential steps; bulleted lists for non-sequential options (minimum two items per list).
   * Start every action step with an **imperative verb** (*Click*, *Run*, *Select*, *Specify*).
   * Separate the action from the result (*"Click Save. The details page opens."*).
7. **Front-Load Conditions**: Put conditions *before* instructions (*"If you use Python 3.14, install uv"* instead of *"Install uv if you use Python 3.14"*).
8. **Descriptive Link Text**: Never write *"click here"*, *"here"*, or use raw URLs. Link text must be meaningful out of context.
9. **Serial (Oxford) Comma**: Always use the comma before the final conjunction in a series of three or more items (*"A, B, and C"*).
10. **Inclusive & Objective Language**:
    * Avoid non-inclusive idioms (*allowlist* not *whitelist*, *primary/replica* not *master/slave*, *coherence check* not *sanity check*).
    * Never use minimizing or condescending words (*simply*, *just*, *easy*, *obviously*).
    * Never use *please* in technical instructions.

---

## 🧭 Topic Routing Table

When auditing or drafting specific types of content, consult the corresponding reference document in `references/`:

| Documentation Task | Reference Document |
| :--- | :--- |
| **Voice, tone, contractions, minimizing words, future-proofing** | [Voice and Tone](references/voice-and-tone.md) |
| **Code in text, code blocks, CLI commands, placeholders, UI elements** | [Code and UI Formatting](references/code-and-ui.md) |
| **Headings, lists, tables, callouts (Note/Caution/Warning), link text** | [Formatting and Organization](references/formatting-and-organization.md) |
| **Step-by-step procedures, prerequisites, sub-steps, verification** | [Procedures and Instructions](references/procedures-and-instructions.md) |
| **Comprehensive A–Z word list, noun vs. verb forms, inclusive language** | [Word List & Inclusive Language](references/word-list-and-inclusive.md) |
| **API specifications, method signatures, parameters, exceptions, types** | [API and Reference Documentation](references/api-and-reference-docs.md) |

---

## 📋 Five-Pass Editorial Review Checklist

When reviewing or drafting documentation, execute the following audit passes:

### Pass 1: Voice and Tone
* [ ] Is the document addressed to "you"? (Eliminate "we", "us", "our", "the developer").
* [ ] Are sentences predominantly in the active voice?
* [ ] Is the text written in present tense?
* [ ] Are condescending adverbs removed (*simply*, *just*, *easy*, *obviously*, *clearly*)?
* [ ] Are exclamation marks removed?
* [ ] Is "please" removed from instructions?

### Pass 2: Headings & Structure
* [ ] Are all headings in sentence case (only first word and proper nouns capitalized)?
* [ ] Are all trailing periods removed from headings?
* [ ] Do all lists have at least two items?
* [ ] Do lists have clear lead-in sentences ending with a colon (`:`)?
* [ ] Are numbered lists reserved strictly for sequential procedures?
* [ ] Is the serial (Oxford) comma used consistently?

### Pass 3: Code and UI Formatting
* [ ] Are code identifiers, filenames, paths, commands, flags, and HTTP methods formatted in backticks?
* [ ] Are visible UI buttons, menus, fields, and windows formatted in **bold**?
* [ ] Are standard UI interaction verbs used (*click* buttons, *select* options, *enter* text, *press* keys)?
* [ ] Do code blocks have language syntax tags?
* [ ] Are user placeholders formatted clearly in uppercase or angle brackets (e.g. `<PROJECT_ID>`)?
* [ ] Are code omissions marked with language comments rather than bare ellipses (`...`)?

### Pass 4: Procedures and Clarity
* [ ] Does each procedural step begin with an imperative verb?
* [ ] Are conditions placed before instructions?
* [ ] Is the action separated from the system result?
* [ ] Does the procedure include prerequisites and a verification step?

### Pass 5: Word Choice & Inclusivity
* [ ] Is "allow" used for permissions, and "enable" for features?
* [ ] Is "because" used for cause, and "since" reserved only for time?
* [ ] Are Latin abbreviations replaced (*for example*, *that is*, *and so on*)?
* [ ] Are two-word verbs distinguished from single-word nouns (*log in* vs *login*, *set up* vs *setup*)?
* [ ] Are non-inclusive terms replaced (*allowlist*, *primary/replica*, *smoke test*, *on-path attacker*)?
* [ ] Do links have descriptive, standalone anchor text?
