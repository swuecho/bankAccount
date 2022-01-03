from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    # Account.java should contains basic personal information like
    # name, gender, birthdate, or any additional properties you would think to add.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=True)
    # DOB: format 20210101
    birthday = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


def init_db():
    db.create_all()
