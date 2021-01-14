# -*- coding: utf-8 -*-

# Scrapy settings for quotesbot project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'quotesbot'

SPIDER_MODULES = ['quotesbot.douban']
NEWSPIDER_MODULE = 'quotesbot.douban'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Referer': 'https://m.douban.com/',
    'Cookie': 'bid=QngtB-xuAV4; douban-fav-remind=1; __utmv=30149280.6718; ll="108258"; _vwo_uuid_v2=DDEEC31D952FCAFB8A89674E32AB334AC|97e5d732130a9964c8fa0bcbdf5194dc; douban-profile-remind=1; gr_user_id=7d2ed445-faa2-4035-bb20-b253bb0a9c78; __gads=ID=d608b713eb6b1f00-22d4cfa2f7c400a3:T=1606792451:RT=1606792451:S=ALNI_MbI50H-Y9p_IFd-icHzs80IBDBFEQ; viewed="3082082"; __utmc=30149280; dbcl2="67181129:EvEBdBt2dYU"; ck=lvDn; push_doumail_num=0; frodotk="6eab907ee06e91ec4c02b17ca14bb5c4"; push_noty_num=0; __utmz=30149280.1610531251.30.18.utmcsr=movie.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/sugae/collect; __utma=30149280.1089770535.1599224554.1610531251.1610632133.31; __utmb=30149280.0.10.1610632133; ap_v=0,6.0; talionusr="eyJpZCI6ICI2NzE4MTEyOSIsICJuYW1lIjogIlx1Njc2OFx1NjAxZFx1NTJhMCJ9"; Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2=1610633742; _ga=GA1.2.1089770535.1599224554; _gid=GA1.2.1266975464.1610633744; Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2=1610634923'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'quotesbot.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'quotesbot.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'quotesbot.pipelines.SomePipeline': 300,
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

FEED_EXPORT_ENCODING = 'utf-8'