import requests


def test_posts_status_code():
    body = {
        "title": "my_title",
        "body": "Новое тело",
        "userId": 10
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body)
    assert response.status_code == 201, response.text
    assert response.json()['id'] == 101
    assert response.json()['title'] == 'my_title', response.text
    assert response.json()['body'] == 'Новое тело', response.text
    assert response.json()['userId'] == 10, response.text
