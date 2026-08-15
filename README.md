# github_submodule_demo

Python Azure Functions project with two HTTP functions:

- `GET /api/health` (anonymous): health/status endpoint.
- `POST /api/echo` (function key auth): validates and echoes JSON payload.

## Requirements

- Python 3.12+
- Azure Functions Core Tools v4

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r requirements-dev.txt`
3. Create local settings:
   - `cp local.settings.json.example local.settings.json`
4. Start Functions host:
   - `func start`

## Request examples

`POST /api/echo`

```json
{
  "message": "hello",
  "metadata": {
    "source": "local"
  }
}
```

## Tests

Run unit tests:

- `pytest`

## Deployment

GitHub Actions workflow at:

- `.github/workflows/azure-functions.yml`

Set these repository secrets before deployment:

- `AZURE_FUNCTIONAPP_NAME`
- `AZURE_FUNCTIONAPP_PUBLISH_PROFILE`
