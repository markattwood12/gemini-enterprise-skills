# Code and UI formatting (Google style guide)

Reference: [Google Developer Documentation Style Guide - Code in text and UI elements](https://developers.google.com/style/code-in-text)

## 1. Code in text

Apply monospace font (backticks `` ` `` in Markdown) to indicate that text is entered verbatim, represents a machine identifier, or separates code entities from prose.

### Elements to format as code

Format the following technical elements in monospace font:

* **Commands and utilities**: `gcloud`, `kubectl`, `git`, `uv`, `pytest`, `terraform`
* **Filenames and directory paths**: `README.md`, `agent.yaml`, `/etc/nginx/nginx.conf`
* **Programming identifiers**: classes (`PreflightChecker`), functions (`create_session()`), methods, variables, constants (`MAX_RETRIES`), and types (`Dict[str, Any]`)
* **Configuration attributes and keys**: `service_name`, `target_type`, `rate_limit_per_minute`
* **HTTP methods and status codes**: `GET`, `POST`, `PUT`, `200 OK`, `404 Not Found`
* **Standard library modules and packages**: `urllib.request`, `fastapi`, `pydantic`
* **Command flags and arguments**: `--project-id`, `-var`, `--auto-approve`

---

## 2. User interface elements

Format all visible software user interface (UI) elements in **bold text** (`**Element**`). Do not use backticks or italics for UI elements.

### UI elements to format in bold

Apply bold formatting to the following UI components:

* **Buttons**: **Submit**, **Cancel**, **Save**, **Create Service Account**
* **Menu items and navigation paths**: **File** > **Open Recent**, **IAM & Admin** > **Roles**
* **Dialog titles and window headers**: **Edit Configuration** dialog, **Select a Project** window
* **Field names and labels**: **Service Account ID** field, **Billing Account** menu
* **Tabs and sections**: **Overview** tab, **Metrics** pane
* **Radio buttons and checkboxes**: **Enable Cloud Armor** checkbox

### UI interaction verbs

Use standard verbs when instructing readers to interact with UI components:

| UI component | Recommended verb | Example | Avoid |
| :--- | :--- | :--- | :--- |
| **Button, link** | **Click** | Click **Deploy**. | Hit, press, punch |
| **Checkbox, radio button, option** | **Select** or **Clear** | Select the **Safe Mode** checkbox. | Check, tick, uncheck |
| **Menu** | **Select** | In the **Region** menu, select **us-central1**. | Pick, choose |
| **Text field** | **Enter** | In the **Project ID** field, enter your project ID. | Type in, punch in |
| **Keyboard key** | **Press** | Press `Enter`. | Hit, tap (unless on mobile) |
| **Touchscreen or mobile** | **Tap** | Tap **Sign In**. | Click |

---

## 3. Code samples and blocks

### Fenced code blocks with language identifiers

Always declare the syntax language identifier on the opening fence:

````markdown
```bash
gcloud run services list --project=my-project
```
````

### Line wrapping and length

Follow these line-length guidelines in code blocks:

* Wrap code lines at **80 characters** where possible.
* Use line-continuation characters (`\` in Bash and Python) for multi-line commands:

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="serviceAccount:deployer@my-project.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"
```

### Command prompt conventions

Observe the following rules regarding shell prompt symbols:

* Omit the command prompt symbol (`$`) when showing commands meant for one-click copying.
* Include the prompt symbol (`$`) only when showing commands alongside their expected console output in the same block:

```bash
$ gcloud storage buckets list
gs://my-project-tfstate
gs://my-project-staging
```

### Placeholders and variables

Format user-supplied variables by using uppercase identifiers enclosed in angle brackets:

* `<PROJECT_ID>`
* `<REGION>`
* `<SERVICE_ACCOUNT_EMAIL>`

Alternatively, use standard shell variable syntax (`${PROJECT_ID}`). Explain all placeholders immediately before or after the code snippet.

### Code omissions

In runnable code samples, do not use bare ellipses (`...`) without comment indicators, because bare ellipses break syntax checking. Use language-specific comments to indicate omitted sections:

```python
def query_agent(prompt: str) -> str:
    # Set up client credentials
    client = get_client()
    # Code omitted for brevity
    return client.send(prompt)
```
