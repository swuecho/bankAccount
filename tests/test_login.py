def test_login_correct(client):
    rv = client.post('/login', json=dict(username='admin', password='test'))
    print(rv.json)
    assert rv.status_code == 200


def test_login_fail(client):
    rv = client.post('/login',
                     json=dict(username='admin', password='wrongpass'))
    print(rv.json)
    assert rv.status_code == 401
