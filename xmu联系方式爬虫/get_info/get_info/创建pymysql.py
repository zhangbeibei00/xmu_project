# 不同老师的邮箱一定不会重复,拿邮箱当关键字
import pymysql

# 创建连接
con = pymysql.connect(host='localhost', user='root', password='123456', database='learnsql', port=3306)
print(con)
# 创建游标对象
cur = con.cursor()
# 编写创建表的sql
sql = """
    create table info_detail(
    name varchar(10),
    yuan varchar(50),
    title varchar(20),
    email varchar(50) primary key,
    phone varchar(20),
    personal_url varchar(200)
    
    )
"""

try:
    cur.execute(sql)
    print("创建表成功")
except Exception as e:
    print(e)
    print("创建表失败")

con.close()
