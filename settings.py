# -*- coding: utf-8 -*-

AUTHOR = u''
SITENAME = u'Bankcasting'
SITEURL = 'http://www.bankcasting.com'
TIMEZONE = 'America/New_York'

PDF_GENERATOR = False

DIRECT_TEMPLATES = ('index', 'sitemap', 'table-of-contents', 'blog', 'all')

ARTICLE_SAVE_AS = 'blog/{slug}.html'

SITEMAP_SAVE_AS = 'sitemap.xml'

FEED_DOMAIN = 'http://www.bankcasting.com'
FEED_RSS = 'feed'

BYLINE = '&copy; 2016 Luke Makai. All Rights Reserved.'
LINKS = ()

MARKUP = ('rst', 'markdown',)

SOCIAL = (
    ('Email', 'mailto:pr@bankcasting.com'),
)

PROJECTS = ()

JINJA_EXTENSIONS = (['jinja2.ext.autoescape',])

