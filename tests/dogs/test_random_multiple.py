import pytest
import cerberus
import requests

schema = {
          'message': {'type': 'list'},
          'status': {'type': 'string'}
}


@pytest.mark.parametrize('count', [1, 3, 50])
def test_randlom_multiple(count):
    response = requests.get('https://dog.ceo/api/breeds/image/random/' + str(count))
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)
    assert len(response.json()['message']) == count
