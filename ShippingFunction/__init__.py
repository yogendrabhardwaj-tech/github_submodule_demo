import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    sample_shipping = {
        "shipmentId": "SHP-2001",
        "carrier": "Fabrikam Logistics",
        "eta": "2026-08-20",
        "status": "In Transit",
        "trackingNumber": "TRK-998877",
    }
    return func.HttpResponse(mimetype="application/json", body=json.dumps(sample_shipping))
