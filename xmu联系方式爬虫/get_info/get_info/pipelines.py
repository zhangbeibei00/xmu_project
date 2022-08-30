# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

# class GetInfoPipeline:
#     def process_item(self, item, spider):
#         return item


class GetInfoPipeline:
    fp = None

    # 重写父类方法,该方法只在开始爬虫时运行一次,打开要保存的文件
    def open_spider(self, spider):
        print('开始爬虫...')
        self.fp = open('org_detail.csv', 'w', encoding='utf-8')

    # 用来处理item对象,将item中保存的数据进行持久化存储
    # 接受爬虫文件提交的item对象
    # 在配置文件中开启管道
    # personal_url = scrapy.Field()
    #     name = scrapy.Field()
    #     phone = scrapy.Field()
    #     email = scrapy.Field()
    #     yuan = scrapy.Field()
    #     title = scrapy.Field()
    # 每当spider使用yield提交一次item,就会调用一次
    def process_item(self, item, spider):
        name = item['name']
        phone = item['phone']
        email = item['email']
        yuan = item['yuan']
        title = item['title']
        personal_url = item['personal_url']

        self.fp.write(name + ',' + yuan + ',' + title + ',' + email + ',' + phone + ',' + personal_url + '\n')
        # 这里的return item 会将这个优先级较高的管道类得到的item继续传递给下一个管道类
        return item

    def close_spider(self, spider):
        print('结束爬虫!')
        self.fp.close()


class mysqlPipeline(object):
    conn = None
    # 游标对象
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='localhost', user='root', password='123456', database='learnsql', port=3306,
                                    charset='utf8')
        print(self.conn)

    # 通过链接对象创建游标对象
    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(
                'insert into org_url_detail(name,yuan,title,email,phone,personal_url)values(%s,%s,%s,%s,%s,%s)',
                (item["name"], item["yuan"], item["title"], item["email"], item["phone"], item["personal_url"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

class GetInfo_org_Pipeline:
    fp = None

    # 重写父类方法,该方法只在开始爬虫时运行一次,打开要保存的文件
    def open_spider(self, spider):
        print('开始爬虫...')
        self.fp = open('org_detail(3).csv', 'w', encoding='utf-8')

    # 用来处理item对象,将item中保存的数据进行持久化存储
    # 接受爬虫文件提交的item对象
    # 在配置文件中开启管道
    # personal_url = scrapy.Field()
    #     name = scrapy.Field()
    #     phone = scrapy.Field()
    #     email = scrapy.Field()
    #     yuan = scrapy.Field()
    #     title = scrapy.Field()
    # 每当spider使用yield提交一次item,就会调用一次
    def process_item(self, item, spider):
        email = item['email']
        org = item['org']
        phone = item['phone']
        address = item['address']

        self.fp.write(org + ',' + email + ',' + phone + ',' + address+'\n')
        # 这里的return item 会将这个优先级较高的管道类得到的item继续传递给下一个管道类
        return item

    def close_spider(self, spider):
        print('结束爬虫!')
        self.fp.close()


class mysql_org_Pipeline(object):
    conn = None
    # 游标对象
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='localhost', user='root', password='123456', database='learnsql', port=3306,
                                    charset='utf8')
        print(self.conn)

    # 通过链接对象创建游标对象
    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(
                'insert into org_url_detail(org,email,phone,address)values(%s,%s,%s,%s)',
                (item["org"], item["email"], item["phone"], item["address"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
