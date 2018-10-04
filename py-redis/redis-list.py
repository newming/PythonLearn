import redis

# 测试 list 相关的操作
class TestList(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def test_push(self):
        """
        lpush/rpush
        """
        t = ('newming', 'aaad')
        rest = self.r.lpush('l_eat', *t) # 通过 * 号解开
        print(rest)
        rest = self.r.lrange('l_eat', 0, -1)
        print(rest)

    def test_pop(self):
        rest = self.r.lpop('l_eat')
        print(rest)


def main():
    str_obj = TestList()
    # str_obj.test_push()
    str_obj.test_pop()

if __name__ == '__main__':
    main()
