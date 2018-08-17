from people import People

# 继承
class Student(People):
    def __init__(self, school, name, age):
        self.school = school
        # People.__init__(self, name, age) # 初始化父类，注意第一个参数传递 self
        super(Student, self).__init__(name, age) # 同样是初始化父类

    def do_homework(self):
        print('english')

print(Student.sum) # 0 从父类继承过来的
student1 = Student('人民路小学', 'niuxuming', 24) # 需要传入参数， people 那边需要
print(student1.sum)
print(student1.name)
print(student1.age)
print(student1.school)
student1.get_name()
student1.do_homework()
