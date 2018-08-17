# pylint: skip-file
import re

# 正则分组
s = 'life is short, i use python'

r = re.search('life(.*)python', s)

print(r.group(0))
print(r.group(1))
