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
   func start
   ```

3. Call endpoints:

- `GET /api/invoice`
- `GET /api/shipping`
- `GET /api/vendor`
- `GET /api/product`