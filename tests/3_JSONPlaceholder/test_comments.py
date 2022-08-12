import requests
import jsonschema
import pytest


def test_valid_date(base_url, schema_comments):
    res = requests.get(base_url + "/comments")
    try:
        jsonschema.validate(instance=res.json(), schema=schema_comments)
        result = True
    except jsonschema.ValidationError:
        result = False
    assert res.status_code == 200
    assert result is True, "schema is not valid"
    assert len(res.json()) == 500


@pytest.mark.parametrize("comments", [1, 203, 500])
def test_valid_number_of_comments(base_url, comments):
    res = requests.get(base_url + "/comments" + f"/{comments}")
    assert res.status_code == 200
    assert res.json().get("id") == comments


@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_valid_post_id(base_url, post_id):
    res = requests.get(base_url + "/comments", params={"postId": post_id})
    assert res.status_code == 200
    for i in res.json():
        assert i.get("postId") == post_id


@pytest.mark.parametrize("post_id", [-1, 0, 101, "three"])
def test_invalid_post_id(base_url, post_id):
    res = requests.get(base_url + "/posts", params={"userId": post_id})
    assert res.status_code == 200
    assert res.json() == []
