#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ajit Singh'
SITENAME = 'ajit\'s blog'
SITEURL = 'http://localhost:8000'
SITETITLE = 'Ajit Singh'
SITELOGO = '//secure.gravatar.com/avatar/1afd86f3379c09df14ba60338d7ae4bf?s=120'
SITEDESCRIPTION = "Movies and code."
SITESUBTITLE = 'Software Developer'


BROSWER_COLOR = '#333'
ROBOTS = 'index, follow'

MAIN_MENU = True
HOME_HIDE_TAGS = True
USE_FOLDER_AS_CATEGORY = True

# Menu items, what you want to show
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)
DEFAULT_PAGINATION = 10

PATH = './content'
OUTPUTPATH = './output'
TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# read about this when you get time, idk what it is yet
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# site monitoring
STATUSCAKE = {
    'trackid': 'i1D5dfPPhZfz1hvBp6mH',
    'days': 7,
    'rumid': 6852,
    'design': 6,
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = 'Flex'

# Blogroll
LINKS = (('Portfolio', 'http://luhach.me'),
         )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/ajit_luhach'),
          ('github', 'https://github.com/ajitluhach'),
          ('linkedin', 'https://www.linkedin.com/in/ajitluhach/'),
          )


# Some of these options are unknown at this time, Read about them later

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']
# PLUGINS = ['extract_toc','render_math','disqus_static','better_figures_and_images']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
    }

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}


ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'  # year followerd by slug
ARTICLE_URL = '{date:%Y}/{slug}.html' # year followed by slug

STATIC_PATHS = [
    'images',
    'extra',
    'extra/robots.txt',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

USE_LESS = True
# save article as draft, default

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# For code block highlighting do this
# PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
