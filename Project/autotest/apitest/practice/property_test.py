class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property # get method
    def score(self):
        return self.__score
    @score.setter # set method 利用装饰器函数，把set 方法装饰成属性调用
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
s = Student('Bob', 59)
s.score = 60
print(s.score)