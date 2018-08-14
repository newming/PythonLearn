class Test():
	pass


test = Test()
if test:
	print('test is True')  # True


class Test1():
	def __len__(self):
		return 0


test1 = Test1()
if test1:
	print('test1 is True')  # False

print('各种假的情况')
print(bool(None))
print(bool([]))
print(bool(()))  # tuple
print(bool(''))
print(bool(0))
print(bool(False))
print(bool(set()))  # 空 set
print(bool({}))  # 空 dict
print(bool(test1))

'''
自定义对象不一定都是 True，有两个内置方法会对此有影响
当只有 __len__ 的时候，实例对象的真假由 __len__ 返回
当加入 __bool__ 的时候，bool() 值由 __bool__ 决定，不会执行 __len__ 方法了，而且 __bool__ 只能返回 True 和 False
'''


class Test2():
	def __len__(self):
		print('bool or len called')
		return 8  # 这里必须返回 int, True 或 False

	def __bool__(self):
		print('bool called')
		return False


test2 = Test2()
print(bool(test2))
print(len(test2))  # 8 如果 __len__ 返回 True 则 len() 为 1。注意如果没有 __len__ 的定义，是不能执行 len() 方法的
print(bool(test2))
