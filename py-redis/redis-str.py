import redis

# 测试字符串相关的操作
class TestString(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def test_set(self):
        rest = self.r.set('user1', 'newming')
        return rest

    def test_get(self):
        rest = self.r.get('user1')
        return rest

    def test_mset(self):
        """
        设置多个，用 dict 设置
        """
        d = {
            'user2': 'ddd',
            'user3': 'aaa'
        }
        rest = self.r.mset(d)
        return rest

    def test_mget(self):
        l = ['user1', 'user2', 'user3']
        rest = self.r.mget(l)
        return rest

    def test_del(self):
        return self.r.delete('user1')

def main():
    str_obj = TestString()
    # print(str_obj.test_set())
    # print(str_obj.test_get())
    # print(str_obj.test_mset())
    # print(str_obj.test_mget())
    print(str_obj.test_del())

if __name__ == '__main__':
    main()
