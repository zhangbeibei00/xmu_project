import pymysql
import numpy as np
import pandas as pd

con = pymysql.connect(host='localhost', user='root', password='123456', database='learnsql', port=3306)
print(con)
# 创建游标对象
cur = con.cursor()
org_url_list = []
sql = 'select*from org_url'
# 查询时间为2022-04-21的数据段
try:
    cur.execute(sql)
    #     处理结果集
    #     返回的是元组的元组
    # 假如使用fetchone是获取一条数据
    orgs = cur.fetchall()
    # print(orgs)
    #     遍历
    org_list = []
    count = 0
    for org in orgs:
        org_url = org[0]
        org_yuan = org[1]
        if (org_yuan in org_list) == False and 'xmu' in org_url:
            org_list.append(org_yuan)
            org_url_list.append(org_url)

            print(org_url)
        else:
            continue
    print(len(org_url_list))
    dataframe = pd.DataFrame({'urls': org_url_list})
    dataframe.to_csv("org_urls1.csv",index=False,sep=',')
except Exception as e:
    print(e)
    print('查询所有数据失败')
finally:
    con.close()
