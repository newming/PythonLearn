origin = 0

def go(step):
    global origin
    new_pos = origin + step # 不加 global 时的报错： local variable 'origin' referenced before assignment
    origin = new_pos    # 这里需要注意，如果不加 global 上一步会报错，因为这里的 origin 会当作 go 函数内部的变量，未定义，增加 global 即可
    return new_pos

print(go(2))
print(go(3))
print(go(6))

# 使用闭包实现上面的功能
origin1 = 0

def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos   # 这里有上边相同的问题
        return new_pos
    return go

tourist = factory(origin1)
print(tourist(2))
print(origin1)
print(tourist.__closure__[0].cell_contents)
print(tourist(3))
print(origin1)
print(tourist.__closure__[0].cell_contents)
print(tourist(6))
print(origin1)
print(tourist.__closure__[0].cell_contents)