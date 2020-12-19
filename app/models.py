from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app.extensions import db
from app.extensions import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    favorite_stock = db.Column(db.String(5))
    state_code = db.Column(db.String(2))
    age = db.Column(db.Integer)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_favorite_stock(self, favorite_stock):
        self.favorite_stock = favorite_stock

    def set_state_code(self, state_code):
        self.state_code = state_code

    def set_age(self, age):
        self.age = age

    def __repr__(self):
        return '<User {}>'.format(self.username)
