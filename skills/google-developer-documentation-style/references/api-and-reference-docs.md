# API and reference documentation (Google style guide)

Reference: [Google Developer Documentation Style Guide - Reference documentation](https://developers.google.com/style/reference)

## 1. Structure of an API reference topic

Each API element (function, class, method, endpoint, or configuration parameter) must follow a standardized layout:

1. **Title or signature**: Format the exact identifier or method signature in monospace code font.
2. **Short description**: Begin with a one-sentence summary of what the method or endpoint does, using an active third-person singular verb (*Returns*, *Creates*, *Deletes*, *Initializes*).
3. **HTTP method and path (REST APIs)**: Format the HTTP method in uppercase (`GET`, `POST`, `PUT`, `DELETE`) followed by the URI template.
4. **Parameters or request body**: Provide a formatted table or description list of input parameters.
5. **Returns or response body**: Describe the output type, schema, or HTTP status code.
6. **Exceptions and errors**: List the status codes or exception classes raised under failure conditions.
7. **Code example**: Provide a runnable, minimal example showing invocation and response handling.

---

## 2. Documenting parameters

Use a structured table or description list to document parameters. Include the following attributes for each parameter:

* **Name**: Formatted in code font (for example, `timeout_seconds`).
* **Type**: The data type or schema (for example, `integer`, `string`, `List[str]`).
* **Requirement**: Explicitly labeled as **Required** or **Optional**.
* **Default value**: If optional, state the default value (for example, *Defaults to `30`*).
* **Description**: Explain what the parameter controls, valid ranges, and edge cases.

### Parameter description conventions

Follow these conventions when writing parameter descriptions:

* Start parameter descriptions with a noun phrase rather than a full sentence (for example, *The maximum number of results to return.*).
* End parameter descriptions with a period.

| Parameter | Type | Requirement | Description |
| :--- | :--- | :--- | :--- |
| `project_id` | `string` | **Required** | The unique Google Cloud project identifier. |
| `max_results` | `integer` | Optional | The maximum number of entries to return. Must be between 1 and 100. Defaults to `20`. |
| `filter_query` | `string` | Optional | A Common Expression Language (CEL) expression used to filter returned entities. |

---

## 3. Documenting return values and responses

When documenting return values and responses, include the following details:

* Describe what the function or endpoint returns upon success.
* For REST APIs, specify the HTTP status code (for example, `200 OK` or `201 Created`) and the response schema.
* If a method returns `None` or void, state that explicitly (*"Returns `None` upon completion"*).

---

## 4. Documenting errors and exceptions

Document expected failure modes and error responses so developers can implement exception handling:

* **HTTP errors**: List standard status codes (`400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `429 Too Many Requests`, `500 Internal Server Error`).
* **Language exceptions**: Document specific exception types and the conditions that trigger them:
  * `ValueError`: Raised if `max_results` is negative or exceeds 100.
  * `PermissionDeniedError`: Raised if the service account lacks `roles/discoveryengine.editor`.

---

## 5. Documenting deprecations

When deprecating an API element, complete the following steps:

1. **Mark the deprecation**: Place a warning notice immediately below the title or signature.
2. **State the replacement**: Direct the developer to the modern alternative.
3. **Specify the timeline**: State when support ends or when removal occurs.
4. **Annotate code**: Use standard deprecation tags (for example, `@deprecated` or `@typing.deprecated`).

```markdown
> [!WARNING]
> **Deprecated:** `v1alpha.query_agent()` is deprecated and scheduled for removal in version 3.0. Use `v2.query_agent_stream()` instead.
```
