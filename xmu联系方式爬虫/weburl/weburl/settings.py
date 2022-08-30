# Scrapy settings for weburl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weburl'
SPIDER_MODULES = ['weburl.spiders']
NEWSPIDER_MODULE = 'weburl.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
# 改成不遵守ROBOT协议
ROBOTSTXT_OBEY = False
# 只输出错误的日志信息
LOG_LEVEL = 'ERROR'
# 设置最大爬取深度
DEPTH_LIMIT = 3
# 优先级为正数时,深度越大,优先级越低
DEPTH_PRIORITY = 1
# Obey robots.txt rules
ROBOTSTXT_OBEY = True
RETRY_ENABLED = False
SPIDER_MIDDLEWARES = {
   'weburl.middlewares.WeburlSpiderMiddleware': 543,
}
ITEM_PIPELINES = {
    'weburl.pipelines.WeburlPipeline': 300,
    'weburl.pipelines.mysqlPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
