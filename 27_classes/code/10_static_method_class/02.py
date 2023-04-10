
class Person:
    def __init__(self, first_name, last_name):
        self.first, self.last = first_name, last_name

    def __repr__(self):
        return f'Person first name: {self.first}  -  last name: {self.last}'

    @classmethod
    def get_person_from_full_name(cls, full_name):
        first, last = cls.process(full_name)
        return cls(first, last)

    @staticmethod
    def process(name):  # No self - no interaction with class/objects
        """Convert to lower, get first word as first name, remaining as last"""
        first, *last = name.lower().split()
        last = ' '.join(last)
        return first, last

if __name__ == '__main__':
    per = Person.get_person_from_full_name('Mostafa Saad Ibrahim Mohamed')
    print(per)
    # Person first name: mostafa  -  last name: saad ibrahim mohamed