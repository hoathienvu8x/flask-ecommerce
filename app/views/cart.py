# -*- coding: utf-8 -*-

from app import engine, SITE_URL, CART_COOKIE_NAME
from flask import render_template, redirect, url_for, request

def get_cart(req):
    cookies = req.cookies.get(CART_COOKIE_NAME)
    if not cookies:
        return None
    cart_items = {}
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

    return cart_items

def cart_item_cookie(items):
    vals = []
    for id in items:
        vals.append("{}:{}".format(id, items[id]))

    return ",".join(vals)

@engine.route("/cart", methods=['GET','POST'])
def cart_page():
    items = []
    cart_items = get_cart(request)
    if cart_items is not None:
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

    return render_template("cart.html", site_url=SITE_URL,items=items)

@engine.route("/addtocart",methods=['GET','POST'])
def addtocart():
    id = request.args.get("id", "0").strip()
    if not id:
        return redirect(url_for(".cart_page",add="invalid"))
    try:
        id = int(id)
    except:
        pass

    if id <= 0:
        return redirect(url_for(".cart_page",add="invalid"))

    cart_items = get_cart(request)
    if cart_items is None:
        cart_items = {}

    quantity = int(cart_items[str(id)]) if str(id) in cart_items else 0
    quantity = quantity + 1

    cart_items[str(id)] = "{}".format(quantity)

    cookie = cart_item_cookie(cart_items)
    
    print(cookie)
    
    from datetime import datetime
    from flask import make_response
    resp = make_response(redirect(url_for(".cart_page",add="done")))

    expiration = int(datetime.timestamp(datetime.now())) + 3600 * 24 * 30 * 12
    expired = datetime.fromtimestamp(int(expiration))

    resp.set_cookie(CART_COOKIE_NAME, cookie, expires=expired)

    return resp

@engine.route("/remove", methods=['GET','POST'])
def removeitem():
    return 'removed'
