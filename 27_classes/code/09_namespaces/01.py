
class Employee:
    """Class Employee is TODO"""
    total_employees = 0
    def __init__(self, name):

        self.name = name
        Employee.total_employees += 1

    def print(self):
        pass

    @classmethod
    def our_f(cls):
        pass


if __name__ == '__main__':
    obj = Employee('Mostafa')
    print(obj.__dict__)
    # {'name': 'Mostafa'}

    print(Employee.__dict__)
    # '__doc__': 'Class Employee is TODO',
    # 'total_employees': 1,
    # '__init__': <function Employee.__init__>,
    # 'print': <function Employee.print>,
    # 'our_f': <classmethod object>
