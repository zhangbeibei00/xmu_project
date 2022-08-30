# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.core.downloader.handlers.http11 import TunnelError
from scrapy.exceptions import NotSupported, IgnoreRequest
from twisted.internet.error import TCPTimedOutError, DNSLookupError
from twisted.web._newclient import ResponseNeverReceived


class GetInfoDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        if isinstance(exception, (
        TimeoutError, TCPTimedOutError, ConnectionRefusedError, ResponseNeverReceived, TunnelError, DNSLookupError,
        FileNotFoundError,NotSupported)):  # 判断为那种异常类型
            raise IgnoreRequest('')
        return None
