import requests
import pytest


@pytest.mark.parametrize("breed", ["bullterrier", "hound", "setter", "terrier"])
def test_valid_date(base_url, breed):
    res = requests.get(base_url + f"breed/{breed}/list")
    assert res.status_code == 200
    assert res.json().get("status") == "success"


def test_invalid_date(base_url):
    res = requests.get(base_url + "breed/uncorrectbreed/list")
    assert res.status_code == 404
    assert res.json().get("status") == "error"


@pytest.mark.parametrize("breed, sub_breed",
                         [("bullterrier", "staffordshire"),
                          ("hound", "ibizan"),
                          ("setter", "gordon"),
                          ("terrier", "fox")])
def test_validation_sub_breed_in_json(base_url, breed, sub_breed):
    res = requests.get(base_url + f"breed/{breed}/{sub_breed}/images")
    for i in res.json().get("message"):
        assert i.split("/")[4].find(f"{breed}-{sub_breed}") == 0


@pytest.mark.parametrize("breed, sub_breed",
                         [("bullterrier", "staffordshire"),
                          ("hound", "ibizan"),
                          ("setter", "gordon"),
                          ("terrier", "fox")])
def test_validation_sub_breed_random_in_json(base_url, breed, sub_breed):
    res = requests.get(base_url + f"breed/{breed}/{sub_breed}/images" + "/random")
    assert res.json().get("message").split("/")[4].find(f"{breed}-{sub_breed}") == 0


@pytest.mark.parametrize("param, result",
                         [("three", 1),
                          (-5, 10),
                          (0, 1),
                          (1, 1),
                          (25, 25),
                          (50, 50),
                          (80, 80)])
@pytest.mark.parametrize("breed, sub_breed",
                         [("bullterrier", "staffordshire"),
                          ("hound", "ibizan"),
                          ("setter", "gordon"),
                          ("terrier", "fox")])
def test_validation_sub_breed_count_random_in_json(base_url, param, result, breed, sub_breed):
    res = requests.get(base_url + f"breed/{breed}/{sub_breed}/images" + "/random/" + str(param))
    assert len(res.json().get("message")) == result
    for i in res.json().get("message"):
        assert i.split("/")[4].find(f"{breed}-{sub_breed}") == 0
