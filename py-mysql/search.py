import MySQLdb


class MysqlSearch(object):
    def __init__(self):
        self.get_conn()

    def get_conn(self):
        # 创建连接
        try:
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='woaiwojia.',
                db='news',
                port=3306,
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print('Error" %s' % e)

    def close_conn(self):
        # 关闭连接
        if self.conn:
            self.conn.close()

    def get_one(self):
        # 准备 sql
        sql = 'SELECT * FROM `news` where `types` = %s;'
        # 找到 cursor
        cursor = self.conn.cursor()
        # 执行 sql
        cursor.execute(sql, ('热点', ))
        # print(dir(cursor)) # 所有 cursor 下的方法
        # print(cursor.description) # 拿到 cursor 的描述，元组
        # 拿到结果
        # result = cursor.fetchone() # 直接拿到的是元组
        result = dict(zip([k[0] for k in cursor.description], cursor.fetchone())) # 将拿到的元组处理成字典
        # 处理数据
        # print(result)
        # print(result['title'])
        # 关闭 cursor/连接
        cursor.close()
        self.close_conn()
        return result

    def get_more(self):
        sql = 'SELECT * FROM `news` where `types` = %s;'
        cursor = self.conn.cursor()
        cursor.execute(sql, ('热点', ))
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()] # 将拿到的元组处理成字典
        cursor.close()
        self.close_conn()
        return result


def main():
    obj = MysqlSearch()
    # result = obj.get_one()
    # print(result)
    result = obj.get_more()
    for item in result:
        print(item)
        print('-----')

if __name__ == '__main__':
    main()
