# github_submodule_demo

Sample Azure Functions repository demonstrating independently owned, independently deployed functions via git submodules. Each function lives in its own GitHub repo, owned by its own team member, with its own GitHub Actions workflow deploying to its own Azure Function App:

| Function | Repo | Route |
|---|---|---|
| invoice | [invoice-function](https://github.com/yogendrabhardwaj-tech/invoice-function) | `GET /api/invoice` |
| shipping | [shipping-function](https://github.com/yogendrabhardwaj-tech/shipping-function) | `GET /api/shipping` |
| vendor | [vendor-function](https://github.com/yogendrabhardwaj-tech/vendor-function) | `GET /api/vendor` |
| product | [product-function](https://github.com/yogendrabhardwaj-tech/product-function) | `GET /api/product` |

Each submodule also bundles its own Swagger docs (`GET /api/swagger`, `GET /api/swagger/openapi.json`) scoped to just that function's own endpoint.

This repo itself contains no function code — it just pins a commit of each of the four repos above via `.gitmodules`.

## Checking out

A plain `git clone` of this repo gives you the folder structure with **empty** submodule directories — nothing is fetched by default. Pull in only the function(s) you own:

```bash
git clone https://github.com/yogendrabhardwaj-tech/github_submodule_demo.git
cd github_submodule_demo
git submodule update --init invoice   # or shipping / vendor / product
```

To pull all four at once instead:

```bash
git submodule update --init --recursive
```

## Working on one function

Once initialized, each submodule folder is a normal, independent git repo — commit, push, and open PRs against `invoice-function` (etc.) directly, same as any other repo. Update the pointer in this parent repo separately when you want to publish a new pinned version:

```bash
cd invoice
git pull origin main
cd ..
git add invoice
git commit -m "Bump invoice submodule"
```

## Run one function locally

```bash
cd invoice   # or shipping / vendor / product
cp local.settings.json.example local.settings.json
python -m pip install -r requirements.txt
func start --python
```
