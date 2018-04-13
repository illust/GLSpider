# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.project import get_project_settings
import json
import re


# 商品sku爬虫
class skuSpider(CrawlSpider):

    # 爬虫名称
    name = 'sku'

    # 导入设置参数
    settings = get_project_settings()
    allowed_domains = settings.get('ALLOWED_DOMAINS')
    start_urls = settings.get('START_URLS')
    allowRule = settings.get('ALLOWRULE')

    global skuXPath
    skuXPath = settings.get('SKUXPATH')

    global pageRule
    pageRule = ".*%s.+.html$"%settings.get('PAGERULE')

    # 链接提取规则
    rules = (
        Rule(LinkExtractor(allow=allowRule,), callback='parse_sku', follow=True),
    )

    # sku解析函数
    def parse_sku(self,response):

        #logger.info('this is information')

        # 通过正则获得sku页面，比如"epet.com"当中的item
        if re.compile(pageRule).match(response.url):

            
            # 构建item字典
            item = {}
            meta = {}
            docDict = {}
            docList = []
            
            
            docDict['collkey'] = response.url
            docDict['uri'] = response.url
            docDict['local'] = "true"

            for k in skuXPath.keys():
                try:
                    meta[k] = response.xpath(skuXPath[k]).extract_first().strip("\n").strip(" ")
                except:
                    pass
            docDict['meta'] = meta
            docList.append(docDict)

            item['collectionName'] = "sku"
            item['uid'] = "geelink"
            item['local'] = "false"
            item['docList'] = docList

            yield item

        else:
            pass