import requests
import pytest


@pytest.fixture
def base_url():
    return "https://dog.ceo/api/"


@pytest.fixture
def schema():
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "message": {
                "type": "object",
            },
            "status": {
                "type": "string"
            }
        },
        "required": [
            "message",
            "status"
        ]
    }
    return schema


@pytest.fixture(params=["african", "boxer", "setter", "whippet"])
def breed(request):
    return request.param
