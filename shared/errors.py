"""Error types and response helpers."""

from __future__ import annotations

import json
from dataclasses import dataclass

import azure.functions as func


@dataclass(frozen=True)
class AppError(Exception):
    code: str
    message: str
    status_code: int = 400


def json_response(payload: dict, status_code: int = 200) -> func.HttpResponse:
    return func.HttpResponse(
        body=json.dumps(payload),
        status_code=status_code,
        mimetype="application/json",
    )


def error_response(error: AppError) -> func.HttpResponse:
    return json_response(
        payload={"error": {"code": error.code, "message": error.message}},
        status_code=error.status_code,
    )
