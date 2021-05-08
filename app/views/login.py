# -*- coding: utf-8 -*-

from app import engine, SITE_URL
from flask import render_template, request
from flask import redirect, url_for

@engine.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html", site_url=SITE_URL)

@engine.route("/admin/login", methods=['GET','POST'])
def admin_login():
    from .common import is_logged

    user = is_logged(request)
    if user is not None:
        return redirect(url_for(".dashboard"))

    if request.method == "POST":
        login = request.form.get("login","").strip()
        password = request.form.get("password","").strip()

        if (not login) and (not password):
            return redirect(url_for('.admin_login',msg=1))

        from .common import is_email
        from ..models.user import User

        code = 2
        if is_email(login):
            user = User.query.filter(User.email == login).first()
            code = 3
        else:
            user = User.query.filter(User.username == login).first()

        if not bool(user):
            return redirect(url_for(".admin_login", msg=code))

        if not user.check_password(password):
            return redirect(url_for(".admin_login", msg=4))

        if user.is_blocked():
            return redirect(url_for(".admin_login", msg=5))

        remember = request.form.get('remember','').strip()
        expiration = ''
        from flask import make_response
        from datetime import datetime

        resp = make_response(redirect(url_for('.dashboard')))
        if remember:
            expiration = "{}".format(int(datetime.timestamp(datetime.now())) + 3600 * 24 * 30 * 12)

        from .common import hash_mac

        _hdata = "{}|{}".format(user.username, expiration)
        _key = hash_mac(_hdata)
        _hash = hash_mac(_hdata, _key)
        _cookie = "{}|{}|{}".format(user.username, expiration, _hash)

        expired = None
        if expiration:
            expired = datetime.fromtimestamp(int(expiration))

        from app import AUTH_COOKIE_NAME
        resp.set_cookie(AUTH_COOKIE_NAME, _cookie, expires=expired)

        return resp

    args = None
    msg = request.args.get("msg","").strip()
    if msg:
        state = "error"
        if msg == "1":
            state = "warning"
            msg = "Please fill input"
        elif msg == "2":
            msg = "Username is not exists"
        elif msg == "3":
            msg = "Email is not exists"
        elif msg == "4":
            state = "warning"
            msg = "Password is not matched"
        elif msg == "5":
            msg = "Account is blocked"

        args = {
            "status": state,
            "msg": msg
        }

    lg = request.args.get("lg", "").strip()
    if lg:
        args = {
            "status":"success",
            "msg": "Your are logout"
        }

    return render_template("auth.html", site_url=SITE_URL, args=args)
