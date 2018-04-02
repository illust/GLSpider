# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import CloseSpider  
from GLSpider.items import html2FileItem

# 爬取html并保存到磁盘
class htm2fSpider(CrawlSpider):
    
    name = 'htm2f'
    custom_settings = {
        'ITEM_PIPELINES': {
            'GLSpider.pipelines.html2FilePipeline': 100,
            }
    }
    settings = get_project_settings()
    allowed_domains = settings.get('ALLOWED_DOMAINS')
    start_urls = settings.get('START_URLS')
    reRule = settings.get('RERULE')

    rules = (
        Rule(LinkExtractor(allow=reRule), callback='parse_item', follow=True),
    )

    def parse_item(self,response):

        item = html2FileItem()
        item['url'] = response.url
        item['title'] = response.xpath("//title").extract_first()
        item['html'] = response.body

        yield item
