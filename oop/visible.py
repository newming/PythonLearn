class Person():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.__score = 100

    def marking(self, score):
        if score < 0:
            score = 0
        self.score = score
        print(self.score)
        print(self.__score)  # 我可以拿到私有变量 100

    def __marking(self):
        print('i am private')


xiaoming = Person('xiaoming')
print(xiaoming.name)
# print(xiaoming._Person__score) # 通过这种间接方式读取私有属性
# print(xiaoming.__score) # AttributeError: 'Person' object has no attribute '__score'
xiaoming.__score = 20000  # 私有属性不能访问，这里直接赋值实际上会给 xiaoming 这个对象新加 __score 这么个属性
# 这里就可以看到 __score 了 {'name': 'xiaoming', 'score': 0, '_Person__score': 100, '__score': 20000} ，其中私有变量 __score 在存储的过程中变为了 _Person__score
print(xiaoming.__dict__)
print(xiaoming.__score)  # 20000 这里拿到的是新加的属性
xiaoming.marking(-50)  # 通过对外暴露方法修改内部属性
# xiaoming.score = -1 # 这个属性是 公开(public) 的，所以仍然可以在外部直接修改
# # 当一个属性或者方法是通过 __ 开头，python 会认为这个属性或方法是私有的，不允许在外部调用，如果是类似 __init__ 在结尾加上 __ 则不会认为是私有
# xiaoming.__marking()

'''
总结：
成员可见性：python 的私有属性只是在保存的时候，将原有的私有属性名改为了 _ClassName__privateProto
'''
