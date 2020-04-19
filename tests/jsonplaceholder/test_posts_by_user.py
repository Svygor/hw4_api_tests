import pytest
import requests


@pytest.mark.parametrize('userId', [1, 2, 10])
def test_posts_status_code(userId):
    response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': userId})
    for item in response.json():
        assert item['userId'] == userId, item
