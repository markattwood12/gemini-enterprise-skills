# Code and UI Formatting (Google Style Guide)

Reference: [Google Developer Documentation Style Guide - Code in Text and UI Elements](https://developers.google.com/style/code-in-text)

## 1. Code in Text

Apply monospace font (backticks `` ` `` in Markdown) to signal that text is entered verbatim, represents a machine identifier, or separates code entities from natural prose.

### What to Format as Code
* **Commands and utilities**: `gcloud`, `kubectl`, `git`, `uv`, `pytest`, `terraform`
* **File names and directory paths**: `README.md`, `agent.yaml`, `/etc/nginx/nginx.conf`
* **Programming identifiers**: classes (`PreflightChecker`), functions (`create_session()`), methods, variables, constants (`MAX_RETRIES`), types (`Dict[str, Any]`)
* **Configuration attributes and keys**: `service_name`, `target_type`, `rate_limit_per_minute`
* **HTTP methods and status codes**: `GET`, `POST`, `PUT`, `200 OK`, `404 Not Found`
* **Standard library modules and packages**: `urllib.request`, `fastapi`, `pydantic`
* **Command flags and arguments**: `--project-id`, `-var`, `--auto-approve`

---

## 2. User Interface Elements

Format all visible software user interface (UI) elements in **bold text** (`**Element**`). **Do not use backticks or italics for UI elements.**

### UI Elements to Bold
* **Buttons**: **Submit**, **Cancel**, **Save**, **Create Service Account**
* **Menu items and navigation paths**: **File** > **Open Recent**, **IAM & Admin** > **Roles**
* **Dialog titles and window headers**: **Edit Configuration** dialog, **Select a Project** window
* **Field names and labels**: **Service Account ID** field, **Billing Account** dropdown
* **Tabs and sections**: **Overview** tab, **Metrics** pane
* **Radio buttons and checkboxes**: **Enable Cloud Armor** checkbox

### UI Interaction Verbs

Use precise, standard verbs when instructing readers to interact with UI components:

| UI Component | Recommended Verb | Example | Avoid |
| :--- | :--- | :--- | :--- |
| **Button, Link** | **Click** | Click **Deploy**. | Hit, press, punch |
| **Checkbox, Radio button, Option** | **Select** or **Clear** | Select the **Safe Mode** checkbox. | Check, tick, uncheck |
| **Dropdown / Menu** | **Select** | In the **Region** menu, select **us-central1**. | Pick, choose |
| **Text field** | **Enter** | In the **Project ID** field, enter your project ID. | Type in, punch in |
| **Keyboard key** | **Press** | Press `Enter`. | Hit, tap (unless on mobile) |
| **Touchscreen / Mobile** | **Tap** | Tap **Sign In**. | Click |

---

## 3. Code Samples & Blocks

### Fenced Code Blocks with Language Identifiers
Always declare the syntax language identifier on the opening fence:
````markdown
```bash
gcloud run services list --project=my-project
```
````

### Line Wrapping and Length
* Soft-wrap code lines at **80 characters** where possible.
* Use line-continuation characters (`\` in Bash, `\` in Python) for readable multi-line shell commands:
```bash
gcloud projects add-iam-policy-binding my-project \
  --member="serviceAccount:deployer@my-project.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"
```

### Command Prompt Conventions
* Omit the command prompt symbol (`$`) when showing single commands or commands meant for one-click copying.
* Include the prompt symbol (`$`) **only** when showing commands alongside their expected console output, so the reader can differentiate input from output:
```bash
$ gcloud storage buckets list
gs://my-project-tfstate
gs://my-project-staging
```

### Placeholders and Variables
* Identify user-supplied variables using uppercase identifiers enclosed in angle brackets or clear descriptive names:
  * `<PROJECT_ID>`
  * `<REGION>`
  * `<SERVICE_ACCOUNT_EMAIL>`
* Alternatively, use standard shell variable syntax: `${PROJECT_ID}`.
* Explicitly explain placeholders immediately before or after the code snippet.

### Code Omissions
* In runnable code samples, **never use bare ellipses (`...`)** without comment indicators, as it breaks syntax checking.
* Use language-specific comments to indicate omitted sections:
```python
def query_agent(prompt: str) -> str:
    # Set up client credentials...
    client = get_client()
    # Code omitted for brevity
    return client.send(prompt)
```
