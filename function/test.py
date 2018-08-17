def add(a, b):
    return a + b


print(add(100, 45))


def mulreturn(a, b):
    return a + 10, b + 10


print(mulreturn(5, 8))

# 直接接收元组
val = mulreturn(20, 30)
print(val[0], val[1])

# 直接用两个变量接收返回值
val1, val2 = mulreturn(59, 102)
print(val1, val2)

# 序列解包(类似 js 中的解构赋值)

a, b, c = 1, 2, 3
print(a, b, c)

d = 1, 2, 3
print(d)  # tuple

e, f, g = [5, 6, 8]
print(e, f, g)
