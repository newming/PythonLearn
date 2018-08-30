import time
# 利用可变参数实现多参数传递的 decorator
def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

# 调用，带多个参数
@decorator
def f2(text, num, bool):
    print(text)
    print(num)
    print(bool)

f2('1', 2, False)
