
class Car:
    def get_name(self):
        return 'BMW'

class Person:
    def get_name(self):
        return 'Mostafa'

class Home:
    pass

def process(obj):
    # any object that has
    # get_name method is good
    print(obj.get_name())

process(Car())
process(Person())

# AttributeError: 'Home' object
#  has no attribute 'get_name'
#process(Home())