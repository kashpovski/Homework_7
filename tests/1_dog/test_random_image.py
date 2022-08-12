import requests
import pytest


def test_valid_date(base_url):
    res = requests.get(base_url + "breeds/image/random")
    assert res.status_code == 200
    assert res.json().get("status") == "success"


def test_invalid_date(base_url):
    res = requests.get(base_url + "breeds/image/uncorrecturl")
    assert res.status_code == 404
    assert res.json().get("status") == "error"


@pytest.mark.parametrize("param, result",
                         [("three", 1),
                          (-5, 1),
                          (0, 1),
                          (1, 1),
                          (25, 25),
                          (50, 50),
                          (80, 50)])
def test_validation_json(base_url, param, result):
    res = requests.get(base_url + "breeds/image/random/" + str(param))
    assert len(res.json().get("message")) == result
