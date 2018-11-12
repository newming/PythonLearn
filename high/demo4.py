# map 类

list_x = [1, 2, 3, 4, 5, 6]


def square(x):
    print(x)
    return x * x


r = map(square, list_x)
print(r)  # <map object at 0x10cfa8e48>
print(list(r))  # [1, 4, 9, 16, 25, 36]

r1 = map(lambda x: x * x, list_x)
print(list(r1))

'''
map 函数

1. 第一个参数是一个函数，需要有返回值
2. 除了第一个参数为，其余的参数会作为第一个函数的参数依次传入
3. 第一个参数执行的次数，取决后后边的列表的最短的长度的一个
'''

list_y = [7, 8, 9, 10, 11]
r2 = map(lambda x, y: x + y, list_x, list_y)
print(list(r2))
