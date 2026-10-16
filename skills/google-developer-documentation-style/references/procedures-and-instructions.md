# Procedures and instructions (Google style guide)

Reference: [Google Developer Documentation Style Guide - Procedures](https://developers.google.com/style/procedures)

## 1. Structure of a procedure

Every task-based procedure follows a four-part structure:

1. **Goal and context**: State what the reader accomplishes by completing the procedure.
2. **Prerequisites**: List required permissions, tools, or prior configurations before the first step.
3. **Step-by-step instructions**: Provide a numbered list of sequential actions.
4. **Verification**: Explain how the reader confirms that the procedure succeeded.

---

## 2. Step construction

### Include a lead-in sentence

Introduce every numbered procedure with a complete lead-in sentence ending with a colon (`:`):

* *To deploy the application to Cloud Run, complete the following steps:*
* *To authenticate your local environment, run the following commands:*

### Use the imperative mood

Start every action step with an **imperative verb** (command form). Do not use gerunds (*-ing*), passive voice, or future tense:

| Avoid | Recommended (imperative) |
| :--- | :--- |
| You should click the **Save** button. | Click **Save**. |
| Creating a service account is the next step. | Create a service account. |
| The next thing to do is run `uv sync`. | Run `uv sync`. |

### Focus on one action per step

Keep each step focused on **one discrete action**. If a step requires two closely related actions (for example, entering a name and clicking **Next**), combine them only if natural; otherwise, separate them into sequential steps.

### State the action first, and the result second

Always state the action that the reader takes **before** describing the system reaction. Place the system result in a new sentence following the action:

| Avoid | Recommended |
| :--- | :--- |
| A confirmation dialog opens after clicking **Delete**. | Click **Delete**. A confirmation dialog opens. |
| To see your active deployments, run `gcloud run services list`. | Run `gcloud run services list`. The terminal lists all active services. |

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

## 4. Verification steps

Conclude every procedure with a verification step so the developer can validate that the action succeeded:

```markdown
### Verify the deployment

To verify that the service is running and healthy, complete the following steps:

1. Send a health check request to the public endpoint:
   ```bash
   curl -I https://<SERVICE_URL>/health
   ```
2. Verify that the server returns an `HTTP/2 200 OK` status response.
```
