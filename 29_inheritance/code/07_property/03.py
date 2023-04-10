class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            value = 0
        self.__salary = value


class HourlyEmployee(Employee):
    extra = 100

    # Override property: get & set
    @property
    def salary(self):
        return self.__salary + HourlyEmployee.extra

    @salary.setter
    def salary(self, value):
        if value < 0:
            value = 0
        self.__salary = value

# depending on ur classes, you might have to do workarounds
# e.g. separate set function

if __name__ == '__main__':
    # inherits: init and properties
    emp = HourlyEmployee(20)
    print(emp.salary)
    emp.salary = -30
    print(emp.salary)
