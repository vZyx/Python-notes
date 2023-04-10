

class Person:
    def __init__(self, full_name):
        # DRY Principle: DON'T repeat yourself!
        self.set_full_name(full_name)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def set_full_name(self, full_name):
        self.first_name, self.last_name = full_name.lower().split()

    # Create property object
    # On class level. No self.
    full_name = property(get_full_name, set_full_name)  # NOT set_full_name()

def f1():
    person = Person('Mostafa Saad')
    # Now can see some attribute named full_name
    print(person.full_name)             # calls get
    person.full_name = 'Hello world'    # calls set
    #person.full_name = 'Helloworld'    # not enough values to unpack

def f2():
    person = Person('Ziad Mostafa')
    print(person.full_name)


if __name__ == '__main__':
    f1()