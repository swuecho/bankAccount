def test_add_user(client):
    # post with data
    user_data = {"email": "user3@example.com", "username": "user3"}
    rv = client.post('/account', json=user_data)
    assert rv.json == {'id': 1}
    rv_get = client.get(f"/account/{rv.json['id']}")
    assert rv_get.json['email'] == user_data['email']
