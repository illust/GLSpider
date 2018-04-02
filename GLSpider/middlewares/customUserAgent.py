# -*- coding: utf-8 -*-

from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from GLSpider.middlewares.resource import USER_AGENT_LIST

import random

class RandomUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        request.headers.setdefault('User-Agent', ua)