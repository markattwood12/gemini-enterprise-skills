# Voice and Tone (Google Style Guide)

Reference: [Google Developer Documentation Style Guide - Voice and Tone](https://developers.google.com/style/tone)

## Core Principles

Google developer documentation strives to be:
* **Conversational and friendly**, yet professional and objective.
* **Direct and concise**, valuing the reader's time.
* **Accessible and neutral**, avoiding regional slang, idioms, or cultural references that don't translate globally.

---

## 1. Person: Use Second Person ("You")

Always address the reader directly as **you**. 
* Do not use the first person plural (**we**, **our**, **us**) to refer to Google, the system, or the author.
* Do not use the first person singular (**I**, **my**, **me**).
* Avoid the third person (**the user**, **the developer**) when giving instructions.

| Avoid | Recommended |
| :--- | :--- |
| In this section, we will demonstrate how to deploy the container. | In this section, you learn how to deploy the container. |
| The developer must configure their API key before running the query. | Configure your API key before running the query. |
| We recommend using Terraform. | Use Terraform to manage your infrastructure. |

---

## 2. Voice: Active Voice over Passive Voice

Use **active voice** so it is immediately clear who or what performs the action. Active voice is crisper, shorter, and easier to understand for international readers.

| Avoid (Passive) | Recommended (Active) |
| :--- | :--- |
| The request is processed by the server and a JSON response is returned. | The server processes the request and returns a JSON response. |
| If an error is encountered by the application... | If the application encounters an error... |
| The configuration file should be saved in the root directory. | Save the configuration file in the root directory. |

> [!NOTE]
> Passive voice is acceptable only when the actor is genuinely unknown or irrelevant, or when emphasizing the object of the action (for example: *"Your API key is encrypted and stored in Secret Manager"*).

---

## 3. Tense: Present Tense

Write in the **present tense**. Document what the software does right now, not what it will do in the future.

| Avoid (Future Tense) | Recommended (Present Tense) |
| :--- | :--- |
| When you click Submit, the modal will close and the page will refresh. | When you click **Submit**, the modal closes and the page refreshes. |
| The function will return a promise that resolves to a User object. | The function returns a promise that resolves to a `User` object. |

---

## 4. Tone: Conversational, Confident, and Objective

### Use Common Contractions
Use standard, natural two-word contractions (*you'll*, *don't*, *it's*, *there's*, *can't*) to keep the prose approachable. 
* Avoid ambiguous, archaic, or awkward contractions (*ain't*, *would've*, *could've*, *they'd*).

### Eliminate Exclamation Points
Do not use exclamation marks (`!`) in conceptual, reference, or procedural documentation. Let the technical clarity convey excitement or emphasis.

| Avoid | Recommended |
| :--- | :--- |
| Congratulations, you're ready to deploy your agent! | You are now ready to deploy your agent. |
| Fasten your seatbelts! | Get started with the following steps. |

### Avoid Condescending and Minimizing Words
Never minimize the effort or complexity of technical tasks with words like **simply**, **just**, **easy**, **obviously**, **clearly**, or **basic**. What is simple to an author might be difficult for a developer encountering the tool for the first time.

| Avoid | Recommended |
| :--- | :--- |
| Simply edit the YAML file to add your key. | Edit the YAML file to add your key. |
| It's easy to deploy with just one command. | Deploy the service by running the following command: |
| Obviously, you need to enable billing first. | You must enable billing on your project before deploying. |

### Never Pre-announce or Promise Future Features
Document only current functionality. Avoid statements like:
* *"In a future release, this parameter will support OAuth."*
* *"We plan to add Python 3.15 support soon."*
If a feature is in preview or beta, label its current status objectively.

---

## 5. Front-Load Conditions

State the condition or context **before** stating the action or instruction. When readers know the condition first, they immediately recognize whether the instruction applies to them.

| Avoid | Recommended |
| :--- | :--- |
| Run the migration script if you are upgrading from v1. | If you are upgrading from v1, run the migration script. |
| Click **Cancel** to discard your changes. | To discard your changes, click **Cancel**. |
