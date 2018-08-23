from enum import Enum

'''
枚举与普通对象或字典的区别：

1. 枚举的值不可以重复，如果重复了，后面的就是前边的别名
2. 不可以随意更改
3. 枚举的属性名不可以重复
'''

class VIP(Enum):
    YELLOW = 1
    GREEN = 1
    BLACK = 2

print(VIP.YELLOW)   # VIP.YELLOW
print(VIP.GREEN)    # VIP.YELLOW

# 不可以修改值
# VIP.YELLOW = 2  # AttributeError: Cannot reassign members.

# 获取某个属性的值
print(VIP.YELLOW.value)

# 获取属性名
print(type(VIP.YELLOW))    # <enum 'VIP'> 是个枚举的类
print(VIP.YELLOW.name, type(VIP.YELLOW.name))  # YELLOW <class 'str'> 是个字符串

# 遍历
for v in VIP:
    print(v)    # VIP.YELLOW VIP.BLACK 注意 green 彻底没什么事了

for v in VIP.__members__:
    print(v)    # 可以访问到 green 这样的 别名

for v in VIP.__members__.items():
    print(v)    # 得到的是元组
    # ('YELLOW', <VIP.YELLOW: 1>)
    # ('GREEN', <VIP.YELLOW: 1>)
    # ('BLACK', <VIP.BLACK: 2>)

# 比较
print(VIP.YELLOW == 1)  # False
print(VIP.YELLOW == VIP.YELLOW) # True
# print(VIP.YELLOW < VIP.BLACK)   # 枚举不支持大小比较 TypeError: '<' not supported between instances of 'VIP' and 'VIP'
print(VIP.YELLOW is VIP.YELLOW) # True

class VIP1(Enum):
    YELLOW = 1

print(VIP.YELLOW == VIP1.YELLOW)    # False

# 将数字类型转换为枚举类型
a = 1
print(VIP(a))   # VIP.YELLOW