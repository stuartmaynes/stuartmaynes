AUTHOR = "Stuart Maynes"
SITENAME = "Stuart Maynes"
SITEURL = "http://127.0.0.1:8000"
SITEDESC = "Software engineer."

PATH = "/Users/stuartmaynes/Library/Mobile Documents/iCloud~md~obsidian/Documents/Martin/Projects/Blog"
FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})\s(?P<title>.*)"

THEME = "../finley"

TIMEZONE = "Europe/London"

DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = "%B %d, %Y"
DEFAULT_LANG = "en"
LOCALE = "en_GB"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True
DIRECT_TEMPLATES = ["index", "archives"]

ARCHIVES_SAVE_AS = "articles/index.html"

ARTICLE_URL = "articles/{slug}/"
ARTICLE_SAVE_AS = "articles/{slug}/index.html"

AUTHOR_URL = "articles/{slug}/"
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

DRAFT_URL = "articles/drafts/{slug}/"
DRAFT_SAVE_AS = "articles/drafts/{slug}/index.html"

CATEGORY_URL = "articles/categories/{slug}/"
CATEGORY_SAVE_AS = "articles/categories/{slug}/index.html"
CATEGORIES_SAVE_AS = "articles/categories/index.html"

TAG_URL = "articles/tags/{slug}/"
TAG_SAVE_AS = "articles/tags/{slug}/index.html"
TAGS_SAVE_AS = "articles/tags/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

DRAFT_PAGE_URL = "drafts/{slug}/"
DRAFT_PAGE_SAVE_AS = "drafts/{slug}/index.html"

YEAR_ARCHIVE_SAVE_AS = "articles/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = ""

FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})\s(?P<title>.*)"

# Blogroll
HEADER_LINKS = ()

FOOTER_LINKS = (
    ("About", f"{SITEURL}/about/"),
    ("GitHub", "https://github.com/stuartmaynes"),
    ("Twitter", "https://twitter.com/stuartmaynes"),
    # ("Categories", f"{SITEURL}/articles/categories/"),
    # ("Tags", f"{SITEURL}/articles/tags/"),
    ("RSS", FEED_ALL_ATOM),
)

DEFAULT_PAGINATION = 24

DEFAULT_METADATA = {
    "status": "draft",
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {
            "footnotes": {},
        },
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {
            "anchorlink": "true",
            "anchorlink_class": "c-anchor",
        },
    },
    "output_format": "html5",
}

PYGMENTS_RST_OPTIONS = {"classprefix": "pgcss", "linenos": "table"}

TYPOGRIFY = True
