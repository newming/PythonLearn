# pylint: skip-file
import re

s = 'sfds32'

# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
r = re.match('\d', s)
print(r)

# re.search 扫描整个字符串并返回第一个成功的匹配。
r1 = re.search('\d', s)
print(r1)
