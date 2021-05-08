# -*- coding: utf-8 -*-

from app import engine, SITE_URL
from flask import make_response, redirect, url_for, request

@engine.route("/logout")
def logout():
    resp = make_response(redirect(url_for('.login',lg='true')))
    from .common import is_logged

    if is_logged(request):
        from app import AUTH_COOKIE_NAME
        resp.delete_cookie(AUTH_COOKIE_NAME)

    return resp

@engine.route('/admin/logout')
def admin_logout():
    resp = make_response(redirect(url_for('.admin_login',lg='true')))
    from .common import is_logged

    if is_logged(request):
        from app import AUTH_COOKIE_NAME
        resp.delete_cookie(AUTH_COOKIE_NAME)

    return resp
