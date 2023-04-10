

class Person:
    def __init__(self, salary):
        self.salary = salary    # calls set

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            value = 0
        self.salary = value # calls salary.setter again for ever!

def f1():
    person = Person(100)
 #   print(person.salary)
   # person.salary = -200
   # print(person.salary)




if __name__ == '__main__':
    f1()