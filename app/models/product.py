# -*- coding: utf-8 -*-

from app import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    regular_price = db.Column(db.Integer)
    discounted_price = db.Column(db.Integer)

    def __init__(self):
        pass

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

    def __repr__(self):
        return "<Product#{} [{}] />".format(self.id, self.name)
