# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import re

from scrapy.core.downloader.handlers.http11 import TunnelError
from scrapy.exceptions import IgnoreRequest
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
# 下载中间件
from twisted.internet.error import TCPTimedOutError, DNSLookupError
from twisted.web._newclient import ResponseNeverReceived


class WeburlDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    # 拦截请求
    # def process_request(self, request, spider):
    #     # Called for each request that goes through the downloader
    #     # middleware.
    #
    #     # Must either:
    #     # - return None: continue processing this request
    #     # - or return a Response object
    #     # - or return a Request object
    #     # - or raise IgnoreRequest: process_exception() methods of
    #     #   installed downloader middleware will be called
    #     return None
    # # 拦截响应
    # def process_response(self, request, response, spider):
    #     # Called with the response returned from the downloader.
    #
    #     # Must either;
    #     # - return a Response object
    #     # - return a Request object
    #     # - or raise IgnoreRequest
    #     return response
    # # 拦截异常的请求对象
    def process_exception(self, request, exception, spider):
        if isinstance(exception, (
        TimeoutError, TCPTimedOutError, ConnectionRefusedError, ResponseNeverReceived, TunnelError, DNSLookupError,
        FileNotFoundError)):  # 判断为那种异常类型
            raise IgnoreRequest('')
        return None
