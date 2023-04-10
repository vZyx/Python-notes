class Employee:
    def __init__(self, salary):
        # self here will refer to the child class! whch doesn't has set!
        self.salary = salary  # AttributeError: can't set attribute

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

    # Override property: get only
    @property
    def salary(self):
        return self.__salary + HourlyEmployee.extra


if __name__ == '__main__':
    # inherits: init and properties
    emp = HourlyEmployee(20)
    print(emp.salary)
    emp.salary = -30
    print(emp.salary)
