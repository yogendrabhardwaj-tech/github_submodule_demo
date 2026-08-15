"""Error types and response helpers."""

from __future__ import annotations

import json

import azure.functions as func


class AppError(Exception):
    def __init__(self, code: str, message: str, status_code: int = 400) -> None:
        self.code = code
        self.message = message
        self.status_code = status_code
        super().__init__(message)


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
