# -*- coding: utf-8 -*-

from app import engine, SITE_URL
from flask import render_template

@engine.route("/")
def homepage():
    return render_template("index.html", site_url=SITE_URL)
