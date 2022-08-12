import requests
import jsonschema


def test_valid_date(base_url, schema):
    res = requests.get(base_url + "/random")
    try:
        jsonschema.validate(instance=res.json(), schema=schema)
        result = True
    except jsonschema.ValidationError:
        result = False
    assert res.status_code == 200
    assert result is True, "schema is not valid"
    assert len(res.json()) == 1
