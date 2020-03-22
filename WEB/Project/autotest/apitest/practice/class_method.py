class Person(object):
    __count = 0
    @classmethod # 类方法无法获得任何实例变量，只能获得类的引用。
    def how_many(cls):
        return cls.__count
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1

print(Person.how_many())
p1 = Person('Bob')
print(Person.how_many())
