import requests
import jsonschema
import pytest


def test_valid_date(base_url, schema):
    res = requests.get(base_url + "/search", params={"query": "brew"})
    try:
        jsonschema.validate(instance=res.json(), schema=schema)
        result = True
    except jsonschema.ValidationError:
        result = False
    assert res.status_code == 200
    assert result is True, "schema is not valid"


@pytest.mark.xfail(reason="The maximum number of breweries returned is more 15")
def test_valid_date_autocomplete(base_url, schema_autocomplete):
    res = requests.get(base_url + "/autocomplete", params={"query": "brew"})
    try:
        jsonschema.validate(instance=res.json(), schema=schema_autocomplete)
        result = True
    except jsonschema.ValidationError:
        result = False
    assert res.status_code == 200
    assert result is True, "schema is not valid"
    assert len(res.json()) <= 15


