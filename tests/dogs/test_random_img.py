import pytest
import cerberus
import requests

schema = {
          'message': {'type': 'string'},
          'status': {'type': 'string'}
}


def test_random_img():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)