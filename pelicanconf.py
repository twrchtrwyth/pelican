#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from bywyd import prif

AUTHOR = u'Wil Ifan'
SITENAME = u'The Library of Babel'
SITESUBTITLE = 'LEAGUES OF SENSELESS CACOPHONIES'
SITEURL = 'https://oki.nohost.me/babel'

STATIC_PATHS = ['images', 'extra']
#EXTRA_PATH_METADATA = {
#    'extra/favicon.ico': {'path': 'favicon.ico'},  # Haven't set this yet.
#}

# To publish an article, add Status: published to the metadata.
DEFAULT_METADATA = {
    'status': 'draft',
}

ABOUT = 'Rhydd i bawb ei farn, ac i bob barn ei llafar.'

# Extensions for Markdown. codehilite's 'linenums': 'True' causes all sorts of issues in code blocks.
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        # Add [TOC] to markdown file to generate contents
        'markdown.extensions.toc': {'toc_depth': 1, 'title': 'Contents'},
    },
    'output_format': 'html5',
}

# Defines where Pelican looks for its articles.
PATH = 'content'

FAVICON = "{{ PATH }}/extra/favicon.ico"

# The theme folder must be in Pelican's root folder (the same one as the content folder).
THEME = 'themes/simple'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_DATE_FORMAT = '%d/%m/%Y'

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

DEFAULT_PAGINATION = 0
SUMMARY_MAX_LENGTH = 20
SUMMARY_END_SUFFIX = "..."

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Enhanced typographical features, e.g. correctly formatted em-dashes.
TYPOGRIFY = True
TYPOGRIFY_DASHES = 'oldschool_inverted'

#MATH_JAX = {
#    "responsive": True,
#}

JINJA_FILTERS = {
    "bywyd": prif,
}

PHRASES = [  # For use in the `About` section of base.html
    'Rhydd i bawb ei farn, ac i bob barn ei llafar.',
    'The universe is trying to turn itself into iron.',
    'Ydy dy dŷ du di o dan dy dô du di?',
    'Cofiwch Dryweryn.',
    'The mediator between the head and the hands must be the heart.',
    'Gaga di bling blong. Gaga blung.',
    'Who called love conquering, when its sweet flower so easily dries among the sour lanes of the living?',
    'We are a way for the cosmos to know itself.',
]
