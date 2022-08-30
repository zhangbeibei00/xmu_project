import pandas as pd
import requests
import re
import pymysql


def get_acad_contact(csv_file):
    data = pd.read_csv(csv_file)
    pattphone = r'592-\d{7}|592.\d{7}'
    pattemail = r'[0-9a-zA-Z_]{1,19}@[0-9a-zA-Z]{1,13}\.[0-9a-zA-Z.]*'

    phone = []
    email = []
    for row in data.itertuples():
        orgphone = []
        orgemail = []
        url = getattr(row, 'vaild_urls')
        org = getattr(row, 'vaild_orgs')
        # 通过正则表达式获取这些页面上最直接的文本信息
        # 找到这些组织的联系方式,邮箱等
        print(url)
        url = str(url)
        r = requests.get(url)
        r.encoding = r.apparent_encoding  # 编码转换
        content = r.text
        it = re.finditer(pattphone, content)
        for match in it:
            orgphone.append(match.group())
        it = re.finditer(pattemail, content)
        for match in it:
            orgemail.append(match.group())
        phone.append(orgphone)
        email.append(orgemail)

    data['phone'] = phone
    data['email'] = email

    print(data)
    data.to_csv("academy_contact.csv", index=False, sep=',')

    con = pymysql.connect(host='localhost', user='root', password='123456', database='learnsql', port=3306)
    print(con)
    # 创建游标对象
    cur = con.cursor()

    sql = 'insert into org_url_detail(org,email,phone)values(%s,%s,%s)'

    # 执行sql
    try:
        # 插入一条数据
        # cur.execute(sql, ('这是一条新闻', '2022-3-4'))
        #     插入多条数据
        # cur.executemany(sql, [('新闻文本', '2022-3-5'), ('新闻文本2', '2022-3-6')])
        for i in range(0, len(phone)):
            t = (org[i], email[i], phone[i])
            cur.execute(sql, t)

        #     提交事务
        con.commit()
        print('插入成功')
    except Exception as e:
        print(e)
        con.rollback()
        print("插入失败")

    finally:
        con.close()


csvfile = 'vaild_academy_urls.csv'
get_acad_contact(csvfile)
