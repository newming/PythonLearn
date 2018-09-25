"""
使用 mysqlclient 连接 mysql 数据库
"""

import MySQLdb

# 创建连接
try:
	conn = MySQLdb.connect(
		host='127.0.0.1',
		user='root',
		passwd='woaiwojia.',
		db='news',
		port=3306,
		charset='utf8'
	)
	# 获取数据
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM `news`;')
	rest = cursor.fetchone()
	print(rest)

	# 关闭连接
	conn.close()
except MySQLdb.Error as e:
	print('Error" %s' % e)
