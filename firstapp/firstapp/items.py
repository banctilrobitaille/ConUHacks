# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from IntelligentCellar.models import Bottle
from IntelligentCellar.models import Crawler

class BottleItems(DjangoItem):

    django_model = Bottle

class CrawlerItems(DjangoItem):

    django_model = Crawler