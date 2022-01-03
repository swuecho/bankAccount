from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


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
