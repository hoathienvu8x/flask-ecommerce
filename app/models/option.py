# -*- coding: utf-8 -*-

from app import db

class Option(db.Model):
    __tablename__ = "options"

    name = db.Column("option_name",db.String(64), index=True, unique=True, primary_key=True)
    value = db.Column("option_value",db.Text, nullable=True, default='')
    description = db.Column("option_desc",db.String(128), nullable=False, default='')

    def __init__(self, name):
        self.name = name

    def add(self):
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

    def __repr__(self):
        return '<Option {}>'.format(self.name)

