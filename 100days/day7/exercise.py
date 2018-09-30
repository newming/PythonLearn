"""
练习1：在屏幕上显示跑马灯文字
"""

import os
import time
import random

def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        # os.system('cls')
        os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""

def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        # print(_)
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

print(generate_code())


"""
练习3：设计一个函数返回给定文件名的后缀名。
"""

def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点

    :return: 文件的后缀名
    """
    pos = filename.rfind('.') # rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

print(get_suffix('aa.text'))

"""
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
"""

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


"""
练习5：计算指定的年月日是这一年的第几天
"""

def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份

    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0 # 这里注意 or 的优先级高于 and


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日

    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)] # 这里注意，通过 boolean 进行下标获取。False 为 0 True 为 1
    total = 0
    for index in range(month - 1):
        total += days_of_month[index] # 此时 total 为 传入 month 的前几个月的天数
    return total + date

print(which_day(1980, 11, 28))
print(which_day(1981, 12, 31))
print(which_day(2018, 1, 1))
print(which_day(2016, 3, 1))

"""
练习6：打印[杨辉三角](https://zh.wikipedia.org/wiki/%E6%9D%A8%E8%BE%89%E4%B8%89%E8%A7%92%E5%BD%A2)。
"""

def ShowYangHuiTriangle():
    num = int(input('Number of rows: '))
    yh = [[]] * num # list 直接做乘法运算
    # print(yh)
    for row in range(len(yh)):
        print(row)
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            # 如果是 当前行 的第一列(col) 或者最后一列，值为 1
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                # 否则等于(看图吧。。。) https://zh.wikipedia.org/wiki/File:PascalTriangleAnimated2.gif
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

ShowYangHuiTriangle()
