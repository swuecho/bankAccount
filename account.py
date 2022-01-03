"""
Please use your own GitHub account to upload the code and paste the repository URL into the answer field.
    • Any java framework at your preference
    • Use jwt as authentication method (you might want to create a method to generate jwt so interviewer later can verify)
    • You can use text file or h2 db for storing data
    • Junit
    • Account.java should contains basic personal information like name, gender, birthdate, or any additional properties you would think to add.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)


class User(db.Model):
    # Account.java should contains basic personal information like
    # name, gender, birthdate, or any additional properties you would think to add.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


def init_db():
    db.create_all()


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

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

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    @app.route("/user/<username>", methods=['GET'])
    def get_user_by_username(username):
        return f"<p>{username}</p>"

    return app
