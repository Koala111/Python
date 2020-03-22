class Person(object):
    address = 'Earth' 
    count = 0 # sum the object number
    def __init__(self, name, gender, score):
        Person.count = Person.count + 1
        self.name = name
        self._gender = gender
        # self.__birth = birth # var can not find in outside with '__'
        self.__score = score
        # '__xxx__' can be found in outside .its the 
        # for k, v in kw.iteritems():
        #   setattr(self, k, v)
    def get_grade(self):
        if self.__score >= 80:
            return 'A'
        if self.__score >=60:
            return 'B'
        return 'c'


Person.address = 'China'
Person.hobby = 'play'

tom = Person('TOM', 'Male',19)
jack = Person('JACK', 'Female', 19920321)
print(tom._gender)
# print(tom.__birth)
print(Person.address)
print(tom.address)
print(tom.hobby)
print(tom.get_grade())
'''
L1 = [p1, p2, p3]
L2 = sorted(L1, lambda p1, p2: cmp(p1.name, p2.name))

for i in range(3):
    print(L2[i].name)
'''