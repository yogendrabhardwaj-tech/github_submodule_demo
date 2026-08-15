import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    sample_product = {
        "productId": "PRD-4001",
        "name": "Wireless Keyboard",
        "sku": "KB-001-WL",
        "price": 79.99,
        "stock": 120,
    }
    return func.HttpResponse(mimetype="application/json", body=json.dumps(sample_product))
