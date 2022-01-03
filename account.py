"""
Please use your own GitHub account to upload the code and paste the repository URL into the answer field.
    • Any java framework at your preference
    • Use jwt as authentication method (you might want to create a method to generate jwt so interviewer later can verify)
    • You can use text file or h2 db for storing data
    • Junit
    • Account.java should contains basic personal information like name, gender, birthdate, or any additional properties you would think to add.
"""
from flask import Flask
import os
from flask import request

from flask.cli import with_appcontext
from flask.json import jsonify
from model import db, init_db, User
import json


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        SQLALCHEMY_DATABASE_URI="sqlite:///" +
        os.path.join(app.instance_path, "account.sqlite"),
    )

    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/initdb")
    def init_db():
        print(app.config['SQLALCHEMY_DATABASE_URI'])
        db.create_all()
        return "DB inited!"

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    @app.route("/account/<user_id>", methods=['GET'])
    def get_user_by_username(user_id):
        user = db.session.query(User).get(user_id)
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })

    @app.route("/account", methods=['POST'])
    def post_user():
        user_dict = request.get_json()
        print(user_dict)
        user = User(username=user_dict['username'], email=user_dict['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'id': user.id})

    return app

    return app


app = create_app()
