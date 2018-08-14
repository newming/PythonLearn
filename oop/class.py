class Person():
  name = '我是原型上的属性 name' # 类上的属性，类似 prototype
  age = 0
  sum1 = 0
  people = 0
  def __init__(self, name, age):
    # 构造函数，初始化属性，挂载到实例化对象上的属性
    self.name = name
    self.age = age
    print('init', self.sum1, Person.sum1) # 1====> init 0 0
    self.__class__.sum1 += 1
    print('当前实例化次数为', self.__class__.sum1) # 2=====> 拿到类方法上的属性 当前实例化次数为 1
  def print_file(self):
    print('name: ', self.name, self.sum1)
    print(self.__class__.sum1) # __class__ 拿到的是类变量，就是原型上的属性和方法

  # 装饰器，类方法
  @classmethod
  def say(cls):
    # 类方法同样需要一个默认参数，是这个类，无法获取实例上的属性
    cls.people += 1
    print('people can say', cls.people)

  # 静态方法，没有必须传入的参数。对象和类都可以调用，也可以拿到类属性，无法获取实例上的属性
  @staticmethod
  def add(x, y):
    print(x + y)
    print(Person.people)

xiaoming = Person('xiaoming', 33)
Person.say() # 调用类方法 3=====> people can say 1
xiaoming.print_file()
print(xiaoming) # <__main__.Person object at 0x10d49cda0>
print(xiaoming.name)
print(xiaoming.__dict__) # {'name': 'newming', 'age': 33} __dict__ 查找对象实例上的属性变量，字典

print(Person.name)
print(Person.__dict__) # {'__module__': '__main__', 'name': '我是原型上的属性 name', 'age': 0, '__init__': <function Person.__init__ at 0x10d6a3c80>, 'print_file': <function Person.print_file at 0x10d6a3bf8>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
# print(type(Person)) # <class 'type'>


newming = Person('newming', 24)
newming.say() # 对象竟然也可以调用 类 方法，不过类方法内部拿不到实例对象上的属性，不建议这么用
Person.say() # 调用类方法

newming.add(5, 8)
Person.add(8, 6)
