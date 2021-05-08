# -*- coding: utf-8 -*-

from app import engine, SITE_URL
from flask import render_template

@engine.route("/")
def homepage():
    from ..models.product import Product

    products = Product.query.all()

    from app import CART_COOKIE_NAME

    return render_template("index.html", site_url=SITE_URL, products=products, cookie_cart=CART_COOKIE_NAME)
