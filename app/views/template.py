# -*- coding: utf-8 -*-

from app import engine
from flask import Markup
import markdown

@engine.template_filter('markdown')
def neomarkdown(markdown_content):
    # https://stackoverflow.com/a/53694635
    return Markup(markdown.markdown(markdown_content, extensions=['tables']))
