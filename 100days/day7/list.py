import sys

def main():
	list1 = [1, 3, 5, 7, 100]
	print(list1)
	list2 = ['hello'] * 5
	print(list2)
	# 计算列表长度(元素个数)
	print(len(list1))
	# 下标(索引)运算
	print(list1[0])
	print(list1[4])
	# print(list1[5])  # IndexError: list index out of range
	print(list1[-1])
	print(list1[-3])
	list1[2] = 300
	print(list1)
	# 添加元素
	list1.append(200)
	list1.insert(1, 400)
	list1 += [1000, 2000]
	print(list1)
	print(len(list1))
	# 删除元素，按元素匹配删除，不是下标
	list1.remove(3)
	if 1234 in list1:
		list1.remove(1234)
	# 按照下标删除
	del list1[0]
	print(list1)
	# 清空列表元素
	list1.clear()
	print(list1)

	# 切片操作
	fruits = ['grape', 'apple', 'strawberry', 'waxberry']
	fruits += ['pitaya', 'pear', 'mango']
	# 循环遍历列表元素
	for fruit in fruits:
		print(fruit.title(), end=' ')
	print(fruits)
	# 列表切片
	fruits2 = fruits[1:4]
	print(fruits2)
	# fruit3 = fruits  # 没有复制列表只创建了新的引用
	# 可以通过完整切片操作来复制列表
	fruits3 = fruits[:]
	print(fruits3)
	fruits4 = fruits[-3:-1]
	print(fruits4)
	# 可以通过反向切片操作来获得倒转后的列表的拷贝
	fruits5 = fruits[::-1]
	print(fruits5)

	# 排序操作
	list5 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
	list6 = sorted(list5)
	# sorted函数返回列表排序后的拷贝不会修改传入的列表
	# 函数的设计就应该像sorted函数一样尽可能不产生副作用
	list7 = sorted(list5, reverse=True)
	# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
	list8 = sorted(list5, key=len)
	print(list5)
	print(list6)
	print(list7)
	print(list8)
	# 给列表对象发出排序消息直接在列表对象上进行排序
	list5.sort(reverse=True)
	print(list5)

	# 创建列表
	f = [x for x in range(1, 10)]
	print(f)
	f = [x + y for x in 'ABCDE' for y in '1234567']
	print(f)
	# 用列表的生成表达式语法创建列表容器
	# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
	f = [x ** 2 for x in range(1, 100)]
	print(sys.getsizeof(f))  # 查看对象占用内存的字节数
	print(f)
	# 请注意下面的代码创建的不是一个列表而是一个生成器对象
	# 通过生成器可以获取到数据但它不占用额外的空间存储数据
	# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
	f = (x ** 2 for x in range(1, 100))
	print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
	print(f) # <generator object main.<locals>.<genexpr> at 0x110412390>
	for val in f:
		print(val)

# 除了上面提到的生成器语法，Python中还有另外一种定义生成器的方式，就是通过`yield`关键字将一个普通函数改造成生成器函数。下面的代码演示了如何实现一个生成[斐波拉切数列](https://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97)的生成器。所谓斐波拉切数列可以通过下面[递归](https://zh.wikipedia.org/wiki/%E9%80%92%E5%BD%92)的方法来进行定义：
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

if __name__ == '__main__':
	main()
	for val in fib(20):
	    print(val)
