

class Employee:
    name = None
    salary = None
    address = None


def print_empl(object):
    print('Employee name:', object.name)
    print('Employee salary:', object.salary)
    print('Employee address:', object.address)

def read_empl():
    obj = Employee()
    obj.name = input('Enter name: ')
    obj.salary = float(input('Enter salary: '))
    obj.address = input('Enter address: ')

    return obj

mostafa = read_empl()
print_empl(mostafa)

"""
Enter name: Ziad Mostafa
Enter salary: 159
Enter address: 55 BC
Employee name: Ziad Mostafa
Employee salary: 159.0
Employee address: 55 BC
"""