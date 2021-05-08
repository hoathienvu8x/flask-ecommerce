# -*- coding: utf-8 -*-

from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    nickname = db.Column(db.String(126), index=True, nullable=False, default='')
    email = db.Column(db.String(126), index=True, nullable=False, default='')
    password = db.Column(db.String(128), nullable=False, default='')
    blocked = db.Column(db.String(1), nullable=False, default='n')
    role = db.Column(db.String(10), nullable=False, default='member')

    def __init__(self, username):
        self.username = username

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def remove(self):
        db.session.delete(self)
        db.session.commit()
        return self

    def update(self, **kwargs):
        fields = 0
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
                fields = fields + 1

        if fields > 0:
            db.session.commit()

        return self

    def set_password(self, password):
        from .password import hash_password
        self.password = hash_password(password)

    def check_password(self, password):
        from .password import verify_password
        return verify_password(self.password, password)

    def is_blocked(self):
        return self.blocked == "y"

    def __repr__(self):
        return "<User#{} [{}] />".format(self.id, self.nickname)
