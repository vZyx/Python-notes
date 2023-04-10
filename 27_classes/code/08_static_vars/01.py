

class Employee:
    total_employees = 0     # static var: shared

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

if __name__ == '__main__':
    emp1 = Employee('Mostafa')
    emp2 = Employee('Belal')
    emp3 = Employee('Ziad')

    print(emp1.total_employees)         # 3: instance can access static
    print(Employee.total_employees)     # 3
