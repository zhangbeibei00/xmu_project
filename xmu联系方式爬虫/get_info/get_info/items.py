# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    personal_url = scrapy.Field()
    name = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    yuan = scrapy.Field()
    title = scrapy.Field()


class GetorgItem(scrapy.Item):
    org = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
