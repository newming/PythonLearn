# 函数和模块的使用

"""

将 M 个苹果分成 N 组，每组至少一个苹果，一共有多少种方案
输入M和N计算C(M,N)
M! // N! // (M-N)!

"""

m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
  fm *= num
fn = 1
for num in range(1, n + 1):
  fn *= num
fmn = 1
for num in range(1, m - n + 1):
  fmn *= num
print(fm, fn, fmn)
print(fm // fn // fmn)

# 使用函数重构上面的代码，将求阶乘的抽象成一个方法
def factorial(num):
  result = 1
  for n in range(1, num + 1):
    result *= n
  return result

m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))

"""
默认参数
摇骰子，参数为骰子个数，求和
"""
from random import randint

def roll_dice(n=2):
  total = 0
  for _ in range(n):
    total += randint(1, 6)
  return total

roll_dice(3)

"""
可变参数
通过在参数前使用 * 号表示
"""

def add (*args):
  total = 0
  for val in args:
    total += val
  return total

print(add(1, 2, 3))

from module1 import test

print(test())

"""
python 中也是类似的函数作用域
因为 python 申明变量没有对应的关键字，所以在函数内部如果要修改全局作用域或者嵌套作用域的变量需要使用 `global` 与 `nonlocal` 的关键字
"""

valA = 100

def func():
  global valA
  print('func ====1', valA)
  valA = 200
  print('func ====', valA)

func()
print('global ====', valA)

def func1():
  valA = 500 # 这里会在函数内部申明新的 valA 变量
  print('func1 ====', valA)
  def bar():
    nonlocal valA
    print('bar ====', valA)
    valA = 1000
  bar()
  print('func1 ====2', valA)

func1()