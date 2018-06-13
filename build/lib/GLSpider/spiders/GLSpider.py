# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.project import get_project_settings
import json
import re
import os


# GeeLink通用爬虫
class GLSpider(CrawlSpider):

    # 爬虫名称
    name = 'spider'

    # 导入设置参数
    settings = get_project_settings()

    # bdf处理方法
    bdfupload = settings.get("BDFUPLOAD")
    if bdfupload == 'YES':
        custom_settings = {
                'ITEM_PIPELINES': {
                        'GLSpider.pipelines.bdfUploaderPipeline': 100
                },
            }
    else:
        custom_settings = {
                'ITEM_PIPELINES': {
                        'GLSpider.pipelines.fileWriterPipeline': 100
                },
            }


    allowed_domains = settings.get('ALLOWED_DOMAINS')
    start_urls = settings.get('START_URLS')

    global extractPattern
    extractPattern = settings.get('EXTRACTPATTERN')

    global include
    include = settings.get('INCLUDE')
    global exclude
    exclude = settings.get('EXCLUDE')

    # 链接提取规则
    rules = (
        Rule(LinkExtractor(), callback='parse_sku', follow=True),
    )

    # sku解析函数
    def parse_sku(self,response):

        # 通过正则获得sku页面，比如"epet.com"网站当中的item字段
        if re.compile(include).match(response.url):
            # 过滤掉不需要解析的页面
            if exclude == "":
                # 构建item字典为BDF格式
                item = {}
                meta = {}
                
                item['collkey'] = "-".join(response.url.split('//')[1].split("/"))

                # 导入item信息作为BDF文件的元数据
                # 匹配需要抓取的正则模式
                urlRe = extractPattern[extractPattern['selOnePt']]['field']
                if re.compile(urlRe).match(response.url):
                    pt = extractPattern[extractPattern['selOnePt']]  # 去除用于匹配网页url的正则表达式域
                    for k in pt.keys():
                        if k == 'field':
                            pass
                        else:
                            try:
                                ret = response.xpath(pt[k]).extract_first()
                                if ret is None:
                                    meta[k] = ""
                                else:
                                    meta[k] = [ret.strip("\n").strip()]
                            except:
                                pass

                    item['meta'] = meta

                    yield item

                else:
                    pass
            elif not re.compile(exclude).match(response.url):
                # 构建item字典为BDF格式
                item = {}
                meta = {}

                item['collkey'] = "-".join(response.url.split('//')[1].split("/"))

                # 导入item信息作为BDF文件的元数据
                # 匹配需要抓取的正则模式
                urlRe = extractPattern[extractPattern['selOnePt']]['field']
                if re.compile(urlRe).match(response.url):
                    pt = extractPattern[extractPattern['selOnePt']]  # 去除用于匹配网页url的正则表达式域
                    for k in pt.keys():
                        if k == 'field':
                            pass
                        else:
                            try:
                                ret = response.xpath(pt[k]).extract_first()
                                if ret is None:
                                    meta[k] = ""
                                else:
                                    meta[k] = [ret.strip("\n").strip()]
                            except:
                                pass

                    item['meta'] = meta

                    yield item
            else:
                pass
        else:
            pass
