import pymysql

# 创建连接
con = pymysql.connect(host='localhost', user='root', password='123456', database='learnsql', port=3306)
print(con)
# 创建游标对象
cur = con.cursor()
# 编写创建表的sql
sql = """
    create table org_url(
    url varchar(100) primary key,
    yuan varchar(20)
    )
"""

try:
    cur.execute(sql)
    print("创建表成功")
except Exception as e:
    print(e)
    print("创建表失败")

con.close()
