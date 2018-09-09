import time


def print_current_time(func):
	print(time.time())
	func()


def f1():
	print('this is a function')


print_current_time(f1)


# 类似闭包的装饰器
def decorator(func):
	def wrapper():
		print(time.time())
		func()

	return wrapper


def f2():
	print('i am another function')


# 使用装饰器（1）
f = decorator(f1)
f()


# 利用 @ 符号(语法糖)调用
@decorator
def f3():
	print('i am the true decorator')


f3()
