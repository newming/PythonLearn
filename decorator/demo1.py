import time


# 装饰器
def decorator(func):
	def wrapper(arg):
		print(time.time())
		func(arg)

	return wrapper


# 调用，带一个参数
@decorator
def f1(text):
	print('i am the true decorator' + text)


f1('我是参数来的')
