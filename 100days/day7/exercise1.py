"""
案例1：双色球选号
"""

from random import randrange, randint, sample
import os


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)] # 全部可选的号码
    selected_balls = []
    # 抽六个数
    for _ in range(6):
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index] # 每次抽一个号码，将可选号码中剔除这个值
    # 上面的for循环也可以写成下面这行代码
    # sample函数是random模块下的函数
    # selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


n = int(input('机选几注: '))
for _ in range(n):
    display(random_select())
"""
可以使用random模块的sample函数来实现从列表中选择不重复的n个元素。
"""


"""
综合案例2：[约瑟夫环问题](https://zh.wikipedia.org/wiki/%E7%BA%A6%E7%91%9F%E5%A4%AB%E6%96%AF%E9%97%AE%E9%A2%98)

《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

def main():
    persons = [True] * 30
    """
    persons 30个人，一上来都是 True 代表基督徒，不是的标为 False
    counter 非基督徒数量，0-14
    index 总人数下标 30
    number 报的数 1-9
    """
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')

# main()


"""
综合案例3：[井字棋](https://zh.wikipedia.org/wiki/%E4%BA%95%E5%AD%97%E6%A3%8B)游戏
"""


def print_board(board):
	print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
	print('-+-+-')
	print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
	print('-+-+-')
	print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def board():
	init_board = {
		'TL': ' ', 'TM': ' ', 'TR': ' ',
		'ML': ' ', 'MM': ' ', 'MR': ' ',
		'BL': ' ', 'BM': ' ', 'BR': ' '
	}
	begin = True
	while begin:
		curr_board = init_board.copy()
		begin = False
		turn = 'x'
		counter = 0
		os.system('clear')
		print_board(curr_board)
		while counter < 9:
			move = input('轮到%s走棋, 请输入位置: ' % turn)
			if curr_board[move] == ' ':
				counter += 1
				curr_board[move] = turn
				if turn == 'x':
					turn = 'o'
				else:
					turn = 'x'
			os.system('clear')
			print_board(curr_board)

		choice = input('再玩一局?(yes|no)')
		begin = choice == 'yes'

board()

"""
最后这个案例来自[《Python编程快速上手:让繁琐工作自动化》](https://item.jd.com/11943853.html)一书（这本书对有编程基础想迅速使用Python将日常工作自动化的人来说还是不错的教材），对代码做了一点点的调整。
"""