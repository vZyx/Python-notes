
class Employee:
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address

    def print(self):
        print('Employee name:', self.name)
        print('Employee salary:', self.salary)
        print('Employee address:', self.address)


mostafa = Employee('Ziad Mostafa', 159, '55 BC')
mostafa.print()


"""
Employee name: Ziad Mostafa
Employee salary: 159
Employee address: 55 BC
"""
