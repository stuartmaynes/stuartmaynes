#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Stuart Maynes'
SITENAME = 'Stuart Maynes'
SITEURL = 'http://127.0.0.1:8080'
SITE_DESC = "I'm a software engineer."

PATH = '/Users/stuartmaynes/Library/Mobile Documents/com~apple~CloudDocs/Stuart Maynes/Blog'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

THEME = './themes/finley'

# PATH = '/Users/stuartmaynes/Library/Mobile Documents/27N4MQEA55~pro~writer/Documents/Blog'

ARCHIVES_SAVE_AS = 'articles/index.html'

ARTICLE_URL = 'articles/{slug}/'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'

AUTHOR_URL = 'articles/{slug}/'
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

DRAFT_URL = 'articles/drafts/{slug}/'
DRAFT_SAVE_AS = 'articles/drafts/{slug}/index.html'

CATEGORY_URL = 'articles/categories/{slug}/'
CATEGORY_SAVE_AS = 'articles/categories/{slug}/index.html'
CATEGORIES_SAVE_AS = 'articles/categories/index.html'

TAG_URL = 'articles/tags/{slug}/'
TAG_SAVE_AS = 'articles/tags/{slug}/index.html'
TAGS_SAVE_AS = 'articles/tags/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DRAFT_PAGE_URL = 'drafts/{slug}/'
DRAFT_PAGE_SAVE_AS = 'drafts/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = ''


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
HEADER_LINKS = ()

FOOTER_LINKS = (
    ('About', f'{SITEURL}/about/'),
    ('Github', 'https://github.com/stuartmaynes'),
    ('Twitter', 'https://twitter.com/stuartmaynes'),
    # ('Categories', f'{SITEURL}/articles/categories/'),
    # ('Tags', f'{SITEURL}/articles/tags/'),
    ('RSS', FEED_ALL_ATOM),
)

DEFAULT_PAGINATION = 25

DEFAULT_METADATA = {
    'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {
            'footnotes': {},
        },
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'anchorlink': 'true',
            'anchorlink_class': 'c-anchor'
        },
    },
    'output_format': 'html5',
}

PYGMENTS_RST_OPTIONS = {
    'classprefix': 'pgcss',
    'linenos': 'table'
}

TYPOGRIFY = True

DEFAULT_DATE_FORMAT = '%B %d, %Y'

LOCALE = ('en_GB')

DEFAULT_DATE = 'fs'
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})\s(?P<title>.*)'
