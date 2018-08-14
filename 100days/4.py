# 用 for 循环实现 1~100 的求和

sum = 0
for x in range(101):
	sum += x
print(sum)


"""
1. `range(101)`可以产生一个0到100的整数序列。
2. `range(1, 100)`可以产生一个1到99的整数序列。
3. `range(1, 100, 2)`可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。
"""

"""

用for循环实现1~100之间的偶数求和

Version: 0.1
Author: newming
Date: 2018-07-19

"""

sum1 = 0
for x in range(2, 101, 2):
	sum1 += x
print(sum1)

sum2 = 0
for x in range(1, 101):
	if x % 2 == 0:
		sum2 += x
print(sum2)

"""

猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: newming
Date: 2018-07-19

"""

import random

answer = random.randint(1, 100)
counter = 0
while True:
	counter += 1
	number = int(input('请输入: '))
	if number < answer:
		print('大一点')
	elif number > answer:
		print('小一点')
	else:
		print('恭喜你猜对了!')
		break
print('你总共猜了%d次' % counter)
if counter > 7:
	print('你的智商余额明显不足')


"""

输出乘法口诀表(九九表)

Version: 0.1
Author: newming
Date: 2018-07-19

"""

for i in range(1, 10):
	for j in range(1, i + 1):
		print('%d*%d=%d' % (i, j, i * j), end='\t')
	print() # 换行

"""

输入一个正整数判断它是不是素数。先求平方根，然后计算从 2 到 平方根 之间有没有整除的就好了

Version: 0.1
Author: newming
Date: 2018-07-19

"""

from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num)) # int 向下取整，因为这里是从小的开始算，向下取整的话拿到的是最小的数，比如在加一的话，那它的最小的乘积出来为 它的平方，大于了原数，所以不需要加一
is_prime = True
for x in range(2, end + 1):
	if num % x == 0:
		is_prime = False
		break
if is_prime and num != 1:
	print('%d是素数' % num)
else:
	print('%d不是素数' % num)


"""

输入两个正整数计算最大公约数和最小公倍数。
从小的开始计算，递减小的。
最大公约数：能被两个数整除
最小公倍数：x * y / 最大公约数

Version: 0.1
Author: newming
Date: 2018-07-19

"""

x = int(input('x = '))
y = int(input('y = '))
if x > y:
	(x, y) = (y, x) # 交换顺序
for factor in range(x, 0, -1):
	if x % factor == 0 and y % factor == 0:
		print('%d和%d的最大公约数是%d' % (x, y, factor))
		print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
		break

"""

打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: newming
Date: 2018-07-19

"""

row = int(input('请输入行数: '))
# 利用两次循环，注意 加 一 的操作，一层循环控制行数，二层循环控制输出多个 *
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()
# 直接利用 str 乘法做
for i in range(row):
  print('*' * (i + 1))


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
