""" for 循环 """

a = ['apple', 'huawei', 'mi']

for item in a:
  print(item, end=' ') # 打印到一行，增加 end = ' '
else:
  print('\n循环结束')

row = int(input('请输入行数： '))
for i in range(row):
  print('*' * (i + 1))

"""
1. `range(101)`可以产生一个0到100的整数序列。
2. `range(1, 100)`可以产生一个1到99的整数序列。
3. `range(1, 100, 2)`可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。
"""

"""
输出基数位的项
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 方法一，使用循环
for i in range(0, len(a), 2):
  print(a[i], end=' | ')

# 方法二，利用列表下标切片
b = a[0:len(a):2]
print(b)
