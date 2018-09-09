# 匿名函数


def add(x, y):
	return x + y


'''
匿名函数，类似与箭头函数
1. 没有名字
2. 不需要 return
3. 冒号后只能是表达式
'''


f = lambda x, y: x + y

print(f(1, 2))
