def add (a, b):
  print(a)

add(b = 6, a = 8) # 关键字参数，可以忽略函数定义顺序

def add1 (x = 4, y = 3):
  return x + y
print(add1(y=8))


def add2 (x, y, z):
  return x + y + z

print(add2(5, y=4, 8)) # 这样混合调用是不行的，即使你的顺序是相同的
