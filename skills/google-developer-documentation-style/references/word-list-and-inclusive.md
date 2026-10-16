# Word list and inclusive language (Google style guide)

Reference: [Google Developer Documentation Style Guide - Word list and inclusive documentation](https://developers.google.com/style/word-list)

## 1. Technical terminology and preferred usage

### `allow` versus `enable` versus `let`

Distinguish between permissions and feature activation:

* **`allow`**: Use when referring to permissions, access rights, or capabilities granted to an identity (*"The `roles/run.admin` role allows the caller to deploy services"*).
* **`enable`**: Use when referring to activating a software feature, flag, service, or API (*"Enable the Cloud Run API before deploying"*).
* **`let`**: Avoid in formal technical documentation.

---

### `can` versus `may` versus `might` versus `must` versus `should`

Use modal verbs with precise meanings:

* **`can`**: Indicates functional capability (*"The agent can query up to 50 datasets"*).
* **`may`**: Avoid due to ambiguity between permission and possibility. Use **can** for capability, **have permission to** for authorization, or **might** for probability.
* **`might`**: Indicates probability or possibility (*"If the network times out, the call might fail"*).
* **`must`**: Indicates an absolute requirement (*"You must provide a project ID"*).
* **`should`**: Indicates a recommendation or best practice (*"You should enable rate limiting in production"*).

---

### `because` versus `since`

Distinguish between causation and time:

* **`because`**: Use for cause-and-effect relationships (*"The build failed because the container registry was unreachable"*).
* **`since`**: Reserve strictly for the passage of time (*"Antigravity has supported Python 3.14 since version 2.0"*).

---

### Latin abbreviations to avoid

Replace Latin abbreviations in prose with plain English equivalents:

* Avoid **`e.g.`**; use **`for example`** or **`such as`**.
* Avoid **`i.e.`**; use **`that is`**.
* Avoid **`etc.`**; use **`and so on`**, or introduce examples with **`such as`**.
* Avoid **`vs.`** in prose; use **`versus`** or **`compared to`**.
* Avoid **`via`**; use **`by using`**, **`through`**, or **`with`**.

---

### Noun versus verb distinctions (compound words)

Distinguish between two-word verbs and one-word nouns or adjectives:

| As a verb (two words) | As a noun or adjective (one word) |
| :--- | :--- |
| **log in**: *Log in to your Google Cloud console.* | **login**: *Enter your login credentials.* |
| **set up**: *Set up your virtual environment.* | **setup**: *The setup process takes two minutes.* |
| **clean up**: *Clean up temporary state files.* | **cleanup**: *Run the cleanup script.* |
| **back up**: *Back up your database before migrating.* | **backup**: *Restore from the latest backup.* |
| **plug in**: *Plug in the security key.* | **plugin**: *Install the Antigravity plugin.* |
| **shut down**: *Shut down the instance.* | **shutdown**: *Initiate a graceful shutdown.* |

---

### Capitalization and spelling standards

Use the following standard spellings in technical documentation:

| Standard Google form | Avoid |
| :--- | :--- |
| **API** | Api, api |
| **backend**, **frontend** | back-end, front-end, back end |
| **codebase** | code base, CodeBase |
| **dataset** | data set |
| **filename**, **filepath** | file name, file path |
| **ID** | Id, id |
| **lifecycle** | life cycle, life-cycle |
| **open source** (noun), **open-source** (adjective) | opensource |
| **read-only** | readonly, read only |
| **real time** (noun), **real-time** (adjective) | realtime |
| **standalone** | stand-alone, stand alone |
| **URL** | Url, url |
| **website** | web site, Web site |

---

### Tone-restricted words

Eliminate the following words from technical instructions:

* **`please`**: Omit from technical steps (*"Click **Save**"*, not *"Please click **Save**"*).
* **`simply`**, **`just`**, **`easy`**, **`obviously`**, **`clearly`**: Never minimize task complexity.

---

## 2. Inclusive documentation

Write clear, objective, and inclusive documentation for all developers.

### Prohibited and recommended terms

Replace outdated or non-inclusive idioms with modern technical equivalents:

| Avoid | Recommended replacement | Rationale |
| :--- | :--- | :--- |
| **whitelist / blacklist** | **allowlist / denylist**, allow / block | Replaces racial metaphors with descriptive technical terms. |
| **master / slave** | **primary / replica**, main / secondary, leader / follower | Replaces human servitude metaphors. |
| **sanity check / sanity test** | **coherence check**, smoke test, confidence check, validation | Replaces ableist metaphors. |
| **blind / blind spot** | **uninformed**, hidden, unseen, unmonitored | Replaces sensory disability metaphors. |
| **cripple / handicap** | **degrade**, impair, slow down, limit | Replaces disability metaphors. |
| **dummy / dummy data** | **placeholder**, sample data, mock data | Replaces derogatory terms. |
| **abort / kill / terminate** | **stop**, cancel, end, exit | Replaces violent terminology (use `kill` only when referencing the exact POSIX command). |
| **man-in-the-middle (MITM)** | **on-path attacker**, machine-in-the-middle | Uses gender-neutral security terminology. |
| **grandfathered** | **legacy status**, exempt, pre-existing | Replaces historically discriminatory terminology. |

### Gender-neutral pronouns

Follow these rules for pronouns in technical prose:

* Address the reader directly by using **you** and **your**.
* When referring to a third-person individual, use the singular **they**, **them**, and **their**.
* Never use *he/she*, *(s)he*, or default to *he*.
