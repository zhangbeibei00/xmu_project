import scrapy
from Learn.items import LearnItem

class Learn1Spider(scrapy.Spider):
    name = 'learn1'
    allowed_domains = ['chinese.xmu.edu.cn']
    # 自动发送请求跟获取响应数据
    start_urls = ['http://chinese.xmu.edu.cn/']
    # 用parse方法进行数据解析

    # 基于终端指令进行持久化存储的代码
    # def parse(self, response):
    #     all_data=[]
    #     # 不用提取文本,直接使用xpath表达式
    #     div_list=response.xpath('//div[@class="container-fluid"]/div')
    #     # 对于其中的子div可以做局部数据解析
    #     print(div_list)
    #     for div in div_list:
    #
    #         # xpath返回的是列表,第一个列表元素就是Selector类型的对象,
    #         # 数据被保存在SElector对象的data里面,可以使用extract提取
    #
    #         news=div.xpath('./div[1]/a[1]/text()')[0].extract()#输出了一个字符串
    #         time=div.xpath('./div[2]/text()')[0].extract()
    #         # 假如提取的文本中包含<br>这样的,要使用
    #         # //text()提取,对应提取的列表有多个selector,
    #         # 此时使用selector会将列表中每一个selector中的data都提取出来,得到一个字符串列表
    #         # news=div.xpath('...//text()').extract()
    #         dic={
    #             'news':news,
    #             'time':time
    #         }
    #         all_data.append(dic)
    #     # 基于终端实现持久化存储,将解析的数据实现持久化储存
    #     # 只能持久化储存在json,jsonlines,jl,csv,xml,marshal,pickle这几种类型的文件中
    #     # 持久化储存指令:scrapy crawl xxx -o filePath
    #     return all_data


    # 基于管道进行持久化存储
    def parse(self, response):
            all_data=[]
            # 不用提取文本,直接使用xpath表达式
            div_list=response.xpath('//div[@class="container-fluid"]/div')
            # 对于其中的子div可以做局部数据解析
            print(div_list)
            for div in div_list:

                # xpath返回的是列表,第一个列表元素就是Selector类型的对象,
                # 数据被保存在SElector对象的data里面,可以使用extract提取

                news=div.xpath('./div[1]/a[1]/text()')[0].extract()#输出了一个字符串
                time=div.xpath('./div[2]/text()')[0].extract()
                item=LearnItem()
                item['news']=news
                item['time']=time
                # 将item提交给管道
                yield item


