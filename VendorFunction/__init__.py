import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    sample_vendor = {
        "vendorId": "VND-3001",
        "name": "Northwind Supplies",
        "category": "Office Equipment",
        "contactEmail": "support@northwind.example",
        "active": True,
    }
    return func.HttpResponse(mimetype="application/json", body=json.dumps(sample_vendor))
