# python 函数

- 功能性
- 隐藏细节
- 避免编写重复的代码
- 组织代码

```python
help(print) # 查看某个函数的帮助文档
```

## 定义函数

注意，没有函数提升

```python
def funcname (parameter_list):
  pass
  # return value # 默认 return None
  # 返回多个值
  # return value1, value2, ... # 返回值为元组 tuple
```

函数参数：

- 必须参数，简称形参，调用时必须传递
- 关键字参数，调用函数时指定参数值，可以忽略函数参数定义顺序
- 默认参数，必须参数必须放到默认参数前，可以和关键字参数配合，但是要注意不能瞎混合着调用

```python
# 关键字参数
def add (x, y):
  return x + y

add(y=4, x=8)

# 默认参数
def add (x = 4, y = 3):
  return x + y
print(add(y=8))

def add2 (x, y, z):
  return x + y + z

print(add2(5, y=4, 8)) # 这样混合调用是不行的，即使你的顺序是相同的
```

设置最大递归次数：

```python
import sys

sys.setrecursionlimit(1000000) # 默认值在 995 左右
```

## 序列解包

> 注意两边的数量必须相等

```python
a, b, c = 1, 2, 3
# a: 1, b: 2, c: 3

d = 1, 2, 3
# d (1, 2, 3)

e, f, g = [1, 2, 3]
```

## 链式赋值

```python
a=b=c=1
```

## global 关键字

```py
a = 10
def func():
    a = 20  # 这里会把 a 当作 func 内部的变量使用

b = 30
def func1():
    global b
    b = 20  # 这里 b 会拿外部的变量
```

## nonlocal 关键字

```py
def func():
    a = 10
    def go():
        nonlocal a  # 指定 go 函数内部使用的 a 不是自己内部的，这样会向上找
        a = 20
    return go
```