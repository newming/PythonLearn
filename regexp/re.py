# pylint: skip-file
# http://www.runoob.com/python/python-reg-expressions.html
import re

a = 'C|C++|Java|C#|Python|Javascript'

# findall(reg, str, flags)
# flags -> xx | xx 这里 | 代表且
r = re.findall('Python', a, re.I | re.S)
print(r)    # ['Python']

b = 'jl6suer78slf'
# 找出 b 中的数字
s = re.findall('\d', b)    # \d 元字符
print(s)

w = re.findall('\D', b)
print(w)
