# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
import hashlib

class GlspiderPipeline(object):
    def process_item(self, item, spider):
        return item

import hashlib
class html2FilePipeline(object):
    def process_item(self, item, spider):
        settings = get_project_settings()
        folder = settings.get('FOLDER')
        file_name = hashlib.sha224(item['url'].encode('utf-8')).hexdigest() #chose whatever hashing func works for you
        with open('%s/%s.html' % (folder,file_name), 'w+b') as f:
            f.write(item['html'])

class skuItemPipeline(object):
	def process_item(self,item,sku):
		return item

