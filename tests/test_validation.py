import pytest

from shared.errors import AppError
from shared.validation import validate_echo_payload


def test_validate_echo_payload_success():
    data = validate_echo_payload({"message": " hello ", "metadata": {"k": "v"}})
    assert data == {"message": "hello", "metadata": {"k": "v"}}


def test_validate_echo_payload_rejects_empty_message():
    with pytest.raises(AppError) as error:
        validate_echo_payload({"message": "   "})

    assert error.value.code == "invalid_message"


def test_validate_echo_payload_rejects_invalid_metadata():
    with pytest.raises(AppError) as error:
        validate_echo_payload({"message": "hello", "metadata": "bad"})

    assert error.value.code == "invalid_metadata"
