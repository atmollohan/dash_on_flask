import datetime as dt
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app.extensions import db
from app.extensions import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# watching = db.Table('watching',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#     db.Column('stock_ticker', db.String(5), primary_key=True),
#     db.Column('stock_name', db.String(64), nullable=False),
#     db.Column('date', db.Date(5), nullable=False),
# )

class Watching(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    stock_ticker = db.Column(db.String(5), primary_key=True)
    stock_name = db.Column(db.String(64), nullable=False)
    date = db.Column(db.DateTime, default=dt.datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<Watching {}>'.format(self.stock_ticker)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    favorite_stock = db.Column(db.String(5))
    state_code = db.Column(db.String(2))
    age = db.Column(db.Integer)
    watches = db.relationship('Watching', lazy='subquery',
        backref=db.backref('user', lazy=True))

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
