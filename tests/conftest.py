import os
import tempfile

import pytest

from account import create_app
from account import init_db


@pytest.fixture(scope='session')
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING':
        True,
        'SQLALCHEMY_DATABASE_URI':
        "sqlite:///" + os.path.join(db_path)
    })
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

    os.close(db_fd)
    os.unlink(db_path)