
class Person:
    def __init__(self, full_name):
        # for simplicity: 2 words space separated
        # e.g. Mostafa Ibrahim
        self.full_name = full_name.lower()

# After some time, many teams used our class!
def f1():
    person = Person('Mostafa Saad')
    print(person.full_name)
    person.full_name = 'Mostafa Ibrahim'

def f2():
    person = Person('Ziad Mostafa')
    print(person.full_name)

