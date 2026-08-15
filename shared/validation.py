"""Request validation helpers."""

from __future__ import annotations

from shared.errors import AppError


MAX_MESSAGE_LENGTH = 500


def validate_echo_payload(payload: dict) -> dict:
    if not isinstance(payload, dict):
        raise AppError("invalid_payload", "Request body must be a JSON object.")

    message = payload.get("message")
    if not isinstance(message, str):
        raise AppError("invalid_message", "'message' is required and must be a string.")

    message = message.strip()
    if not message:
        raise AppError("invalid_message", "'message' cannot be empty.")

    if len(message) > MAX_MESSAGE_LENGTH:
        raise AppError(
            "invalid_message",
            f"'message' must be {MAX_MESSAGE_LENGTH} characters or fewer.",
        )

    metadata = payload.get("metadata")
    if metadata is not None and not isinstance(metadata, dict):
        raise AppError("invalid_metadata", "'metadata' must be a JSON object.")

    return {
        "message": message,
        "metadata": metadata or {},
    }
