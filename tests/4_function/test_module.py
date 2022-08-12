import requests


def test_status_url(base_url, status_code):
    res = requests.get(base_url)
    assert res.status_code == status_code
