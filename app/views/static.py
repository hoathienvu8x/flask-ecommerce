# -*- coding: utf-8 -*-

from app import engine, IMAGE_FOLDER
from flask import send_from_directory

@engine.route('/images/<path:filename>')
def image_static(filename):
    return send_from_directory(IMAGE_FOLDER, filename)
