
class FullName:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.middle_name = None
        self.last_name = last_name

class Employee:
    def __init__(self, first_name, last_name, salary, address):
        self.full_name = FullName(first_name, last_name)
        self.salary = salary
        self.address = address

    def print(self):
        print('Employee name:',
              self.full_name.first_name + " " + self.full_name.last_name)
        print('Employee salary:', self.salary)
        print('Employee address:', self.address)


mostafa = Employee('Ziad', 'Mostafa', 159, '55 BC')
mostafa.print()


"""
Employee name: Ziad Mostafa
Employee salary: 159
Employee address: 55 BC
"""
