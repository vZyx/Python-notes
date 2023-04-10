
class Person:
    def __init__(self, name):
        self.first, self.last = Person.process(name)
    def __repr__(self):
        return f'Person first name: {self.first}  -  last name: {self.last}'

    @staticmethod
    def process(name):  # No self - no interaction with class/objects
        """Convert to lower, get first word as first name, remaining as last"""
        first, *last = name.lower().split()
        last = ' '.join(last)
        return first, last

if __name__ == '__main__':
    print(Person('Mostafa Saad Ibrahim Mohamed'))
    # Person first name: mostafa  -  last name: saad ibrahim mohamed