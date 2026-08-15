import json

import azure.functions as func

from function_app import echo, health


def test_health_returns_service_status():
    req = func.HttpRequest(method="GET", url="http://localhost/api/health", body=b"")

    response = health(req)

    assert response.status_code == 200
    payload = json.loads(response.get_body())
    assert payload["status"] == "ok"
    assert "timestamp" in payload


def test_echo_returns_payload():
    req = func.HttpRequest(
        method="POST",
        url="http://localhost/api/echo",
        body=b'{"message":"hello","metadata":{"source":"test"}}',
    )

    response = echo(req)

    assert response.status_code == 200
    payload = json.loads(response.get_body())
    assert payload == {"message": "hello", "metadata": {"source": "test"}}


def test_echo_rejects_invalid_json():
    req = func.HttpRequest(method="POST", url="http://localhost/api/echo", body=b"not-json")

    response = echo(req)

    assert response.status_code == 400
    payload = json.loads(response.get_body())
    assert payload["error"]["code"] == "invalid_json"


def test_echo_rejects_invalid_payload():
    req = func.HttpRequest(
        method="POST",
        url="http://localhost/api/echo",
        body=b'{"metadata":{"source":"test"}}',
    )

    response = echo(req)

    assert response.status_code == 400
    payload = json.loads(response.get_body())
    assert payload["error"]["code"] == "invalid_message"


def test_echo_rejects_invalid_metadata():
    req = func.HttpRequest(
        method="POST",
        url="http://localhost/api/echo",
        body=b'{"message":"hello","metadata":"bad"}',
    )

    response = echo(req)

    assert response.status_code == 400
    payload = json.loads(response.get_body())
    assert payload["error"]["code"] == "invalid_metadata"


def test_echo_rejects_non_string_message():
    req = func.HttpRequest(
        method="POST",
        url="http://localhost/api/echo",
        body=b'{"message":123}',
    )

    response = echo(req)

    assert response.status_code == 400
    payload = json.loads(response.get_body())
    assert payload["error"]["code"] == "invalid_message"
