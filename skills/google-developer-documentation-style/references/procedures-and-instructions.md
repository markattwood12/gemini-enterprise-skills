# Procedures and Instructions (Google Style Guide)

Reference: [Google Developer Documentation Style Guide - Procedures](https://developers.google.com/style/procedures)

## 1. Structure of a Procedure

Every task-based procedure should follow a predictable structure:
1. **Goal / Context**: Explain what the user will accomplish.
2. **Prerequisites**: State any required permissions, tools, or prior tasks before starting.
3. **Step-by-Step Instructions**: A numbered list of sequential actions.
4. **Verification / Validation**: How the reader can confirm the procedure succeeded.

---

## 2. Step Construction

### Lead-In Sentence
Always introduce a numbered procedure with a clear lead-in sentence ending with a colon:
* *To deploy the application to Cloud Run, complete the following steps:*
* *To authenticate your local environment, run the following commands:*

### Imperative Mood
Start every action step with an **imperative verb** (command form). Do not use gerunds (-ing), passive voice, or future tense.

| Avoid | Recommended (Imperative) |
| :--- | :--- |
| You should click the **Save** button. | Click **Save**. |
| Creating a service account is the next step. | Create a service account. |
| The next thing to do is run `uv sync`. | Run `uv sync`. |

### One Action per Step
Keep each step focused on **one discrete action**. If a step requires two closely related actions (e.g. entering a name and clicking Next), combine them only if natural; otherwise, separate them into sequential steps.

### Action First, Result Second
Always state the action the user must take **before** describing the result or system reaction. Place the result in a new sentence following the action.

| Avoid | Recommended |
| :--- | :--- |
| A confirmation dialog opens after clicking **Delete**. | Click **Delete**. A confirmation dialog opens. |
| To see your active deployments, run `gcloud run services list`. | Run `gcloud run services list`. The terminal displays all active services. |

---

## 3. Sub-steps

When a primary step contains multiple sub-actions or optional variations, use indented sub-steps:
* Use letters (`a.`, `b.`, `c.`) or nested numbers for sequential sub-steps.
* Use bullet points (`*`) for unordered choices within a step.

```markdown
1. In the Google Cloud console, open the **Workload Identity Pools** page:
   a. In the navigation menu, click **IAM & Admin** > **Workload Identity Federation**.
   b. Click **Create Pool**.
2. Configure the pool details:
   * **Name**: Enter `github-actions-pool`.
   * **Description**: Enter an optional description.
3. Click **Continue**.
```

---

## 4. Verification Steps

Always conclude a procedure with a verification step so the developer can independently validate that their action produced the intended state:

```markdown
### Verification

To verify that the service is running and healthy:

1. Send a health check request to the public endpoint:
   ```bash
   curl -I https://<SERVICE_URL>/health
   ```
2. Verify that the server returns an `HTTP/2 200 OK` status response.
```
