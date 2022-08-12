import requests
import jsonschema
import pytest


@pytest.mark.parametrize("id_brewing",
                         ["seven-stills-san-francisco-2",
                          "dead-oak-brewing-company-atascadero",
                          "our-brewing-co-holland",
                          "la-verne-brewing-la-verne"])
def test_valid_date(base_url, schema_single, id_brewing):
    res = requests.get(base_url + f"/{id_brewing}")
    try:
        jsonschema.validate(instance=res.json(), schema=schema_single)
        result = True
    except jsonschema.ValidationError:
        result = False
    assert res.status_code == 200
    assert result is True, "schema is not valid"


def test_invalid_date(base_url):
    res = requests.get(base_url + "/unknown-brewing")
    assert res.status_code == 404
    assert res.json().get("message") == "Couldn't find Brewery"