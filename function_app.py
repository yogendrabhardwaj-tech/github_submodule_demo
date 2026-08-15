"""Azure Functions app entrypoint."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import azure.functions as func

from shared.config import get_settings
from shared.errors import AppError, error_response, json_response
from shared.validation import validate_echo_payload

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="health", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def health(req: func.HttpRequest) -> func.HttpResponse:
    settings = get_settings()
    return json_response(
        {
            "status": "ok",
            "service": settings.app_name,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    )


@app.route(route="echo", methods=["POST"])
def echo(req: func.HttpRequest) -> func.HttpResponse:
    try:
        payload = req.get_json()
    except ValueError:
        return error_response(AppError("invalid_json", "Request body must be valid JSON."))

    try:
        validated = validate_echo_payload(payload)
    except AppError as error:
        return error_response(error)

    return json_response(
        {
            "message": validated["message"],
            "metadata": validated["metadata"],
        },
        status_code=200,
    )
