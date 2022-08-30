import scrapy
import jieba
import re
import pandas as pd
import csv
import sys
import numpy as np
from get_info.items import GetInfoItem, GetorgItem

# 将包含parent包的路径添加进系统路径
sys.path.append(r"D:\project\python\test\get_info\get_info\spiders")
import get_detail
import pickle


# 读取已经爬取的url列表,依次访问
class InfoSpider(scrapy.Spider):
    name = 'info'
    yuan = ''
    count = 0
    # allowed_domains = ['www.']
    # 依次访问所有的提取链接
    # 传输到数据库储存
    data_col = ['url']
    count = 0
    data1 = pd.read_csv(r'D:\project\python\test\weburl\org_url1.csv', usecols=[0], names=data_col)
    # print(data1['url'])
    data_array = np.array(data1['url'])
    data_list = data_array.tolist()
    start_urls = data_list

    # 加载院名索引字典
    # f_read = open(r'D:\project\python\test\get_info\get_info\spiders\dict_file.pkl', 'rb')
    # name_dict = pickle.load(f_read)
    # print(name_dict)
    # f_read.close()

    # 解析每个网页
    def parse(self, response):
        content = response.xpath('string(.)').extract_first()
        # print(content)
        # ans = get_detail.get_org_info(content)
        ans = get_detail.get_first_info(content)
        print(ans)
        print(response.url)
        # # 解析院wangye
        # if ans[0] != '' and ans[1] != '':
        #     item = GetorgItem()
        #     item['org'] = ans[0]
        #     item['email'] = ans[1]
        #     if (ans[1] == '' and ans[2] != ''):
        #         item['email'] = 'none' + str(self.count)
        #         self.count += 1
        #         print('*' * 30, item['email'])
        #     item['phone'] = ans[2]
        #     item['address'] = ans[3]
        #     yield item
        #
        # 解析老师的网页
        # 名字不为空
        if ans[0] != '':
            # print(ans)
            # ans=(名字,职称,电话,邮箱)
            url = response.url
            item = GetInfoItem()
            item["name"] = ans[0]
            item["title"] = ans[1]
            item["email"] = ans[3]
            item["phone"] = ans[2]
            item["personal_url"] = url
            # 获取院名
            yuan_pat = r'\/\/[a-zA-Z0-9]+'
            yuan = re.findall(yuan_pat, response.url)
            yuan_str = yuan[0][2:]
            # item['yuan'] = self.name_dict[yuan_str]
            item['yuan'] = yuan_str
            # print('(', item["name"], ' ', item["title"], ' ', item["email"], ' ', item["phone"], ' ', item['yuan'], ' ',
            #       item["personal_url"], ')')
            if item['email'] == '' and item['phone'] != '':
                item['email'] = 'none' + str(self.count)
                self.count += 1

            yield item
