# 面向对象

```python
class Person():
  eye = 2 # 类上的属性，类似 prototype 上
  mouse = 1
  # 自动执行，可以显式调用，但是尽量不要这么干。返回值只能为 None
  def __init__(self, name, age):
    print('我是构造函数，类似 constructor')
    self.name = name
    self.age = age
  # 方法必填 self 参数，注意 self 并不是关键字，所以叫 this 也无所谓，挂载到原型上的
  def print_file (self):
    print('name', self.name)

xiaoming = Person('newming', 24) # 实例化不需要 new
xiaoming.print_file()
```

<!-- 133 -->