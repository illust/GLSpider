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

    global pageRule
    pageRule = settings.get('PAGERULE')
    # 链接提取规则
    rules = (
        Rule(LinkExtractor(allow=allowRule,), callback='parse_sku', follow=True),
    )

    # sku解析函数
    def parse_sku(self,response):
        # 通过正则获得sku页面，比如"epet.com"当中的item
        if re.compile(pageRule).match(response.url):
            
            # 打开解析规则文件
            with open("D:/Product/Code/Python/GLSpider/GLSpider/cfg.json",'r') as f:
                cfg_dict = json.load(f)[0]

            # 构建item字典
            item = {}
            item['url'] = response.url
            for k in cfg_dict.keys():
                try:
                    item[k] = response.xpath(cfg_dict[k]).extract_first().strip("\n").strip(" ")
                except:
                    pass
            yield item

        else:
            pass