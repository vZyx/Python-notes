
class Employee:
    def __init__(self, name):
        self.name = name

# creates new object with =
obj1 = Employee('Mostafa')
print(id(obj1))       # 0x111

obj2 = obj1
print(id(obj2))       # 0x111

# creates new object
obj2 = Employee('belal')
print(id(obj2))      # 0x222

