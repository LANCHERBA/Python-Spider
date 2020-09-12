"""
    使用pymysql模块在mytab表中插入一条表记录。
"""

import pymysql

# 1. 创建数据库连接对象
db = pymysql.connect(
    'localhost',
    'root',
    '123456',
    'mydb',
    charset='utf8'
)
# 2. 创建游标对象
cur = db.cursor()
# 3. 执行SQL命令
ins = 'insert into mytab values(%s,%s,%s)'
li = ['大话西游', '周星驰', '1994-01-01']
cur.execute(ins, li)
# 4. 提交到数据库执行
db.commit()
# 5. 关闭游标
cur.close()
# 6. 断开数据库连接
db.close()
