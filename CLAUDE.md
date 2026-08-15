# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A CI/CD demo of splitting an Azure Functions app into independently owned, independently deployed pieces using git submodules. This repo itself holds no function code — it pins commits of four separate GitHub repos (`invoice-function`, `shipping-function`, `vendor-function`, `product-function`) via `.gitmodules`, one per HTTP-trigger sample function.

## Commands

A plain `git clone` of this repo leaves the four submodule directories (`invoice/`, `shipping/`, `vendor/`, `product/`) empty — nothing is fetched by default. Initialize only the one(s) you need:

```bash
git submodule update --init invoice   # or shipping / vendor / product
# or, for all four:
git submodule update --init --recursive
```

Each initialized submodule is a fully independent Azure Functions project. Run one locally:

```bash
cd invoice   # or shipping / vendor / product
cp local.settings.json.example local.settings.json
python -m pip install -r requirements.txt
func start --python
```

Endpoints per function (anonymous auth, GET only): its own data route (`/api/invoice`, `/api/shipping`, `/api/vendor`, or `/api/product`), plus `GET /api/swagger` and `GET /api/swagger/openapi.json` for that function's own docs.

There is no test suite in any of the submodules yet.

## Architecture

**Each submodule is a self-contained Azure Functions app**, not a shared one: its own `host.json`, `requirements.txt`, `.funcignore`, and a bundled `SwaggerFunction` whose `FUNCTIONS` dict documents only that app's own single endpoint (not the other three) — there is no shared API catalog to keep in sync across repos.

**Python v1 Functions model** (unchanged within each submodule): a function is a folder containing `__init__.py` (a `main(req: func.HttpRequest) -> func.HttpResponse` handler) and `function.json` (the `httpTrigger` binding, route, allowed methods) — the older folder-per-function layout, not the `@app.route` decorator model.

**Deployment is per-submodule, not centralized**: each of the four repos has its own `.github/workflows/deploy.yml` that builds and deploys to that function's own Azure Function App via `Azure/functions-action@v1` on every push to its own `main`, using that repo's own `AZURE_FUNCTIONAPP_NAME` / `AZURE_FUNCTIONAPP_PUBLISH_PROFILE` secrets. This parent repo has no deploy workflow of its own — pushing here only updates which commit of each submodule is pinned, it does not trigger any deployment.

**Submodule pointers are pinned, not floating**: this repo's git index stores a specific commit SHA for each of `invoice/`, `shipping/`, `vendor/`, `product/`. Editing code inside a submodule folder and committing from the parent repo does *not* work like a normal subdirectory — you must commit and push from inside the submodule's own repo first, then separately `git add <submodule>` + commit here to bump the pinned pointer (see README.md's "Working on one function" section).

**When adding a fifth function**, follow the same pattern used to create the existing four: a new standalone GitHub repo with its own `host.json`/`requirements.txt`/`.funcignore`/bundled `SwaggerFunction`/`deploy.yml`, then `git submodule add <url> <name>` here.
