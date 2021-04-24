from .db_session import db
import sqlalchemy as sa
from sqlalchemy import orm


class Admins(db):
    __tablename__ = 'Admins'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(64), unique=True)
    password_hash = sa.Column(sa.Integer, unique=True)


class Teams(db):
    __tablename__ = 'Teams'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(64), unique=True)
    points = sa.Column(sa.Integer, default=0)
    password_hash = sa.Column(sa.Integer, unique=True)
    open_tasks = sa.Column(sa.String, default=None)

    teams = sa.orm.relationship('User', lazy='dynamic', primaryjoin="Teams.id == User.team")


class User(db):
    __tablename__ = 'User'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(64), unique=True, index=True)

    team = sa.Column(sa.Integer, sa.ForeignKey('Teams.id'))


class Tasks(db):
    __tablename__ = 'tasks'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    body = sa.Column(sa.String, unique=True)
    test = sa.Column(sa.String, unique=True)
    max_price = sa.Column(sa.Integer)
