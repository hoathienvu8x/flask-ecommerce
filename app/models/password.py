# -*- coding: utf-8 -*-

import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_password)
