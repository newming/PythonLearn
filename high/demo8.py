# 列表推导式 [] 列表， set 集合， dict 都可以

a = [1, 2, 3, 4, 5]
d = {1, 2, 3, 4, 5}

# 在 for 循环前边添加对每个 项 要执行的操作
b = [i*i for i in a] # [1, 4, 9, 16, 25]

print(b)

# 在 for 循环后添加判断条件，先执行 for 然后 if 然后前边的操作
c = [i*i for i in a if i >= 3]
print(c) # [9, 16, 25]

# 还可以是 set
e = {i*i for i in d}
print(e)

# 而且还可以切换
f = {i*i for i in a}
print(f)

# 字典的列表推导
dict_source = {
    1: 'a',
    2: 'b'
}
print(dict_source.items()) # dict_items([(1, 'a'), (2, 'b')])
dict_list = [key for key,value in dict_source.items()]
print(dict_list) # [1, 2]

dict_dict = {value:key for key,value in dict_source.items()}
print(dict_dict) # {'a': 1, 'b': 2} key value 互换

# 元组，元组是不可变的，所以表现比较特殊
dict_tuple = (key for key,value in dict_source.items())
print(dict_tuple) # <generator object <genexpr> at 0x104cc1390> 返回的是一个 generator 对象
for x in dict_tuple:
    print(x)
