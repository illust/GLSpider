# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field
import json
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Identity, Compose

class GlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class html2FileItem(Item):

	url = Field()
	title = Field()
	html = Field()


# class skuItem(Item):

# 	def __setitem__(self,key,value):
# 		self._values[key] = value
	
