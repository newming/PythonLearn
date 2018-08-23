# 闭包，和 js 类似
a = 10
def curve_pre():
    a = 25
    def curve(x):
        # print('this is a function')
        return a * x * x
    return curve

f = curve_pre()
print(f.__closure__)    # 闭包的环境变量 -> (<cell at 0x10646d9d8: int object at 0x1061fd320>,)
print(f.__closure__[0].cell_contents)    # 闭包的环境变量 -> 25

print(f(2))


def test():
    a = 20
    def test1():
        return 10
    return test1

t = test()
print(t.__closure__)    # None

'''
注意观察：
如果内部的函数没有引用父级函数内部的变脸，则不会形成 __closure__ 的闭包环境变量
'''
