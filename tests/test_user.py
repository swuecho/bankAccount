def test_add_user(client):
    # post with data
    user_data = {"email": "user3@example.com", "username": "user3"}
    rv = client.post('/account', data=user_data)
    assert rv.data == b'Hello, World!'
