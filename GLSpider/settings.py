# -*- coding: utf-8 -*-

# Scrapy settings for GLSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html


BOT_NAME = 'GLSpider'

SPIDER_MODULES = ['GLSpider.spiders']
NEWSPIDER_MODULE = 'GLSpider.spiders'

# 导入用户自定义设置
import json
with open('d:/settings.json') as f:
    settings = json.load(f)

##############################################################
#*****************用户自定义参数部分*************************#
# 站点限制
ALLOWED_DOMAINS = [settings['ALLOWED_DOMAINS'],]

# 起始网址
START_URLS = [settings['START_URLS'],]

# url页面解析规则
PAGERULE = settings['PAGERULE']

# html文件存储文件夹
FOLDER = settings['FOLDER']

# 抓取指定数量的Item之后终止爬虫
CLOSESPIDER_ITEMCOUNT = settings['CLOSESPIDER_ITEMCOUNT']

# 指定时间之后终止爬虫
#CLOSESPIDER_TIMEOUT = settings['CLOSESPIDER_TIMEOUT']

# 商品单品解析xpath
SKUXPATH = settings['SKUXPATH']
#*************************结束*******************************#
##############################################################

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'


# 是否遵循robots.txt，通常设为False，不遵守
ROBOTSTXT_OBEY = False


# 输出文件编码格式
FEED_EXPORT_ENCODING = 'utf-8'


# 自行选择输出item字段域field
#FEED_EXPORT_FIELDS = ['url','title','subtitle','price']


# Scrapy提前终止条件有以下四个可选参数：

# 1)收到指定数目的响应之后终止爬虫
# CLOSESPIDER_PAGECOUNT = 50

# 2)抓取指定数码的Item之后终止爬虫
# CLOSESPIDER_ITEMCOUNT = 200

# 3)指定时间之后终止爬虫
# CLOSESPIDER_TIMEOUT=100

# 4)发生指定数目错误之后终止爬虫
# CLOSESPIDER_ERROR=10



# 向下载器并发发出的请求数目，默认为16
CONCURRENT_REQUESTS = 100

# 广度优先遍历
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'GLSpider.middlewares.EpetSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'GLSpider.middlewares.customProxy.RandomProxyMiddleware':300,
#    'GLSpider.middlewares.customUserAgent.RandomUserAgentMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'GLSpider.pipelines.EpetPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



# 提高scrapy性能的一些设置

# 降低log级别
LOG_LEVEL = 'INFO'

# 禁止cookies
COOKIES_ENABLED = False

# 禁止重试
RETRY_ENABLED = False

# 减小下载超时
DOWNLOAD_ITMEOUT = 15

# 禁止重定向
#REDIRECT_ENABLED = False


# 如果为 True，进程所有的标准输出(及错误)将会被重定向到log中。
# 例如，执行 print "hello" ，其将会在Scrapy log中显示
#LOG_STDOUT = True