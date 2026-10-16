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
> **Precedence clause for agency guidelines:**
> If an agency-specific standard, statutory requirement, or project-specific style manual (such as the GPO Style Manual or PlainLanguage.gov) conflicts with a rule in this guide, the agency-specific requirement takes precedence.

---

## The 10 golden rules

Apply the following 10 core principles to all developer documentation:

1. **Second person ("you")**: Address the developer directly as *you*. Never use *we*, *I*, or *the user*.
2. **Active voice**: Make the actor clear (*"The server processes the request"*, not *"The request is processed by the server"*).
3. **Present tense**: Describe what the software does now, not what it will do (*"Clicking **Submit** sends..."*, not *"will send"*).
4. **Sentence-case headings**: Capitalize only the first word and proper nouns in headings and table column headers. Never end a heading with a period or colon.
5. **Code versus UI distinction**:
   * Use code font (`` `monospace` ``) for code, filenames, CLI commands, flags, parameters, and HTTP methods.
   * Use **bold font** (`**Element**`) for UI buttons, menus, dialog titles, and fields. Never use code font for UI elements.
6. **Task-oriented procedures**:
   * Use numbered lists for sequential steps, and bulleted lists for non-sequential options (minimum two items per list).
   * Start every action step with an **imperative verb** (*Click*, *Run*, *Select*, *Specify*).
   * Separate the user action from the system result (*"Click **Save**. The details page opens."*).
7. **Front-loaded conditions**: Put conditions *before* instructions (*"If you use Python 3.14, install `uv`"* instead of *"Install `uv` if you use Python 3.14"*).
8. **Descriptive link text**: Never write *"click here"*, *"here"*, or display raw URLs as link text. Link text must be meaningful out of context.
9. **Serial (Oxford) comma**: Always include a comma before the final conjunction in a series of three or more items (*"A, B, and C"*).
10. **Inclusive and objective language**:
    * Replace non-inclusive idioms (*allowlist* instead of *whitelist*, *primary/replica* instead of *master/slave*, and *coherence check* instead of *sanity check*).
    * Remove minimizing or condescending words (*simply*, *just*, *easy*, *obviously*).
    * Never use *please* in technical instructions.

---

## Topic routing table

When auditing or drafting specific types of content, consult the corresponding reference document in `references/`:

| Documentation task | Reference document |
| :--- | :--- |
| **Voice, tone, contractions, minimizing words, and future-proofing** | [Voice and tone](references/voice-and-tone.md) |
| **Code in text, code blocks, CLI commands, placeholders, and UI elements** | [Code and UI formatting](references/code-and-ui.md) |
| **Headings, lists, tables, callouts, and link text** | [Formatting and organization](references/formatting-and-organization.md) |
| **Step-by-step procedures, prerequisites, sub-steps, and verification** | [Procedures and instructions](references/procedures-and-instructions.md) |
| **Comprehensive A–Z word list, noun versus verb forms, and inclusive language** | [Word list and inclusive language](references/word-list-and-inclusive.md) |
| **API specifications, method signatures, parameters, exceptions, and types** | [API and reference documentation](references/api-and-reference-docs.md) |

---

## Five-pass editorial review checklist

When reviewing or drafting documentation, execute the following five audit passes:

### Pass 1: Voice and tone

* [ ] Is the document addressed to "you" (with "we", "us", "our", and "the developer" removed)?
* [ ] Are sentences written in the active voice?
* [ ] Is the text written in the present tense?
* [ ] Are condescending adverbs removed (*simply*, *just*, *easy*, *obviously*, *clearly*)?
* [ ] Are exclamation marks removed?
* [ ] Is "please" removed from instructions?

### Pass 2: Headings and structure

* [ ] Are all headings and table headers in sentence case (only the first word and proper nouns capitalized)?
* [ ] Are all trailing periods and colons removed from headings?
* [ ] Do all lists contain at least two items?
* [ ] Do all lists have clear lead-in sentences ending with a colon (`:`)?
* [ ] Are numbered lists reserved strictly for sequential procedures?
* [ ] Is the serial (Oxford) comma used consistently?

### Pass 3: Code and UI formatting

* [ ] Are code identifiers, filenames, paths, commands, flags, and HTTP methods formatted in backticks?
* [ ] Are visible UI buttons, menus, fields, and windows formatted in **bold**?
* [ ] Are standard UI interaction verbs used (*click* buttons, *select* options, *enter* text, *press* keys)?
* [ ] Do fenced code blocks declare language syntax tags?
* [ ] Are user placeholders formatted in uppercase angle brackets (for example, `<PROJECT_ID>`)?
* [ ] Are code omissions marked with language comments rather than bare ellipses (`...`)?

### Pass 4: Procedures and clarity

* [ ] Does each procedural step begin with an imperative verb?
* [ ] Are conditions placed before instructions?
* [ ] Is the user action separated from the system result?
* [ ] Does the procedure include prerequisites and a verification step?

### Pass 5: Word choice and inclusivity

* [ ] Is "allow" used for permissions, and "enable" used for features?
* [ ] Is "because" used for cause, and "since" reserved strictly for time?
* [ ] Are Latin abbreviations replaced with English equivalents (*for example*, *that is*, *and so on*)?
* [ ] Are two-word verbs distinguished from single-word nouns (*log in* versus *login*, *set up* versus *setup*)?
* [ ] Are non-inclusive terms replaced (*allowlist*, *primary/replica*, *coherence check*, *on-path attacker*)?
* [ ] Do links use descriptive, standalone anchor text?
