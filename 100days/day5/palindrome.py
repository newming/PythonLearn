"""

判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

这个在 js 算法那实现的方式是利用双向队列，每次取出头尾比较，这种方式感觉更好

Version: 0.1
Author: newming
Date: 2018-07-20

"""

num = int(input('请输入一个正整数: '))
temp = num
num2 = 0
# while 循环做的是将原数字倒过来
while temp > 0:
	num2 *= 10
	num2 += temp % 10
	temp //= 10
# 那倒过来的数和原数字比较
if num == num2:
	print('%d是回文数' % num)
else:
	print('%d不是回文数' % num)
