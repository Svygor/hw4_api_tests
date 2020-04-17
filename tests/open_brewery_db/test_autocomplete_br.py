import pytest
import requests
import jsonschema

schema = {'type': 'array', 'items': {
                'type': 'object',
                'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'}
                }}
          }


@pytest.mark.parametrize('query', ['dog', 'new_york', 'dsfafs'])
def test_complete_br(query):
    response = requests.get('https://api.openbrewerydb.org/breweries', params={'query': query})
    assert response.status_code == 200
    try:
        check = jsonschema.validate(response.json(), schema)
    except Exception as e:
        check = str(e)
    assert check is None, check
