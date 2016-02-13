#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'starofrainnight'
SITENAME = 'StarOfRainNight\'s Home'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
THEME = "bootstrap2-dark"

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("My English Blog", "/eng"),
    ("My old Chinese Blog", "http://starofrainnight.blogspot.com"),
    ("My old English Blog", "http://starofrainnight-eng.blogspot.com"),)

# Social widget
SOCIAL = ()

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]

# Fixed tag could size great differences
TAG_CLOUD_STEPS = 1

DISQUS_SITENAME = "starofrainnightcht"

DEFAULT_PAGINATION = 10

DEFAULT_METADATA = {
    'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


