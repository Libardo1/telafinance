# -*- coding: utf-8 -*-

AUTHOR = u''
SITENAME = u'Tela'
SITEURL = 'http://www.telafinance.com'
TIMEZONE = 'America/New_York'

PDF_GENERATOR = False

DIRECT_TEMPLATES = ('index', 'sitemap', 'table-of-contents', 'blog', 'all')

ARTICLE_SAVE_AS = 'blog/{slug}.html'

SITEMAP_SAVE_AS = 'sitemap.xml'

FEED_DOMAIN = 'http://www.telafinance.com'
FEED_RSS = 'feed'

BYLINE = '&copy; 2018. All Rights Reserved.'
LINKS = ()

MARKUP = ('rst', 'markdown',)

SOCIAL = (
    ('Email', 'mailto:contact@telafinance.com'),
)

PROJECTS = ()

JINJA_EXTENSIONS = (['jinja2.ext.autoescape',])

