# API and Reference Documentation (Google Style Guide)

Reference: [Google Developer Documentation Style Guide - Reference Documentation](https://developers.google.com/style/reference)

## 1. Structure of an API Reference Topic

Each API element (function, class, method, endpoint, or configuration parameter) must follow a predictable, standardized layout:

1. **Title / Signature**: The exact identifier or method signature in monospace code font.
2. **Short Description**: A one-sentence summary of what the method or endpoint does, starting with an active third-person singular verb (*Returns*, *Creates*, *Deletes*, *Initializes*).
3. **HTTP Method & Path (REST APIs)**: Formatted with the HTTP method in uppercase (`GET`, `POST`, `PUT`, `DELETE`) followed by the URI template.
4. **Parameters / Request Body**: A formatted table or description list of input parameters.
5. **Returns / Response Body**: Explanation of the output type, schema, or HTTP status code.
6. **Exceptions / Errors**: Status codes or exception classes raised under failure conditions.
7. **Code Example**: A runnable, minimal example showing invocation and response handling.

---

## 2. Documenting Parameters

Use a structured table or definition list for parameters. Each parameter must document:

* **Name**: In code font (for example, `timeout_seconds`).
* **Type**: The data type or schema (for example, `integer`, `string`, `List[str]`).
* **Requirement**: Explicitly mark as **Required** or **Optional**.
* **Default Value**: If optional, state the default value (for example, *Defaults to `30`*).
* **Description**: Explain what the parameter controls, valid ranges, and edge cases.

### Parameter Description Conventions
* Start parameter descriptions with a phrase, not a complete sentence:
  * *The maximum number of results to return.*
  * *The timeout duration in milliseconds.*
* End parameter descriptions with a period if they contain multiple sentences.

| Parameter | Type | Required? | Description |
| :--- | :--- | :--- | :--- |
| `project_id` | `string` | **Required** | The unique GCP project identifier. |
| `max_results` | `integer` | Optional | The maximum number of entries to return. Must be between 1 and 100. Defaults to `20`. |
| `filter_query` | `string` | Optional | A CEL expression used to filter the returned entities. |

---

## 3. Documenting Return Values & Responses

* Describe what the function or endpoint returns upon success.
* For REST APIs, specify the HTTP status code (for example, `200 OK` or `201 Created`) and the response schema.
* If a method returns `None` or void, state that explicitly (*"Returns `None` upon successful completion"*).

---

## 4. Documenting Errors and Exceptions

Document expected failure modes and error responses so developers can implement robust exception handling:

* **HTTP Errors**: List standard status codes (`400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `429 Too Many Requests`, `500 Internal Server Error`).
* **Language Exceptions**: Document specific exception types and the conditions that trigger them:
  * `ValueError`: Raised if `max_results` is negative or exceeds 100.
  * `PermissionDeniedError`: Raised if the service account lacks `roles/discoveryengine.editor`.

---

## 5. Deprecations

When deprecating an API element:

1. **Mark Clearly**: Add a deprecation notice immediately below the title or signature.
2. **Explain Replacement**: Direct the developer to the modern alternative.
3. **Specify Timeline (if known)**: State when support ends or when removal occurs.
4. **Code Annotation**: Use standard deprecation tags (for example, `@deprecated` or `@typing.deprecated`).

```markdown
> [!WARNING]
> **Deprecated:** `v1alpha.query_agent()` is deprecated and will be removed in version 3.0. Use `v2.query_agent_stream()` instead.
```
