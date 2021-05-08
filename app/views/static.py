# -*- coding: utf-8 -*-

from app import engine, IMAGE_FOLDER
from flask import send_from_directory

@engine.route('/images/<path:filename>')
def image_static(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@engine.route('/products/<path:filename>')
def product_image_static(filename):
    from app import UPLOAD_FOLDER
    return send_from_directory(UPLOAD_FOLDER, filename)

@engine.route('/thumbnail/<path:filename>')
def w500_image(filename):
    import os
    from app import THUMBNAIL_FOLDER, UPLOAD_FOLDER
    if os.path.isfile(THUMBNAIL_FOLDER + filename):
        return send_from_directory(THUMBNAIL_FOLDER, filename)

    filepath = UPLOAD_FOLDER + '/' + filename
    if os.path.isfile(filepath):
        try:
            from PIL import Image
            img = Image.open(filepath)
            width, height = img.size
            new_width = 500
            if width == new_width:
                return send_from_directory(filepath)

            percent = (new_width / width)
            new_height = (height * percent)

            _format = img.format
            _mimetype = img.get_format_mimetype()

            img = img.resize((new_width, int(new_height)), Image.ANTIALIAS)

            """
            if int(new_height) > 314:
                img = img.crop((0, 0, new_width, 314))
            """

            thumbpath = THUMBNAIL_FOLDER + '/' + filename

            os.makedirs(os.path.dirname(thumbpath), exist_ok=True)
            img.save(thumbpath, _format)

            return send_from_directory(THUMBNAIL_FOLDER , filename)
        except:
            from .errors import not_found
            return not_found(None)

    from .errors import not_found
    return not_found(None)
