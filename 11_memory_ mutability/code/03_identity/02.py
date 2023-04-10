

x = 1
if type(x) is int:
    print('an int')    # an int

y = None
print(y is None)        # True
print(x is not None)    # True

print(type(2.5) is float)   # True

class Employee:
    def __init__(self, name):
        self.name = name

obj1 = Employee('Mostafa')
print(type(obj1) is Employee)   # True
