
class Employee:
    total_employees = 0
    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

if __name__ == '__main__':
    emp1 = Employee('Mostafa')
    emp2 = Employee('Belal')

    emp1.total_employees = 10           # Re-bind
    print(emp1.total_employees)         # 10: refers to its attribute
    del emp1.total_employees
    print(emp1.total_employees)         # 3 now: I see shared static

    # del emp1.total_employees           # AttributeError
    del Employee.total_employees

    # print(emp1.total_employees)         # AttributeError
    # print(emp2.total_employees)         # AttributeError
    # print(Employee.total_employees)     # AttributeError

