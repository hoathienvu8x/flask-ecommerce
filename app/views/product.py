# -*- coding: utf-8 -*-

from app import engine, SITE_URL, CART_COOKIE_NAME
from flask import render_template

@engine.route("/product/<string:name>/")
def detail_product(name=""):
    name = name.strip()
    if not name:
        from .errors import not_found
        return not_found(None)

    from ..models.product import Product

    product = Product.query.filter(Product.slug == name).first()
    if not bool(product):
        from .errors import not_found
        return not_found(None)

    product.description = product.description.strip()

    from app import db
    others = Product.query.filter(Product.id != product.id).order_by(db.func.random()).limit(5).all()

    return render_template('product.html', site_url=SITE_URL, product=product, others=others, cookie_cart=CART_COOKIE_NAME)
