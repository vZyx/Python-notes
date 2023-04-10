

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

most = Employee('mostafa', 33)

print(most) # <__main__.Employee object at 0x7f9ec1def3d0>

# Recall __init__ is a special method (we call Dunder = “Double Under (Underscores)”.)
# It is called an implicit way to create a new object

# if we tried to print the object, we get unexpected printing (e.g. memory)

# Python search for __str__ function: if provided, it will be used to represent the object
# If not provided, it will search for __repr__ and use it
# If not provided, it will use some default way (e.g. memory address)

# print(object) or str(object) will try to do the above procedure implicitly
# If so, the used function MUST return string

# You can return anything, but this will be useless for the proper practical usage

