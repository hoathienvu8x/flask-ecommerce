# -*- coding: utf-8 -*-

from ..models.user import User
from ..models.option import Option

def init_database(db):
    db.drop_all()
    db.create_all()

    admin = User("admin")
    admin.nickname ="Administrator"
    admin.email = "admin@ecommerce.io"
    admin.blocked = "n"
    admin.role = "admin"
    admin.set_password("123456")

    admin.save()
