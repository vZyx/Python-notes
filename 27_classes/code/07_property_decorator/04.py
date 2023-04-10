

class Person:
    def __init__(self, salary):
        self.salary = salary    # Fixed

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            value = 0
        self.__salary = value

def f1():
    person = Person(100)
    print(person.salary)    # 100
    person.salary = -200
    print(person.salary)    # 0




if __name__ == '__main__':
    f1()