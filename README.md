# github_submodule_demo

Sample Azure Functions repository containing four independent HTTP-trigger functions:

- `invoice`
- `shipping`
- `vendor`
- `product`

Each function returns its own sample JSON data and can be called independently.

## Structure

```
InvoiceFunction/
ShippingFunction/
VendorFunction/
ProductFunction/
host.json
requirements.txt
```

## Run locally

1. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

2. Start Azure Functions runtime:

   ```bash
   func start --python
   ```

3. Open the Swagger UI in the browser:

   ```text
   http://localhost:7071/api/swagger
   ```

4. Call endpoints directly:

- `GET /api/invoice`
- `GET /api/shipping`
- `GET /api/vendor`
- `GET /api/product`

The Swagger page also exposes the OpenAPI document at:

```text
http://localhost:7071/api/swagger/openapi.json
```

## CI/CD: deploy to dev, test, prod

Two workflows drive the pipeline:

- [.github/workflows/cicd-pipeline.yml](.github/workflows/cicd-pipeline.yml) — builds the package once, then calls the reusable deploy workflow for `dev` → `test` → `prod` in order (each stage requires the previous one to succeed).
- [.github/workflows/deploy-function.yml](.github/workflows/deploy-function.yml) — reusable workflow that logs in to Azure via OIDC and deploys the package to the target Function App.

### One-time setup per environment

For each of `dev`, `test`, `prod`:

1. Create a GitHub **Environment** (repo Settings → Environments) named `dev`, `test`, `prod`. Add required reviewers on `test`/`prod` if you want manual approval gates before promotion.
2. Create a Microsoft Entra app registration (or reuse one) and add a **federated credential** scoped to `repo:<org>/<repo>:environment:<dev|test|prod>` so GitHub Actions can authenticate without storing a client secret.
3. Grant that app's service principal the **Contributor** role (or a narrower custom role limited to `Microsoft.Web/sites/*` on the target Function App) on the target Function App resource.
4. Add these secrets to each GitHub Environment:
   - `AZURE_CLIENT_ID` — the app registration's client ID
   - `AZURE_TENANT_ID` — your Entra tenant ID
   - `AZURE_SUBSCRIPTION_ID` — the subscription containing that environment's Function App
   - `AZURE_FUNCTIONAPP_NAME` — the Function App name for that environment (e.g. `func-demo-dev`, `func-demo-test`, `func-demo-prod`)

No publish-profile secrets are used — auth is via OIDC federated credentials, so there are no long-lived credentials stored in GitHub.

### Triggering

- Push to `main` runs the full pipeline automatically (dev → test → prod).
- Manual runs are available from the Actions tab via `workflow_dispatch`.