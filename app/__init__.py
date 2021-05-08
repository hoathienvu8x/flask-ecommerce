# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

engine = Flask("app")

engine.config["DEBUG"] = True

# Restfull response json configurations
engine.config["JSON_AS_ASCII"] = False
engine.config["JSONIFY_PRETTYPRINT_REGULAR"] = False

# Database configurations
engine.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(os.path.join(engine.root_path, "ecommerce.db"))
engine.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(engine)

# Login
AUTH_KEY = '#Im$nw#u=6eAU>qk6=lZJPa2T,n.~cu/soIF^3|?V4xCAzKjKL-<mA!H$1JD::i'
AUTH_COOKIE_NAME = 'm48CFwYC5e'

SITE_URL = ""
IMAGE_FOLDER = os.path.join(engine.root_path, "static", "images")

from .views import *
