
class Employee:
    def __init__(self, name):
        self.name = name
        print(f'Init {self.name}')
        self.employees_names = []

    def __del__(self):
        # is called on object when
        # garbage collector destroys it
        print(f'Deleting {self.name}')
        # Don't provide unless very strong reasons


if __name__ == '__main__':
    m = Employee('Mostafa')
    b = Employee('Belal')
    z = Employee('Ziad')
