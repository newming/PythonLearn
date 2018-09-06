# None 空
# 不等于 空字符串 空列表 0 False

a = ''
b = False
c = []
d = 0
e = {}

print(a == None)
print(b == None)
print(c == None)
print(d == None)
print(e == None)

# 空的字典是 False
if e:
    print('e is True')

# 类型：也是自己独有的类型
print(type(None)) # <class 'NoneType'>

print(a is None) # False
print(None is None) # True
