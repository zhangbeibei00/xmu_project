import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from weburl.items import WeburlItem
import re
import pandas as pd
import numpy as np
import pickle


# 提取所有info网页的信息
# 'cpst.xmu.edu.cn', 'phys.xmu.edu.cn'
class XmuwebSpider(CrawlSpider):
    name = 'xmuweb'
    allow_domain = ['xmu.edu.cn']
    data_col = ['yuan', 'url']

    # (1)广度爬取全网五层的网页,教师信息延伸不超过五层
    # data1 = pd.read_csv(r'D:\project\python\test\vaild_academy_urls(2).csv', usecols=[0, 1], names=data_col)
    # print(data1['url'])
    # url_array = np.array(data1['url'])
    # url_list = url_array.tolist()[1:]
    # yuan_array = np.array(data1['yuan'])
    # yuan_list = yuan_array.tolist()[1:]
    # start_urls = url_list
    # allow_domain = url_list
    # key_list = [re.findall(r'\/\/[a-zA-Z0-9]+', url)[0][2:] for url in start_urls]
    # dict1 = dict(zip(key_list, yuan_list))
    # print(dict1)
    # # 保存为pickle字典
    # f_save = open('yuan_dict.pkl', 'wb')
    # pickle.dump(dict, f_save)
    # f_save.close()

    # 获取组织机构相关信息,找到一级域名,一般在一级域名里提取的联系方式一定是准确的,一级域名一般出现在首页,所以广度爬取的层数不用太高,3层即可
    # start_urls = ['https://www.xmu.edu.cn/']

    data_col = ['url']
    data1 = pd.read_csv(r'D:\project\python\test\Learn\Learn\org_urls.csv', usecols=[0], names=data_col)
    # print(data1['url'])
    data_array = np.array(data1['url'])
    data_list = data_array.tolist()
    start_urls = data_list
    allow_domain=start_urls
    link_list = LinkExtractor(allow=(allow_domain))
    # 多个ruler规则
    # follow 指定根据该规则提取的连接是否需要根据
    rules = (
        Rule(link_list, callback='parse_item', follow=True),
        # Rule(link_info_list, callback='parse_detail', follow=True),
    )

    # 这里必须手动写解析方法
    def parse_item(self, response):
        # (1)的解析方式
        # if 'info' in response.url:
        # item = WeburlItem()
        # print(response.url)
        # print(response.xpath('string(.)').extract_first())
        # item['url'] = response.url
        # yuan_pat = r'\/\/[a-zA-Z0-9]+'
        # yuan = re.findall(yuan_pat, response.url)
        # yuan_str = yuan[0][2:]
        # item['yuan'] = yuan_str
        # yield item

        # (2)的解析方式
        # url_str = response.url
        # count = url_str.count('/')
        # 满足一级域名的条件
        # if count <= 2 or (count == 3 and url_str[-1] == '/'):
        # print(url_str)
        item = WeburlItem()
        yuan_pat = r'\/\/[a-zA-Z0-9]+'
        yuan = re.findall(yuan_pat, response.url)
        yuan_str = yuan[0][2:]
        item['yuan'] = yuan_str
        item['url'] = response.url
        yield item
