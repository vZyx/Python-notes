
class Person:
    def __init__(self, name):
        self.first, self.last = Person.process(name)
    def __repr__(self):
        return f'Person first name: {self.first}  -  last name: {self.last}'

    def myprocess(name):
        first, *last = name.lower().split()
        last = ' '.join(last)
        return first, last

if __name__ == '__main__':
    # staticmethod: Convert a function to be a static method.
    Person.process = staticmethod(Person.myprocess)

    print(Person('Mostafa Saad Ibrahim Mohamed'))
    # Person first name: mostafa  -  last name: saad ibrahim mohamed
