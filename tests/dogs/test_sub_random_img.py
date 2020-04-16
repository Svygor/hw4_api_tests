import pytest
import cerberus
import requests


schema = {
          'message': {'type': 'string'},
          'status': {'type': 'string'}
}


@pytest.mark.parametrize('breed, sub_breed', [('hound', 'afghan'), ('hound', 'english'), ('hound', 'walker')])
def test_random_img(breed, sub_breed):
    response = requests.get('https://dog.ceo/api/breed/' + breed + '/' + sub_breed + '/images/random')
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)