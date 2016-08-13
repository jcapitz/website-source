#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Juan Carlos Apitz'
SITENAME = u'Juan Carlos Apitz'
SITETITLE = u'Juan Carlos Apitz'
SITESUBTITLE = u'Statistician and Machine Learning Practitioner'
SITEURL = 'http://jcapitz.github.io'
SITELOGO = u'/images/drchivins_small.png'
BROWSER_COLOR = '#333'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Flex Theme settings
USE_FOLDER_AS_CATEGORY = True
ROBOTS = u'index, follow'
MAIN_MENU = True
#STATIC_PATHS = ['static']
#FAVICON = SITEURL + '/static/favicon.ico'
ROBOTS = 'index, follow'
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'))
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True

ADD_THIS_ID = 'ra-77hh6723hhjd'
#DISQUS_SITENAME = 'jcapitz'
GOOGLE_ANALYTICS = 'UA-1234-5678'
GOOGLE_TAG_MANAGER = 'GTM-ABCDEF'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = ((),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/jcapitz'),
          ('github','https://github.com/jcapitz'),
          ('envelope-o','mailto:jc@jcapitz.com'),)

DEFAULT_PAGINATION = 10

#THEME = "pelican-themes/pelican-bootstrap3"
THEME = "pelican-themes/Flex"

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['render_math','ipynb.markup']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
