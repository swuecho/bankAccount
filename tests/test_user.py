import pytest


@pytest.fixture()
def test_get_token(client):
    rv = client.post('/login', json=dict(username='admin', password='test'))
    token = rv.json['access_token']
    return token


def test_add_user(client, test_get_token):
    # add user
    jwt_token = test_get_token
    print(jwt_token)
    headers = {'Authorization': f"Bearer {jwt_token}"}

    user_data = {
        "email": "user3@example.com",
        "username": "user3",
        "birthday": "19890506"
    }

    rv = client.post('/account', headers=headers, json=user_data)
    assert rv.json == {'id': 1}

    rv_put = client.put(f"/account/{rv.json['id']}",
                        headers=headers,
                        json={"username": "user5"})
    assert rv_put.json['username'] == 'user5'
    # check user exists in db
    rv_get = client.get(f"/account/{rv.json['id']}", headers=headers)
    assert rv_get.json['email'] == user_data['email']

    # delete user
    rv_del = client.delete(f"/account/{rv.json['id']}", headers=headers)
    assert rv_del.json == {'id': 1}
    # check user not exists any more
    rv_get_not_exits = client.get(
        f"/account/{rv.json['id']}",
        headers=headers,
    )
    rv_get_not_exits.status == 404
