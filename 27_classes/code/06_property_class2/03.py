

class Person:
    def __init__(self, full_name):
        # DRY Principle: DON'T repeat yourself!
        self.set_full_name(full_name)

    def set_full_name(self, full_name):
        self.first_name, self.last_name = full_name.lower().split()

    full_name = property(fset=set_full_name)

def f1():
    person = Person('Mostafa Saad')
    # Now can see some attribute named full_name
    #print(person.full_name)             # AttributeError: unreadable attribute
    person.full_name = 'Hello world'    # calls set

def f2():
    person = Person('Ziad Mostafa')
    print(person.full_name)


if __name__ == '__main__':
    f1()