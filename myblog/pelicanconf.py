#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yangxu'
SITENAME = u'杨旭的博客'
SITEURL = u'http://yangxu.in'
AUTHOR_EMAIL = u'yang.asahi@gmail.com'
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zhs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = u"yangmika"
THEME = u"pure"

PLUGIN_PATH = u"pelican-plugins"

PLUGINS = ["sitemap"]

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
}
}

# for "theme-svbhack" & "theme-pure"
TAGLINE = u'幸せだから笑うんじゃないよ。笑うから幸せになるんだよ。<br/>并不是因为幸福才笑，是因为笑了才幸福吧!'
