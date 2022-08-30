import pymysql

con = pymysql.connect(host='localhost', user='root', password='123456', database='learnsql', port=3306)
print(con)
# 创建游标对象
cur = con.cursor()
# 修改sql
sql = 'update learn1 set time=%s where news=%s'
# 删除sql
deletesql = 'delete from learn1 where time=%s'

try:
    cur.execute(deletesql, ('unknown'))
    con.commit()
    print('修改成功')
except Exception as e:
    print(e)
    con.rollback()
    print('修改失败')
finally:
    con.close()
