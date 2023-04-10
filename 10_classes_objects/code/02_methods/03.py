

class Employee:
    name = None
    salary = None
    address = None

    def print(self):
        print('Employee name:', self.name)
        print('Employee salary:', self.salary)
        print('Employee address:', self.address)

    def read(self):
        self.name = input('Enter name: ')
        self.salary = float(input('Enter salary: '))
        self.address = input('Enter address: ')


mostafa = Employee()
mostafa.read()
mostafa.print()


"""
Enter name: Ziad Mostafa
Enter salary: 159
Enter address: 55 BC
Employee name: Ziad Mostafa
Employee salary: 159.0
Employee address: 55 BC
"""