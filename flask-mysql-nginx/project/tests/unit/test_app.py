"""
Get '/ping' response
"""
def test_ping(client):
    res = client.get('/ping')
    assert res.status_code == 200
    response_json = res.get_json()
    expected = {'message': 'Pong!'}
    assert response_json == expected

"""
Get list of
"""
def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert 'books' in response.get_json()

"""
Test post new book
"""
def test_post_book(client):
    data = {
        'title': 'Guru Aini',
        'author': 'Andre Hirata',
        'read': True
    }
    response = client.post('/books', json=data)
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Book added!'

    response = client.get('/books')
    books = response.get_json()['books']
    assert any(book['title'] == 'Guru Aini' for book in books)