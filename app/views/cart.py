# -*- coding: utf-8 -*-

from app import engine, SITE_URL, CART_COOKIE_NAME
from flask import render_template, redirect, url_for, request

@engine.route("/cart", methods=['GET','POST'])
def cart_page():
    items = []
    cookies = request.cookies.get(CART_COOKIE_NAME)
    if cookies:
        cart_items = {}
        ids = []
        a = cookies.strip().split(",")
        for i in range(len(a)):
            x = a[i].strip().split(":")
            if len(x) != 2:
                continue
            try:
                id = int(x[0])
            except:
                continue
            if id <= 0:
                continue
            cart_items[x[0]] = x[1]
            ids.append(id)

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
    return render_template("cart.html", site_url=SITE_URL,items=items)

@engine.route("/addtocart",methods=['GET','POST'])
def addtocart():
    return redirect(url_for(".cart_page",add="done"))
