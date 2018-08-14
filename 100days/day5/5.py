"""
总结和练习
"""

"""

求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

Version: 0.1
Author: newming
Date: 2018-07-20

"""

for x in range(0, 20):
	for y in range(0, 33):
		z = 100 - x - y
		if 5 * x + 3 * y + z / 3 == 100:
			print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

# 要理解程序背后的算法 - 穷举法


"""

Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: newming
Date: 2018-07-20

"""

from random import randint

money = 1000 # 初始玩家的金钱
# 最外层 while，当钱不够时停止
while money > 0:
	print('你的总资产为:', money)
	needs_go_on = False # 是否进行下一轮游戏，主要控制最后一个 while 的暂停
  # 用户下注输入检测，知道输入有效金额才开始下边的游戏
	while True:
		debt = int(input('请下注: '))
		if debt > 0 and debt <= money:
			break

  # 第一轮游戏，如果没有决出胜负，则 needs_go_on 进行下边的 while 循环
	first = randint(1, 6) + randint(1, 6)
	print('玩家摇出了%d点' % first)
	if first == 7 or first == 11:
		print('玩家胜!')
		money += debt
	elif first == 2 or first == 3 or first == 12:
		print('庄家胜!')
		money -= debt
	else:
		needs_go_on = True

  # 一直是玩家摇骰子，知道决出胜负，这一轮结束
	while needs_go_on:
		current = randint(1, 6) + randint(1, 6)
		print('玩家摇出了%d点' % current)
		if current == 7:
			print('庄家胜')
			money -= debt
			needs_go_on = False
		elif current == first:
			print('玩家胜')
			money += debt
			needs_go_on = False

print('你破产了, 游戏结束!')


"""

输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: newming
Date: 2018-07-20

"""

a = 0
b = 1
for _ in range(20):
	(a, b) = (b, a + b) # 卧槽
	print(a, end=' ')


"""

找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: newming
Date: 2018-07-20

"""

for num in range(100, 1000):
	low = num % 10
	mid = num // 10 % 10 # 这里找中位数的方式注意一下，先除以十取整，然后在除以十取余
	high = num // 100
	if num == low ** 3 + mid ** 3 + high ** 3:
		print(num)
