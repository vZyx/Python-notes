
class Person:
    def __init__(self, full_name):
        # DRY Principle: DON'T repeat yourself!
        self.set_full_name(full_name)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    full_name = property(get_full_name)

def f1():
    person = Person('Mostafa Saad')
    # Now can see some attribute named full_name
    print(person.full_name)              # calls get
    #person.full_name = 'Hello world'    # no attribute 'set_full_name'

def f2():
    person = Person('Ziad Mostafa')
    print(person.full_name)


if __name__ == '__main__':
    f1()