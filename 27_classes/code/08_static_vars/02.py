

class Employee:
    total_employees = 0
    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

if __name__ == '__main__':
    emp1 = Employee('Mostafa')
    emp2 = Employee('Belal')

    emp1.total_employees = 10           # Re-bind  : this is now your own attribute! Be careful
    print(emp1.total_employees)         # 10: refers to its attribute
    print(emp2.total_employees)         # 3: shared static
    print(Employee.total_employees)     # 3
