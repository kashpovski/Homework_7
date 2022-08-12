import requests
import jsonschema
import pytest


def test_valid_date(base_url, schema_posts):
    res = requests.get(base_url + "/posts")
    try:
        jsonschema.validate(instance=res.json(), schema=schema_posts)
        result = True
    except jsonschema.ValidationError:
        result = False
    assert res.status_code == 200
    assert result is True, "schema is not valid"
    assert len(res.json()) == 100


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_valid_userid(base_url, user_id):
    res = requests.get(base_url + "/posts", params={"userId": user_id})
    assert res.status_code == 200
    for i in res.json():
        assert i.get("userId") == user_id


@pytest.mark.parametrize("user_id", [-1, 0, 11, "three"])
def test_invalid_userid(base_url, user_id):
    res = requests.get(base_url + "/posts", params={"userId": user_id})
    assert res.status_code == 200
    assert res.json() == []


@pytest.mark.parametrize("post", [1, 53, 100])
def test_valid_number_of_posts(base_url, post):
    res = requests.get(base_url + "/posts" + f"/{post}")
    assert res.status_code == 200
    assert res.json().get("id") == post


@pytest.mark.parametrize("post", [-1, 0, 101, "three"])
def test_invalid_number_of_posts(base_url, post):
    res = requests.get(base_url + "/posts" + f"/{post}")
    assert res.status_code == 404


@pytest.mark.parametrize("post", [1, 53, 100])
def test_valid_all_comments_of_post(base_url, post, schema_all_comments_of_post):
    res = requests.get(base_url + "/posts" + f"/{post}" + "/comments")
    print(res.json())
    try:
        jsonschema.validate(instance=res.json(), schema=schema_all_comments_of_post)
        result = True
    except jsonschema.ValidationError:
        result = False
    assert res.status_code == 200
    assert result is True, "schema is not valid"
    for i in res.json():
        assert i.get("postId") == post


def test_creating_a_resource(base_url, created_json):
    res = requests.post(base_url + "/posts",
                        headers={"Content-type": "application/json"},
                        json=created_json)
    assert res.status_code == 201
    for i in created_json:
        assert res.json().get(i) == created_json.get(i)


@pytest.mark.parametrize("post", [1, 50, 100])
def test_updating_a_resource(base_url, updated_json, post):
    res = requests.put(base_url + "/posts" + f"/{post}",
                       headers={"Content-type": "application/json"},
                       json=updated_json)
    assert res.status_code == 200
    for i in updated_json:
        if i == "id":
            assert res.json().get(i) == post
        else:
            assert res.json().get(i) == updated_json.get(i)
