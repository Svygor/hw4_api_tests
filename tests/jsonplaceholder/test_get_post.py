import pytest
import requests


@pytest.mark.parametrize('id, title', [(1, 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'),
                                       (2, 'qui est esse'), (100, 'at nam consequatur ea labore ea harum')])
def test_post(id, title):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(id))
    assert response.status_code == 200
    assert response.json()['id'] == id
    assert response.json()['title'] == title
