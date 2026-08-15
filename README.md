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