# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# 数据解析
# 在item中定义相关的属性
# 将解析出来的数据储存到item类型的对象
# 将item中的对象提交到管道进行持久化存储

import scrapy


class LearnItem(scrapy.Item):
    # define the fields for your item here like:
    news = scrapy.Field()
    time = scrapy.Field()
    # pass
