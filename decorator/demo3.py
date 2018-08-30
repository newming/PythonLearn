import time

# 关键字参数处理
def decorator1(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

# 调用，带多个参数
@decorator1
def f1(text, num, dd, **kw):
    print(text)
    print(num)
    print(dd)
    print(kw)

f1('1', 2, 'aaa', a=1, b=2, c='222')

@decorator1
def f2(a):
    print(a)

f2(666)
