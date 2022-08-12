import requests
from jsonschema import validate, ValidationError


def test_valid_date(base_url):
    res = requests.get(base_url + "breeds/list/all")
    assert res.status_code == 200
    assert res.json().get("status") == "success"


def test_invalid_date(base_url):
    res = requests.get(base_url + "breeds/list/uncorrecturl")
    assert res.status_code == 404
    assert res.json().get("status") == "error"


def test_validation_json(base_url, schema):
    res = requests.get(base_url + "breeds/list/all")
    try:
        validate(instance=res.json(), schema=schema)
        result = True
    except ValidationError:
        result = False
    assert result is True, "schema is not valid"
