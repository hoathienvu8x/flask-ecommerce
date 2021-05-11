# -*- coding: utf-8 -*-

from app import engine, SITE_URL, CART_COOKIE_NAME
from flask import render_template, redirect, request, url_for
from .cart import get_cart

@engine.route("/checkout", methods=["GET","POST"])
def checkout_page():
    items = []
    cart_items = get_cart(request)
    if cart_items is None:
        return redirect(url_for(".homepage"))

    ids = []
    for id in cart_items:
        ids.append(int(id))

    if len(ids) > 0:
        from ..models.product import Product
        query = Product.query.filter(Product.id.in_(ids)).all()
        items = [{
            "id":v.id,
            "name":v.name,
            "slug":v.slug,
            "image":v.image,
            "price":v.regular_price,
            "discounted":v.discounted_price,
            "quantity": cart_items[str(v.id)] if str(v.id) in cart_items else 1
        } for v in query ]

    return render_template("checkout.html", site_url=SITE_URL,items=items)
