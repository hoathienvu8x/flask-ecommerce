# -*- coding: utf-8 -*-

from app import engine, SITE_URL
from flask import render_template, make_response

@engine.errorhandler(404)
def not_found(err):
    return make_response(
        render_template(
            "error.html",
            title="Not Found",
            site_url=SITE_URL,
            msg="404 Not Found"
        ),
        404
    )

@engine.errorhandler(400)
def bad_request(err):
    return make_response(
        render_template(
            "error.html",
            title="Bad Request",
            site_url=SITE_URL,
            msg="400 Bad Requested"
        ),
        400
    )

@engine.errorhandler(500)
def server_error(err):
    return make_response(
        render_template(
            "error.html",
            title="Internal Server Error",
            site_url=SITE_URL,
            msg="500 Internal Server Error"
        ),
        500
    )

@engine.errorhandler(405)
def not_allowed(err):
    return make_response(
        render_template(
            "error.html",
            title="Method Not Allowed",
            site_url=SITE_URL,
            msg="405 Method Not Allowed"
        ),
        405
    )

@engine.errorhandler(403)
def forbidden(err):
    return make_response(
        render_template(
            "error.html",
            title="Forbidden",
            site_url=SITE_URL,
            msg="403 Forbidden"
        ),
        403
    )

