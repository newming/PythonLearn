"""

找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: newming
Date: 2018-07-20

"""
import time
import math

start = time.clock()
for num in range(1, 10000):
	sum = 0
  # 从 1 开始进行穷举到 num 开方的位置，并且要包含这个位置，所以you 了加一的操作，range 的第二个参数是结束位子，但不包含该位，所以加一。比如 num 为 6 的时候，int(math.sqrt(6)) = 2，这里 2 是需要穷举的，所以加一后为 3， 1-3
	for factor in range(1, int(math.sqrt(num)) + 1):
		if num % factor == 0:
			sum += factor # 如果能够除尽就给 sum 就给 sum 加上
			if factor > 1 and num / factor != factor: # 同时要增加与他相乘的另一半，如果刚好是平方根或者 1，不需要加，例如 num = 6，factor 循环到 1 ，只需要加 1，循环到 2 需要增加 3
				sum += num / factor
  # 内部循环完毕，刚好判断完一个数是否为完美数
	if sum == num:
		print(num)

end = time.clock()
print("执行时间:", (end - start), "秒")

# 通过比较上面两种不同的解决方案的执行时间 意识到优化程序的重要性
