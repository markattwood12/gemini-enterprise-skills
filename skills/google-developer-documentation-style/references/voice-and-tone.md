# Voice and tone (Google style guide)

Reference: [Google Developer Documentation Style Guide - Voice and tone](https://developers.google.com/style/tone)

## Core principles

Google developer documentation adheres to three foundational tone principles:

* **Conversational and friendly**, while remaining professional and objective.
* **Direct and concise**, respecting the reader's time.
* **Accessible and neutral**, avoiding regional slang, idioms, or cultural references that do not translate globally.

---

## 1. Person: Use second person ("you")

Address the reader directly as **you**:

* Do not use the first-person plural (**we**, **our**, **us**) to refer to Google, the system, or the author.
* Do not use the first-person singular (**I**, **my**, **me**).
* Avoid the third person (**the user**, **the developer**) when giving instructions.

| Avoid | Recommended |
| :--- | :--- |
| In this section, we will demonstrate how to deploy the container. | In this section, you learn how to deploy the container. |
| The developer must configure their API key before running the query. | Configure your API key before running the query. |
| We recommend using Terraform. | Use Terraform to manage your infrastructure. |

---

## 2. Voice: Prefer active voice over passive voice

Use **active voice** so it is clear who or what performs the action. Active voice is shorter, clearer, and easier to read for global audiences:

| Avoid (passive) | Recommended (active) |
| :--- | :--- |
| The request is processed by the server and a JSON response is returned. | The server processes the request and returns a JSON response. |
| If an error is encountered by the application... | If the application encounters an error... |
| The configuration file should be saved in the root directory. | Save the configuration file in the root directory. |

> [!NOTE]
> Passive voice is acceptable when the actor is unknown or irrelevant, or when you must emphasize the object of the action (for example, *"Your API key is encrypted and stored in Secret Manager"*).

---

## 3. Tense: Use present tense

Write in the **present tense**. Document what the software does now, not what it will do:

| Avoid (future tense) | Recommended (present tense) |
| :--- | :--- |
| When you click Submit, the modal will close and the page will refresh. | When you click **Submit**, the modal closes and the page refreshes. |
| The function will return a promise that resolves to a User object. | The function returns a promise that resolves to a `User` object. |

---

## 4. Tone: Conversational, confident, and objective

### Use common contractions

Use standard two-word contractions (*you'll*, *don't*, *it's*, *there's*, *can't*) to keep prose approachable. Avoid ambiguous or awkward contractions (*ain't*, *would've*, *could've*, *they'd*).

### Eliminate exclamation points

Do not use exclamation marks (`!`) in conceptual, reference, or procedural documentation:

| Avoid | Recommended |
| :--- | :--- |
| Congratulations, you're ready to deploy your agent! | You are now ready to deploy your agent. |
| Fasten your seatbelts! | Complete the following steps to get started. |

### Avoid condescending and minimizing words

Never minimize the complexity of technical tasks by using words such as **simply**, **just**, **easy**, **obviously**, **clearly**, or **basic**:

| Avoid | Recommended |
| :--- | :--- |
| Simply edit the YAML file to add your key. | Edit the YAML file to add your key. |
| It's easy to deploy with just one command. | Deploy the service by running the following command: |
| Obviously, you need to enable billing first. | Enable billing on your project before deploying. |

### Do not pre-announce future features

Document only current functionality. Avoid statements about unreleased capabilities:

* Avoid: *"In a future release, this parameter will support OAuth."*
* Avoid: *"We plan to add Python 3.15 support soon."*

If a feature is in preview or beta, state its current status objectively.

---

## 5. Front-load conditions

State the condition or goal **before** stating the action or instruction. When readers see the condition first, they immediately know whether the instruction applies to them:

| Avoid | Recommended |
| :--- | :--- |
| Run the migration script if you are upgrading from v1. | If you are upgrading from v1, run the migration script. |
| Click **Cancel** to discard your changes. | To discard your changes, click **Cancel**. |
