from shared.errors import AppError
from shared.validation import validate_echo_payload


def test_validate_echo_payload_success():
    data = validate_echo_payload({"message": " hello ", "metadata": {"k": "v"}})
    assert data == {"message": "hello", "metadata": {"k": "v"}}


def test_validate_echo_payload_rejects_empty_message():
    try:
        validate_echo_payload({"message": "   "})
        assert False, "Expected AppError"
    except AppError as error:
        assert error.code == "invalid_message"


def test_validate_echo_payload_rejects_invalid_metadata():
    try:
        validate_echo_payload({"message": "hello", "metadata": "bad"})
        assert False, "Expected AppError"
    except AppError as error:
        assert error.code == "invalid_metadata"
