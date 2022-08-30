# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


# 可以定义多个管道类,将数据保存到不同的地方
class LearnPipeline:
    fp = None

    # 重写父类方法,该方法只在开始爬虫时运行一次,打开要保存的文件
    def open_spider(self, spider):
        print('开始爬虫...')
        self.fp = open('learn1.txt', 'w', encoding='utf-8')

    # 用来处理item对象,将item中保存的数据进行持久化存储
    # 接受爬虫文件提交的item对象
    # 在配置文件中开启管道
    # 每当spider使用yield提交一次item,就会调用一次
    def process_item(self, item, spider):
        news = item['news']
        time = item['time']

        self.fp.write(news + ':' + time + '\n')
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
            self.cursor.execute('insert into learn1(news,time)values(%s,%s)', (item["news"], item["time"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

# 爬虫文件提交的item类型的对象会提交给优先级高的管道类,在优先级较高的管道类中return item会将item传递给下一个管道类
