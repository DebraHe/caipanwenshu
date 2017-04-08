# -*- coding: utf-8 -*-

# Scrapy settings for panjueshu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'panjueshu'

SPIDER_MODULES = ['panjueshu.spiders']
NEWSPIDER_MODULE = 'panjueshu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'panjueshu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
PROXIES = ['125.88.74.122:81',
               '183.95.80.165:8080',
               '59.37.160.57:8081',
               '124.133.230.254:80',
               '183.78.183.156:82',
               '124.88.67.83:843',
               '42.81.58.199:80',
               '124.88.67.9:80',
               '180.167.34.187:80',
               '183.78.183.156:82',
               '125.88.74.122:85',
               '124.88.67.22:83',
               '14.152.93.79:8080',
               '182.38.36.42:8998',
               '122.96.59.98:82',
               '117.95.19.112:8998',
               '14.127.200.59:8081',
               '221.3.6.2:8081',
               '182.112.128.115:80',
               '124.88.67.9:843',
               '171.8.79.143:8080',
               '180.136.83.16:8998',
               '220.174.236.211:80',
               '124.88.67.17:83',
               '42.81.58.199:80',
               '183.165.150.216:8998',
               '183.78.183.156:82',
               '218.26.227.108:80',
               '124.88.67.9:83',
               '175.30.124.128:80',
               '180.169.59.222:8080',
               '60.250.72.252:8080',
               '222.92.141.250:80',
               '202.107.222.50:80',
               '122.116.229.240:80',
               '112.11.126.198:80',
               '124.88.67.34:82',
               '220.174.236.211:80',
               '119.254.84.90:80',
               '118.122.250.109:80',
               '211.140.151.220:80',
               '118.99.178.21:8080',
               '222.169.193.162:8099',
               '111.207.231.14:8080',
               '112.11.126.202:80',
               '180.167.34.187:80',
               '120.132.6.206:80',
               '122.228.179.178:80',
               '218.4.101.130:83',
               '122.193.14.102:80',
               '111.12.96.188:80',
               '111.7.174.135:80',
               '101.204.163.82:8080',
               '58.52.201.119:8080',
               '183.95.80.165:8080',
               '124.234.157.250:80',
               '112.11.126.197:80',
               '111.206.163.235:80',
               '58.221.38.170:8080',
               '101.230.214.25:8080',
               '220.174.236.211:80',
               '183.78.183.156:82',
               '106.58.127.229:80',
               '112.11.126.202:8080',
               '61.135.217.3:80',
               '111.12.96.188:80',
               '119.254.84.90:80',
               '124.234.157.250:80',
               '112.11.126.204:8080',
               '222.92.141.250:80',
               '106.58.115.12:80',
               '112.11.126.198:8080',
               '60.250.72.252:8080',
               '218.104.148.157:8080',
               '122.229.17.128:80',
               '122.228.179.178:80',
               '202.107.222.50:80',
               '112.11.126.201:8080',
               '42.81.58.199:80',
               '118.99.178.21:8080',
               '14.152.93.79:8080',
               '61.191.41.130:80',
               '42.81.58.198:80',
               '222.73.27.178:80'
    ]
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
DOWNLOADER_MIDDLEWARES = {

    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,

    'panjueshu.middlewares.ProxyMiddleware': 100,

}

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
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'panjueshu.middlewares.PanjueshuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'panjueshu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'panjueshu.pipelines.PanjueshuPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

