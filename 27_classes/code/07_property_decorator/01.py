

class Person:
    def __init__(self, full_name):
        self.full_name = full_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, value):
        self.first_name, self.last_name = value.lower().split()

def f1():
    person = Person('Mostafa Saad')
    # Now can see some attribute named full_name
    print(person.full_name)             # calls get
    person.full_name = 'Hello world'    # calls set




if __name__ == '__main__':
    f1()