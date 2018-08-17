# pylint: skip-file
import re

a = 'abc, acc, adc, aec, afc, ahc, _+-*/'

# 找出 a 中单词中间字母为 c 或 f 的单词
r = re.findall('a[cf]c', a)
print(r)

s = re.findall('\w', a)     # \w 包含下划线，不含 + - * / & 等
print(s)
