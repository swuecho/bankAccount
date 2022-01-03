def test_hello(client):
    rv = client.get('/hello', follow_redirects=True)
    assert rv.data == b'Hello, World!'


def test_hello_protected(client):
    rv = client.get('/hello_protected', follow_redirects=True)
    print(rv.data)
    assert rv.json == {"msg":"Missing Authorization Header"} 
