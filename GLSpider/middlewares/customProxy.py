# -*- coding: utf-8 -*-

from GLSpider.middlewares.resource import *
import random

class RandomProxyMiddleware(object):
    def process_request(self,request, spider):
        try:
            if request.url:
                request.meta['proxy'] = 'http://%s'% random.choice(PROXIES)
        except ValueError as error:
            logging.error("proxies is not useful")