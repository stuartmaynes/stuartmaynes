#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Stuart Maynes'
SITENAME = 'Stuart Maynes'
SITEURL = 'https://stuartmaynes.com'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

THEME = './themes/finley'

ARTICLE_URL = 'articles/{slug}/'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'

CATEGORY_URL = 'articles/categories/{slug}/'
CATEGORY_SAVE_AS = 'articles/categories/{slug}/index.html'

TAG_URL = 'articles/tags/{slug}/'
TAG_SAVE_AS = 'articles/tags/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
            ('Home', '/'),
            ('About', '/about'),
            ('Twitter', 'https://twitter.com/mrmaynes'),
            ('Github', 'https://github.com/stuartmaynes'),
        )

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
