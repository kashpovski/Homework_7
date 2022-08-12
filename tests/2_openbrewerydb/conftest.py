import requests
import pytest


@pytest.fixture
def base_url():
    return "https://api.openbrewerydb.org/breweries"


@pytest.fixture
def schema_single():
    schema_single = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "required": [
            "id",
            "name",
            "brewery_type",
            "street",
            "address_2",
            "address_3",
            "city",
            "state",
            "county_province",
            "postal_code",
            "country",
            "longitude",
            "latitude",
            "phone",
            "website_url",
            "updated_at",
            "created_at"
        ]
    }
    return schema_single


@pytest.fixture
def schema():
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "required": [
                    "id",
                    "name",
                    "brewery_type",
                    "street",
                    "address_2",
                    "address_3",
                    "city",
                    "state",
                    "county_province",
                    "postal_code",
                    "country",
                    "longitude",
                    "latitude",
                    "phone",
                    "website_url",
                    "updated_at",
                    "created_at"
                ]
            }
        ]
    }
    return schema


@pytest.fixture
def schema_autocomplete():
    schema_autocomplete = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"}
                },
                "required": [
                    "id",
                    "name"
                ]
            }
        ]
    }
    return schema_autocomplete
