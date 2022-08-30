import pymysql
import pandas as pd
import requests
import re

data = pd.read_csv(r'D:\project\python\test\academy_contact.csv')
sql_list = []
for row in data.itertuples():
    orgphone = []
    orgemail = []
    url = getattr(row, 'vaild_urls')
    org = getattr(row, 'vaild_orgs')
    phone = getattr(row, 'phone')
    print(phone)
    email = getattr(row, 'email')
    if email=='[]':
        email='none'
    if phone=='[]':
        phone='none'


    sql_list.append((org, email, phone))

print(sql_list)

con = pymysql.connect(host='localhost', user='root', password='123456', database='learnsql', port=3306)
print(con)
# 创建游标对象
cur = con.cursor()

sql = 'insert into org_url_detail(org,email,phone)values(%s,%s,%s)'

# 执行sql
try:
    # 插入一条数据
    for x in sql_list:
        try:
            cur.execute(sql,x)
        except:
            continue
    #     插入多条数据
    # cur.executemany(sql, sql_list)
    #     提交事务
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print("插入失败")

finally:
    con.close()
