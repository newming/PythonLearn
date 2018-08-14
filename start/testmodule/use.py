# import module1
from module1 import a
import package

import package.test1 as test # 别名

from package.test2 import * # 导入全部变量

# print(module1.a)
print(a)
print(package.b)
print(test.a)

print(test2)
print(test22)
print(test222) # 报错，没有导出
