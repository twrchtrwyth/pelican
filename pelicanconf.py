#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Wil Ifan'
SITENAME = u'The Library of Babel'
SITESUBTITLE = 'Rhydd i bawb ei farn, ac i bob barn ei llafar.'
SITEURL = 'https://oki.nohost.me/babel'

STATIC_PATHS = ['images', 'extra',]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},  # Haven't set this yet.
}

# To publish an article, add Status: published to the metadata.
DEFAULT_METADATA = {
    'status': 'draft',
}

ABOUT = 'Leagues of senseless cacophonies'

# Extensions for Markdown. codehilite's 'linenums': 'True' causes all sorts of issues in code blocks.
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Defines where Pelican looks for its articles.
PATH = 'content'

# The theme folder must be in Pelican's root folder (the same one as the content folder).
THEME = 'future-imperfect'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Icon names (second item in tuple) use Font Awesome nomenclature.
CONTACTS = [
    ("Twitter", "twitter", "https://twitter.com"),
    ("Facebook", "facebook-f", "https://facebook.com"),
    ("Instagram", "instagram", "https://www.instagram.com"),
    ("Email", "envelope", "#"),
]

DEFAULT_PAGINATION = 3
SUMMARY_MAX_LENGTH = 20
SUMMARY_END_SUFFIX = "..."

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Enhanced typographical features, e.g. correctly formatted em-dashes.
TYPOGRIFY = True
TYPOGRIFY_DASHES = 'default'
