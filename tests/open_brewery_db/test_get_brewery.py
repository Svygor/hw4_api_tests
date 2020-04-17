import pytest
import requests
import jsonschema

schema = {
            'type': 'object', 'properties':
                {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'brewery_type': {'type': 'string'},
                    'street': {'type': 'string'},
                    'city': {'type': 'string'},
                    'state': {'type': 'string'},
                    'postal_code': {'type': 'string'},
                    'country': {'type': 'string'},
                    'longitude': {'type': ["string", "null"]},
                    'latitude': {'type': ["string", "null"]},
                    'phone': {'type': 'string'},
                    'website_url': {'type': 'string'},
                    'updated_at': {'type': 'string'},
                    'tag_list': {'type': 'array'}
                }
          }


@pytest.mark.parametrize('id', [153, 2541, 1])
def test_get_br_by_id(id):
    response = requests.get('https://api.openbrewerydb.org/breweries/' + str(id))
    assert response.status_code == 200
    try:
        check = jsonschema.validate(response.json(), schema)
    except Exception as e:
        check = str(e)
    assert check is None, check
