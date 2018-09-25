"""
使用 mysqlclient 连接 mysql 数据库
"""

import MySQLdb

conn = MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    passwd='woaiwojia.',
    db='news',
    port=3306,
    charset='utf8'
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM `news`;')
rest = cursor.fetchone()
print(rest)