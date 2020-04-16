import pytest
import cerberus
import requests

schema = {
          'message': {'type': 'list'},
          'status': {'type': 'string'}
}


def test_sub_list():
    response = requests.get("https://dog.ceo/api/breed/hound/list")
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)
    assert response.json()['message'] == [
        "afghan",
        "basset",
        "blood",
        "english",
        "ibizan",
        "plott",
        "walker"
    ]
