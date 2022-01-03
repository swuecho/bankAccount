def test_add_user(client):
    # add user
    user_data = {"email": "user3@example.com", "username": "user3"}
    rv = client.post('/account', json=user_data)
    assert rv.json == {'id': 1}

    rv_put = client.put(f"/account/{rv.json['id']}",
                        json={"username": "user5"})
    assert rv_put.json['username'] == 'user5'
    # check user exists in db
    rv_get = client.get(f"/account/{rv.json['id']}")
    assert rv_get.json['email'] == user_data['email']

    # delete user
    rv_del = client.delete(f"/account/{rv.json['id']}")
    assert rv_del.json == {'id': 1}
    # check user not exists any more
    rv_get_not_exits = client.get(f"/account/{rv.json['id']}")
    rv_get_not_exits.status == 404
