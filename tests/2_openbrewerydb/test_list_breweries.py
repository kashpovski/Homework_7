import requests
import jsonschema
import pytest


def test_valid_date(base_url, schema):
    res = requests.get(base_url)
    try:
        jsonschema.validate(instance=res.json(), schema=schema)
        result = True
    except jsonschema.ValidationError:
        result = False
    assert res.status_code == 200
    assert result is True, "schema is not valid"


@pytest.mark.parametrize("city",
                         ["San Francisco",
                          "Atascadero",
                          "Holland",
                          "La Verne"])
def test_valid_by_city(base_url, city):
    res = requests.get(base_url, params=f"by_city={city}")
    for i in res.json():
        assert i.get("city").lower().find(city.lower()) != -1


@pytest.mark.parametrize("name",
                         ["Brew",
                          "comP",
                          "hILl",
                          "Pitch"])
def test_valid_by_name(base_url, name):
    res = requests.get(base_url, params=f"by_name={name}")
    for i in res.json():
        assert i.get("name").lower().find(name.lower()) != -1


@pytest.mark.parametrize("postal",
                         ["5552",
                          "90292",
                          "90292-5552"])
def test_valid_by_postal(base_url, postal):
    res = requests.get(base_url, params=f"by_postal={postal}")
    for i in res.json():
        assert i.get("postal_code").find(postal) != -1


@pytest.mark.parametrize("type",
                         ["micro",
                          "nano",
                          "regional",
                          "brewpub",
                          "large",
                          "planning",
                          "bar",
                          "contract",
                          "closed"])
def test_valid_by_type(base_url, type):
    res = requests.get(base_url, params=f"by_type={type}")
    for i in res.json():
        assert i.get("brewery_type").find(type) != -1


@pytest.mark.parametrize("type",
                         ["Micro",
                          "nanO",
                          "regionality",
                          "brew",
                          "proprietor",
                          "nontype"])
def test_invalid_by_type(base_url, type):
    res = requests.get(base_url, params=f"by_type={type}")
    assert res.json().get("errors") != "Brewery type must include one of these types: [\"micro\", \"nano\"," \
                                       " \"regional\", \"brewpub\", \"large\", \"planning\", \"bar\", \"contract\"," \
                                       " \"proprieter\", \"closed\"]"


@pytest.mark.parametrize("per_page, result",
                         [("three", 20),
                          (-1, 20),
                          (0, 0),
                          (1, 1),
                          (25, 25),
                          (50, 50),
                          (60, 50)])
def test_valid_by_per_page(base_url, per_page, result):
    res = requests.get(base_url, params=f"per_page={per_page}")
    assert len(res.json()) == result


@pytest.mark.parametrize("per_page_1, page_1, per_page_2, page_2", [(4, 1, 3, 2)])
def test_valid_by_page(base_url, per_page_1, page_1, per_page_2, page_2):
    res_1 = requests.get(base_url, params={"per_page": per_page_1, "page": page_1})
    res_2 = requests.get(base_url, params={"per_page": per_page_2, "page": page_2})
    assert res_2.json()[0] == res_1.json()[-1]
