#!/usr/bin/python3

from app import db, google_blueprint
from flask_login import current_user
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    picture = db.Column(db.String(250))

class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)

google_blueprint.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user)

class Categories(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable=False)

class Items(db.Model):
    __tablename__ = 'items'
    name = db.Column(db.String(80), nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(250))
    categories_id= db.Column(db.Integer, db.ForeignKey('categories.id'))
    categories = db.relationship(Categories)