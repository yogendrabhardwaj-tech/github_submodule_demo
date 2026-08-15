import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    sample_invoice = {
        "invoiceId": "INV-1001",
        "customer": "Contoso Ltd",
        "currency": "USD",
        "total": 1299.5,
        "status": "Paid",
    }
    return func.HttpResponse(mimetype="application/json", body=json.dumps(sample_invoice))
