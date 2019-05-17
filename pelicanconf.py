#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'marco'
SITENAME = 'Memory Leak'
SITEURL = 'https://memoryleak.it/blog'
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'it'

PATH = 'content'
STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/cDc.ico': {'path': 'favicon.ico'},  # put favicon on site root
}


DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
    ('HOME', '/index.html'),
    ('ABOUT', '/pages/about.html'),
)

### Attenzione #####################
DELETE_OUTPUT_DIRECTORY = True
### Attenzione #####################

THEME='themes/aesop-rock'
PROFILE_IMAGE='mishima.jpg'  # used by Hyde theme

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
