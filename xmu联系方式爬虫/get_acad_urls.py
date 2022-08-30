import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas

orgs = []
weburls = []


# 获得网页源码
def find_website(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding  # 编码转换
    code = r.status_code
    print('code:', code)
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    links = soup.find_all('a')
    # 查找文本里包含字符串的
    # links=soup.find_all(text=re.compile('xum.edu.cn'))
    # 选取class属性是content的所有结点
    tags = soup.select('.content')
    # 嵌套选取content内容下a节点
    for tag in tags:
        aTags = tag.select('a')
        for aTag in aTags:
            orgs.append(aTag.get_text())
            weburls.append(aTag['href'])


urls = ['https://www.xmu.edu.cn/xbyx/zrkxxb.htm', 'https://www.xmu.edu.cn/xbyx/rwyysxb.htm'
    , 'https://www.xmu.edu.cn/xbyx/shkxxb.htm', 'https://www.xmu.edu.cn/xbyx/gcjsxb.htm'
    , 'https://www.xmu.edu.cn/xbyx/yxysmkxxb.htm', 'https://www.xmu.edu.cn/xbyx/dqkxyjsxb.htm']

for url in urls:
    find_website(url)

dataframe = pd.DataFrame({'orgs': orgs, 'urls': weburls})
dataframe.to_csv("academy_urls.csv", index=False, sep=',')
