class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person,my name is %s'%self.name

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender) # 初始化父类，否则，继承自 Person 的 Student 将没有 name 和 gender。
        self.score = score
    def whoAmI(self):
        return 'I am a Person,my name is %s'%self.name

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Person,my name is %s'%self.name

p = Person('Tom', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')
print(t.name)
print(t.course)
print(isinstance(p, Person))
print(isinstance(p, Student))
print(isinstance(p, Teacher))
print(isinstance(t, object))
print(type(s)) # get the var type
print(dir(s)) # get the var attr

getattr(s, 'name', 'not exit')
setattr(s, 'name', 'Adam') #set the new name
        
