# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A sample Azure Functions app (Python v1 / folder-based programming model) exposing independent HTTP-trigger endpoints that each return static sample JSON. It exists as a CI/CD demo, not a production service.

## Commands

Install dependencies and run the Functions host locally (requires the Azure Functions Core Tools `func` CLI):

```bash
python -m pip install -r requirements.txt
func start --python
```

Endpoints (anonymous auth, GET only):
- `GET /api/invoice`
- `GET /api/shipping`
- `GET /api/vendor`
- `GET /api/product`
- `GET /api/swagger` — Swagger UI
- `GET /api/swagger/openapi.json` — OpenAPI document

There is no test suite yet — `npm test` is a stub (`package.json`), and `playwright` is present only as a devDependency for future browser-driven tests.

## Architecture

**Python v1 Functions model**: each endpoint is its own top-level folder containing `__init__.py` (a `main(req: func.HttpRequest) -> func.HttpResponse` handler) and `function.json` (declares the `httpTrigger` binding, route, and allowed methods). This is the older folder-per-function layout, not the newer `@app.route` decorator model — new endpoints must follow the same two-file pattern, not be added as decorated functions in a single file.

**Data functions are intentionally independent and stateless**: `InvoiceFunction`, `ShippingFunction`, `VendorFunction`, `ProductFunction` each hardcode one sample JSON record and have no shared code, imports, or dependencies on each other.

**`SwaggerFunction` is a hand-maintained API catalog, not auto-generated**: its route is `swagger/{*path}` (a catch-all), and `__init__.py` branches on the wildcard path — `openapi.json` returns a manually built OpenAPI 3.0.1 spec (`FUNCTIONS` dict), any other path serves an HTML page that loads `swagger-ui-dist` from a CDN pointed at that spec. Because the spec is a hardcoded dict rather than introspected from the other functions, **adding, removing, or changing a data function's route requires manually updating `FUNCTIONS` in `SwaggerFunction/__init__.py` to keep the Swagger doc in sync**.

**`host.json`** is minimal (just declares the 2.0 extension bundle schema) — no custom logging or route-prefix overrides.
