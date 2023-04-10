

class Person:
    def __init__(self, salary):
        self.__salary = salary    # calls set

    @property
    def salary(self):
        return self.salary   # calls salary.getter again for ever!

    @salary.setter
    def salary(self, value):
        if value < 0:
            value = 0
        self.__salary = value #

def f1():
    person = Person(100)
    print(person.salary)
   # person.salary = -200
   # print(person.salary)




if __name__ == '__main__':
    f1()