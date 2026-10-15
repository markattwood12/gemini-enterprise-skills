# Word List & Inclusive Language (Google Style Guide)

Reference: [Google Developer Documentation Style Guide - Word List & Inclusive Documentation](https://developers.google.com/style/word-list)

## 1. Technical Terminology & Preferred Usage

### `allow` vs. `enable` vs. `let`
* **`allow`**: Use when referring to permissions, access rights, or capabilities granted to a user or identity.  
  * *The `roles/run.admin` role allows the caller to deploy services.*
* **`enable`**: Use when referring to activating a software feature, flag, service, or API.  
  * *Enable the Cloud Run API before deploying.*
* **`let`**: Avoid in formal technical documentation.

---

### `can` vs. `may` vs. `might` vs. `must` vs. `should`
* **`can`**: Indicates physical or functional capability (*"The agent can query up to 50 datasets"*).
* **`may`**: Avoid whenever possible due to ambiguity between permission and possibility. Use **can** for capability, or **have permission to** for authorization. Use **might** for probability.
* **`might`**: Indicates probability or possibility (*"If the network times out, the call might fail"*).
* **`must`**: Indicates an absolute requirement or mandatory prerequisite (*"You must provide a project ID"*).
* **`should`**: Indicates a strong recommendation, best practice, or optional step (*"You should enable rate limiting in production"*).

---

### `because` vs. `since`
* **`because`**: Always use for cause-and-effect relationships.  
  * *The build failed because the container registry was unreachable.*
* **`since`**: Reserve strictly for the passage of time.  
  * *Antigravity has supported Python 3.14 since version 2.0.*

---

### Abbreviations to Avoid (Latin Abbreviations)
Avoid Latin abbreviations in running text. Use English equivalents instead:
* Avoid **`e.g.`** $\rightarrow$ Use **`for example`** or **`such as`**.
* Avoid **`i.e.`** $\rightarrow$ Use **`that is`**.
* Avoid **`etc.`** $\rightarrow$ Rephrase with **`and so on`**, or use an introductory **`such as`** without a trailing ellipsis/etc.
* Avoid **`vs.`** in prose $\rightarrow$ Use **`versus`** or **`compared to`** (abbreviation acceptable only in table headers or charts).
* Avoid **`via`** $\rightarrow$ Use **`by using`**, **`through`**, or **`with`**.

---

### Noun vs. Verb Distinctions (Compound Words)

| As a Verb (Two Words) | As a Noun or Adjective (One Word) |
| :--- | :--- |
| **log in**: *Log in to your GCP console.* | **login**: *Enter your login credentials.* |
| **set up**: *Set up your virtual environment.* | **setup**: *The setup process takes two minutes.* |
| **clean up**: *Clean up temporary state files.* | **cleanup**: *Run the cleanup script.* |
| **back up**: *Back up your database before migrating.* | **backup**: *Restore from the latest backup.* |
| **plug in**: *Plug in the external monitor.* | **plugin**: *Install the Antigravity plugin.* |
| **shut down**: *Shut down the instance.* | **shutdown**: *Initiate a graceful shutdown.* |

---

### Capitalization and Spelling Standards

| Standard Google Form | Avoid / Incorrect |
| :--- | :--- |
| **API** | Api, api |
| **backend**, **frontend** | back-end, front-end, back end |
| **codebase** | code base, CodeBase |
| **dataset** | data set |
| **filename**, **filepath** | file name, file path |
| **ID** | Id, id |
| **lifecycle** | life cycle, life-cycle |
| **open source** (noun), **open-source** (adj) | opensource |
| **read-only** | readonly, read only |
| **real time** (noun), **real-time** (adj) | realtime |
| **standalone** | stand-alone, stand alone |
| **URL** | Url, url |
| **website** | web site, Web site |

---

### Tone-Banned Words
* **`please`**: Never use in technical instructions (*"Please click Save"* $\rightarrow$ *"Click Save"*).
* **`simply`**, **`just`**, **`easy`**, **`obviously`**, **`clearly`**: Never minimize task complexity.

---

## 2. Inclusive Documentation

Google documentation requires clear, unbiased, and inclusive language that treats all developers respectfully.

### Prohibited & Recommended Terms

| Non-Inclusive Term | Recommended Replacement | Context / Reason |
| :--- | :--- | :--- |
| **whitelist / blacklist** | **allowlist / denylist**, allow / block | Avoid racial connotations; replacement is more technically descriptive. |
| **master / slave** | **primary / replica**, main / secondary, leader / follower | Avoid references to human servitude. |
| **sanity check / sanity test** | **coherence check**, smoke test, confidence check, validation | Avoid ableist mental health metaphors. |
| **blind / blind spot** | **uninformed**, hidden, unseen, unmonitored | Avoid ableist sensory metaphors. |
| **cripple / handicap** | **degrade**, impair, slow down, limit | Avoid disability metaphors. |
| **dummy / dummy data** | **placeholder**, sample data, mock data | Avoid derogatory intelligence terms. |
| **abort / kill / terminate** | **stop**, cancel, end, exit | Avoid violent terminology (use `kill` only when referencing the exact POSIX command or signal). |
| **man-in-the-middle (MITM)** | **on-path attacker**, machine-in-the-middle | Gender-neutral, modern security standard. |
| **grandfathered** | **legacy status**, exempt, pre-existing | Historical discriminatory roots. |

### Gender-Neutral Pronouns
* Use the singular **they**, **them**, and **their** when referring to an individual whose gender is unspecified.
* Never use *he/she*, *(s)he*, or default to *he*.
* Better yet, address the reader directly using **you** and **your**.
