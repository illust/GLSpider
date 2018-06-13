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
import sys


try:
    if sys.argv[1].startswith("--cmdfile="):
        try:
            with open(sys.argv[1].split("=")[1]) as f:
                settings = json.load(f)
        except json.JSONDecodeError:
            print("Configure Errors: some fields of the configure file expecting value!")
    elif sys.argv[1] == "-c":
        try:
            with open(sys.argv[2]) as f:
                settings = json.load(f)
        except json.JSONDecodeError:
            print("Some Errors: some fields of the configure file expecting value!")

except ValueError:
    print("Command Errors: input command is wrong!")


    
##############################################################
#************************用户设置参数部分*************************#

# 起始网址。必选项。
if 'START_URL' in settings:
    if settings['START_URL'] == "":
        raise ValueError("Can't find start url!")
    else:
        START_URLS = [settings['START_URL'],]
else:
    raise ValueError("Can't find START_URL field!")

# 站点限制，应该与起始网址的站点一致。必选项。
if 'ALLOWED_DOMAINS' in settings:
    if settings['ALLOWED_DOMAINS'] == "":
        raise ValueError("Can't find allowed domain!")
    else:
        ALLOWED_DOMAINS = [settings['ALLOWED_DOMAINS'],]
else:
    raise ValueError("Can't find ALLOWED_DOMAINS field!")


# 允许解析的页面，正则表达式形式，默认为空字符串。可选项。
if 'INCLUDE' in settings:
    INCLUDE = settings['INCLUDE']
else:
    INCLUDE = ".*"

# 拒绝解析的页面，正则表达式形式，默认为空字符串。可选项。
if 'EXCLUDE' in settings:
    EXCLUDE = settings['EXCLUDE']
else:
    EXCLUDE = ""

# 文件存储文件夹，默认为空字符串，即项目根目录。可选项。
if 'COLLECTION' in settings:
    COLLECTION = settings['COLLECTION']
else:
    COLLECTION = ""

# bdf格式文件名称，默认为'bdf'。可选项。
if 'FILENAME' in settings:
    if settings['FILENAME'] == "":
        raise ValueError("Can't find file name!")
    else:
        FILENAME = settings['FILENAME']
else:
    FILENAME = 'bdf'


# 抓取指定数量的Item之后终止爬虫，默认抓取数据量为100000。可选项。
if 'CLOSESPIDER_ITEMCOUNT' in settings:
    CLOSESPIDER_ITEMCOUNT = settings['CLOSESPIDER_ITEMCOUNT']
else:
    CLOSESPIDER_ITEMCOUNT = 100000


# 进行解析的url字段以及对应页面的解析xpath，若不存在该字段则报错。必选项。
if 'EXTRACTPATTERN' in settings:
    if settings['EXTRACTPATTERN'] == {}:
        raise ValueError("Can't find web page extract patterns!")
    else:
        EXTRACTPATTERN = settings['EXTRACTPATTERN']
else:
    raise ValueError("Can't find EXTRACTPATTERN field!")


# api上传秘钥。可选项。
if 't' in settings:
    T = settings['t']
else:
    T = ""

# 上传bdf开关
if 'BDFUPLOAD' in settings:
    BDFUPLOAD = settings['BDFUPLOAD']
else:
    BDFUPLOAD = "NO"


#*************************结束*******************************#
##############################################################

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'


# 是否遵循robots.txt，通常设为False，不遵守
ROBOTSTXT_OBEY = False


# 输出文件编码格式
FEED_EXPORT_ENCODING = 'utf-8'




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
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#   'GLSpider.middlewares.RandomProxyMiddleware':300,
#    'GLSpider.middlewares.RandomUserAgentMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'GLSpider.pipelines.JsonWriterPipeline': 200,
# }//it's setted in the skuSpider.py file

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
LOG_LEVEL = 'DEBUG'

# 禁止cookies
COOKIES_ENABLED = False

# 禁止重试
RETRY_ENABLED = False

# 减小下载超时
DOWNLOAD_TIMEOUT = 5

# 禁止重定向
REDIRECT_ENABLED = False


# 如果为 True，进程所有的标准输出(及错误)将会被重定向到log中。
# 例如，执行 print "hello" ，其将会在Scrapy log中显示
#LOG_STDOUT = True


LOG_SHORT_NAMES = True
LOG_FORMAT = '%(asctime)s [GLSpider] INFO: %(message)s'
