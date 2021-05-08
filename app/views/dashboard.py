# -*- coding: utf-8 -*-

from app import engine, SITE_URL
from flask import render_template, request, url_for, redirect

@engine.route("/admin/")
def dashboard():
    from .common import is_logged
    user = is_logged(request)

    if user is None:
        return redirect(url_for('.admin_login',msg=1))

    return render_template("dashboard.html", site_url=SITE_URL)
