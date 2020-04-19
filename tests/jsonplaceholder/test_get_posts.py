import pytest
import jsonschema
import requests

schema = {'type': 'array', 'items': {
                'type': 'object',
                'properties': {
                        'userId': {'type': 'integer'},
                        'id': {'type': 'integer'},
                        'title': {'type': 'string'},
                        'body': {'type': 'string'}
                }}
          }


def test_posts_status_code():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200


def test_posts_schema():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    try:
        check = jsonschema.validate(response.json(), schema)
    except Exception as e:
        check = str(e)
    assert check is None, check