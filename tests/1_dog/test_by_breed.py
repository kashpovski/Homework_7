import requests
import pytest


def test_valid_date(base_url, breed):
    res = requests.get(base_url + f"breed/{breed}/images")
    assert res.status_code == 200
    assert res.json().get("status") == "success"


def test_invalid_date(base_url):
    res = requests.get(base_url + "breed/uncorrectbreed/images")
    assert res.status_code == 404
    assert res.json().get("status") == "error"


def test_validation_breed_in_json(base_url, breed):
    res = requests.get(base_url + f"breed/{breed}/images")
    for i in res.json().get("message"):
        assert i.split("/")[4].find(breed) == 0


def test_validation_breed_random_in_json(base_url, breed):
    res = requests.get(base_url + f"breed/{breed}/images" + "/random")
    assert res.json().get("message").split("/")[4].find(breed) == 0


@pytest.mark.parametrize("param, result",
                         [("three", 1),
                          (-5, 10),
                          (0, 1),
                          (1, 1),
                          (25, 25),
                          (50, 50),
                          (80, 80)])
def test_validation_breed_count_random_in_json(base_url, param, result, breed):
    res = requests.get(base_url + f"breed/{breed}/images" + "/random/" + str(param))
    assert len(res.json().get("message")) == result
    for i in res.json().get("message"):
        assert i.split("/")[4].find(breed) == 0
