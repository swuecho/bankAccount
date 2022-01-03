
def test_hello(client):
    rv = client.get('/hello', follow_redirects=True)
    assert rv.data == b'Hello, World!' 