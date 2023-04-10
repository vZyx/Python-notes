

class Employee:
    def __init__(self, name):
        self.name = name

obj1 = Employee('Mostafa')  # mutable
obj2 = 'mostafa'            # immutable

my_tuple = (obj1, obj2)
#my_tuple[0] = Employee('belal')     # TypeError
y, z = my_tuple
print(y.name)    # Mostafa

# we can't replace tuple items
# but if an item is mutable, we can change its content

obj1.name = 'ziad'
y, z = my_tuple
print(y.name)    # ziad