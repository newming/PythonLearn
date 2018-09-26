import MySQLdb

# 查询数据库内容
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

    def add_one(self):
        try:
            # 通过下边的方法，写成元组，分了多行，但是会拼成一行使用
            sql = (
                "INSERT INTO `news` (`title`, `content`, `created_at`, `types`, `image`, `author`) VALUE"
                "(%s, %s, %s, %s, %s, %s);"
            )
            cursor = self.conn.cursor()
            cursor.execute(sql, ('插入标题3', '插入的内容', '2018-09-26 22:20:33', '体育', 'www.newming.cn', 'newming123'))
            cursor.execute(sql, ('插入标题4', '插入的内容', '2018-09-26 22:20:33', '体育', 'www.newming.cn', 'newming123', '我是错误的数据', '会跑到 except 中，再次 commit ，正确的数据会保存上，我不会'))
            # 提交事物，修改数据库，可以将多次 execute 操作一起保存到数据库，如果不 commit ，execute 同样会生效，会有数据占到数据库中，但是查不到
            self.conn.commit()
            cursor.close()
        except:
            print('error')
            # self.conn.commit() # 如果不进行再次提交，多次 execute 的操作都不会保存
            self.conn.rollback() # 回滚，所有的 execute 都不生效
        self.close_conn()

def main():
    obj = MysqlSearch()
    # 获取单条数据
    # result = obj.get_one()
    # print(result)
    # 获取多条数据
    # result = obj.get_more()
    # for item in result:
    #     print(item)
    #     print('-----')
    # 插入一条数据
    obj.add_one()


if __name__ == '__main__':
    main()
