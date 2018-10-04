import redis

# 测试 set 相关的操作
class TestSet(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def test_sadd(self):
        l = ['cat', 'dog']
        rest = self.r.sadd('zoo2', *l)
        print(rest)
        print(self.r.smembers('zoo2'))

    def test_srem(self):
        rest = self.r.srem('zoo2', 'dog')
        print(rest)
        print(self.r.smembers('zoo2'))


def main():
    str_obj = TestSet()
    # str_obj.test_sadd()
    str_obj.test_srem()

if __name__ == '__main__':
    main()
