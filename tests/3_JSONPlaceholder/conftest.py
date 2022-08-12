import requests
import pytest


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def schema_posts():
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "userId": {"type": "integer"},
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": [
                    "userId",
                    "id",
                    "title",
                    "body"
                ]
            }
        ]
    }
    return schema


@pytest.fixture
def schema_all_comments_of_post():
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "postId": {"type": "integer"},
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": [
                    "postId",
                    "id",
                    "name",
                    "email",
                    "body"
                ]
            }
        ]
    }
    return schema


@pytest.fixture
def schema_comments():
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "postId": {"type": "integer"},
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": [
                    "postId",
                    "id",
                    "name",
                    "email",
                    "body"
                ]
            }
        ]
    }
    return schema


@pytest.fixture
def created_json():
    json = {
        "title": "abra cadabra",
        "body": "ships tacked tacked but not caught",
        "userId": 325
    }
    return json


@pytest.fixture
def updated_json():
    json = {
        "id": 1,
        "title": "abra cadabra",
        "body": "ships tacked tacked but not caught",
        "userId": 325
    }
    return json

# @pytest.fixture(params=["african", "boxer", "setter", "whippet"])
# def breed(request):
#     return request.param
