
# is: return True if two variables are the SAME object (memory)

str1 = 'mostafa'
str2 = str1
str3 = str2

# 0x111 0x111 0x111
print(id(str1), id(str2), id(str3))

print(str1 is str3)     # True

class Employee:
    def __init__(self, name):
        self.name = name

# same value: but not mutable
obj1 = Employee('Mostafa')
obj2 = Employee('Mostafa')
obj3 = obj2

# 0x222 0x333 0x333
print(id(obj1), id(obj2), id(obj3))
print(obj2 is obj1)     # False
print(obj2 is obj3)     # True
print(obj2 is not obj3) # False