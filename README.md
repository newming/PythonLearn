# Python

小楼昨夜又秋风

缺点：

- 慢。编译型语言(C, C++)、解释型语言(Javascript, Python)、Java 和 C# 属于中间类型。
- 运行效率与开发效率不可兼得


```bash
# mac 安装 python
# 安装 xcode
xcode-select --install
brew install python3 # 报错没有权限去 link
brew doctor # 给权限
brew link python # link
brew postinstall python3
```

## 什么是代码

代码是现实世界事物在计算机世界中的映射

## 什么是写代码

写代码是将现实世界中的事物用计算机语言来描述

## Python 的基本数据类型

type(param)

- 数字
  - int
  - float
  - bool
  - complex
- 组
  - 序列: str(不可变), list 列表, tuple 元组。有序，可用下标索引来访问，切片操作[0:5]
  - 集合 set: 无序，没有索引，不能切片
  - 字典 dict: key: value 键值对

### Number: int, float, bool 布尔类型, complex 复数(36j)

- 运算符： `/` 代表除法，但是会自动将结果转换为 float 类型，`//` 代表整除
- 进制表示：二(0b), 八(0o), 十六(0x)
- 转换为二进制：bin(num)
- 转换为八进制：oct(num)
- 转换为十进制：int(num)
- 转换为十六进制：hex(num)
- True, False: int(True) -> 1, bool(0) -> False
- False 的情况：0 '' [] {} None

### str 字符串: 单引号，双引号，三引号

- "let's go": 不需要转译哈
- "let\"s go": 转译
- 多行字符串：
  '''
  我是多行
  我是多行
  '''
  """
  我也是多行
  我也是多行
  """
- 转义字符：\n 换行 \r 回车
- r或R: 当一个字符串前面加上 r，他就不是一个普通字符串，而是原始字符串，r'hello\nworld' -> 'hello\\nworld'
- 字符串操作：'hello' + 'world', 'hello' * 3, 'hello'[0:4], 'hello'[-4] -> 'e', 'hello'[-4:] -> 'ello'

### 列表/组: [1, 2, 3, 4, 5]

```python
type([1, 2, 3])
# <class 'list'>
```

组的每一项可以是各种不同的类型

```python
[1, 2, 3][-1] -> 3 类似于字符串的操作
[1, 2, 3][1] -> 2 类似于字符串的操作

[2] + [3] -> [2, 3]
[2] * 3 -> [2, 2, 2]
```

### 元组(有序): (1, 2, 3)

```python
type((1, 2))
# <class 'tuple'>

type((1))
# <class 'int'> 只有一个元素的时候，() 解释为了数学的运算符号

(2) * 3 # 仍然解析为数学公式
# 6
(2, 2) * 3
# (2, 2, 2, 2, 2, 2)

(3, 2) + (5)
# 报错
(4, 5) + (6, 8)
# (4, 5, 6, 8)

# 所以如果声明只有一个元素的元组，要多加个逗号
(1,)
# 表示空的元组
()
```

序列: str list tuple

序列共有的操作：

- 通过下标获取 'hello'[2] -> l
- 切片 'hello'[2:4] -> 'll'
- 运算 +, *, in, not in : 3 in [3, 7] # True 这里要注意使用 in, not in 的时候，两边的数据类型相同
- 长度 len(): len('shj') -> 3
- max(), min(), ord('w') -> w 的 ascll 码值

### 集合 set

- 无序
- 不重复

```python
type({1, 2})
# <class 'set'>

{1, 2, 3, 2}
# {1, 2, 3}

len({2, 3, 4})
# 集合长度

1 in {1, 2, 3}
# True

2 not in {2, 3, 4}
# False

# - 减法操作: 求两个集合的差集
{1, 2, 3, 4, 5} - {3, 4}
# {1, 2, 5}

# & 交集
{1, 2, 3, 4, 5} & {3, 4, 8}
# {3, 4}

# | 并集
{1, 2, 3, 4, 5} | {3, 4, 8}
# {1, 2, 3, 4, 5, 8}

# 定义空的集合
type({}) # 错误 <class 'dict'>
type(set()) # 正确
```

### 字典

由多个 key value 组成的无序集合，key 值不重复，但是可以是不同数据类型，注意 key 值必须是不可变的类型(字符串，数组，元组，数字)，字符串需要加引号

```python
type({1:1, 2: '2'})
# <class 'dict'>

# 访问字典属性
{'name': 'newming'}[name]
```

## 变量

变量名 = 值

- 变量名可以是字母、数字、下划线的组合，但是不能以数字开头
- 系统关键字不能用在变量名中 and, if, import 等等
- 区分大小写
- 动态语言，没有类型限制，可覆盖
- 和 js 类似，同样分值类型(不可改变)(int, str, tuple)和引用类型(可以改变)(list, set, dict)，可以通过 id() 进行查看

```python
A = [1, 2, 3]
print(A)

a = 1
b = a
a = 2
print(b) # 1

a = [1, 2, 3]
b = a
a[0] = '1'
print(b) # ['1', 2, 3]

# 查看变量所在的内存地址
id(a)
```

## 运算符

### 算数运算符

- +
- -
- *
- /
- // 取整
- % 取余
- ** 平方 2**3 2的三次方

### 赋值运算符

- =
- +=
- -=
- *=
- /=
- %=
- **=
- //=

### 比较(关系)运算符：字符串，列表，元组都可以比较

- ==: 类似 js 的 ===
- !=
- >
- >=
- <
- <=

### 逻辑运算符: 操作与返回的都是布尔值

- and -> 类似 js 中的 &&，前边错返回前边的值，否则返回后边的值
- or -> 类似 js 中的 ||
- not -> 类似 js 中的 !

**返回 False 的情况：**

- 空字符串
- 0
- False
- 空列表 []
- 空 set: set()
- 空 tuple: ()
- 空 dict: {}

### 成员运算符：返回布尔值

- in: 对于字典的判断，判断的是 key 值
- not in

### 身份运算符：返回布尔值

不同于比较运算符 ==，比较运算符比较的是 值 是否相等。is 比较的是两个变量的身份(内存地址)是否相等

- is
- is not

```python
a = 1
b = 2
a is b
# False

a = 1
b = 1
a is b
# True

a = 1
b = 1.0
a == b # True
a is b # False

# ========== 注意注意
a = {1, 2, 3}
b = {1, 3, 2}
a == b # True 集合是无序的，所以值的顺序不影响值的比较
a is b # False 但是他们的内存地址不同

c = (1, 2, 3)
d = (2, 1, 3)
c == d # False 元组是有序的，所以顺序影响值的比较
c is d # False

e = {'name': 'newming', 'age': 24}
f = {'age': 24, 'name': 'newming'}
e == f # True 字典无序
e is f # False
```

类型判断：

```python
a = 'hello'
type(a) == int # False
type(a) == str # True

isinstance(a, str) # True

b = 1.3
isinstance(a, (str, int, float)) # 是不是后面类型中的一种
```

### 位运算符

把数字当作二进制数进行运算

- &: 按位与：转位二进制，每一位进行比较，如果两个位上都是 1，该位为 1，否则为 0
- |: 按位或：转位二进制，每一位进行比较，如果两个位上有一个为 1，该位为 1，否则为 0
- ^: 按位异或
- ~: 按位取反
- <<: 左移动
- >>: 右移动

- [README.md](./start/README.md)
- [README.md](./function/README.md)
- [README.md](./oop/README.md)