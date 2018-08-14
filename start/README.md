## 语法规范

- 语句结尾一般不加分号
- 变量名用下划线连接
- 通过缩进代表代码块，无法混淆压缩，缩进为四个空格
- 常量(表现意义上的常量，python没有常量)全部大写
- 文件开头编写 module 说明
- 冒号前不加空格
- 文件结尾增加一个空行

## 表达式

表达式(Expression)是运算符(operator)和操作数(operand)所构成的序列

运算优先级：

![image](优先级.jpg)

## 流程控制

- 条件控制
- 循环控制
- 分支

```python
# if else 判断逻辑
mood = 1

if mood == 1:
  print('go to 1')
elif mood == 2:
  print('go to 2')
else:
  print('go to right')

if pression:
  pass # 注意这里的 pass 是 python 的关键字，代表一个占位符，使这个语句不报错

# while 循环
n = 1
while n <= 10:
  print(n)
  n += 1
  # break
else:
  print('while done')

# for 循环。主要是用来遍历/循环 序列或者集合、字典
a = ['apple', 'huawei', 'mi']
for item in a:
  print(item)
  if item == 'huawei'
    break
    # continue
else:
  print('循环结束，一般都不用') # 如果 for 循环是通过 break 非正常结束，不会执行 else
```

## python 项目的组织结构

包 -> 模块 -> 类 -> 函数、变量

命名空间: package.module

- 包的名字就是文件夹的名字，需要包含 `__init__.py` 文件，__init__.py 可以作为一个模块(模块名直接为文件夹名)，也可以什么都不写，会自动执行
- 模块的名字就是文件名
- 包和模块不会重复导入
- 避免循环导入

```python
# 模块导入
import modulepath # import 后只能是模块名，不可以是模块下的某个变量
import modulepath as module

from module import a, def # 从 module 中导入 a 和某个函数
from module import a, b, \
  c, d # 引入多个变量换行
from module import (a, b,
  c) # 换行

from module import * # 这里可以在导入的模块中指定默认导出的东西 __all__ = ['a', 'b']
```
