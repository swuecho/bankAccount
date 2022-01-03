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
