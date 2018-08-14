class Person():
  def __init__(self, name):
    self.name = name
    self.score = 0

  def marking(self, score):
    if score < 0:
      score = 0
    self.score = score
    print(self.score)

xiaoming = Person('xiaoming')
print(xiaoming.name)
xiaoming.marking(-50) # 通过对外暴露方法修改内部属性
xiaoming.score = -1 # 这个属性是 public 的，所以仍然可以在外部直接修改
