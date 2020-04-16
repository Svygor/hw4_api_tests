import pytest
import cerberus
import requests

schema = {
          'message': {'type': 'list'},
          'status': {'type': 'string'}
}


@pytest.mark.parametrize('breed, count', [('hound', 1000), ('brabancon', 153)])
def test_all_imgs(breed, count):
    response = requests.get('https://dog.ceo/api/breed/' + breed + '/images')
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)
    assert len(response.json()['message']) == count