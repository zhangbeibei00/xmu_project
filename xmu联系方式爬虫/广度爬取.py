import requests
import re
# 保存链接的标题像是人的名字的页面
PATTERN_URl = "<a.*href=\"(https?://.*?)[\"|\'].*"

depthDict = {}

def getHtml(url):
    r=requests.get(url,verify=False)
    r.encoding=r.apparent_encoding#编码转换
    code=r.status_code
    depthDict[startUrl] = 0
    print(r.text)


if __name__ == '__main__':
    startUrl = 'https://chinese.xmu.edu.cn/szdw/jys/yyxjyyyyxjys.htm'
    #爬取页面设置有第0级
    getHtml(startUrl)
    depthDict[startUrl] = 0

