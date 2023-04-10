
class Person:
    __slots__ = ['name', 'email']
    def __init__(self, name, email):
        self.name = name
        self.email = email

#Person('mostafa', 'm@g').__dict__ # Error

class Student(Person):
    def __init__(self, name, email, gpa):
        Person.__init__(self, name, email)
        print(self.__dict__)   # {}
        self.gpa = gpa
        # Will use the parents slots + dict by default

st = Student('mostafa', 'm@g', 3.7)
print(st.__dict__)   # {'gpa': 3.7}