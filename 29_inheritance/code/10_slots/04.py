
class Person:
    __slots__ = ['name', 'email']
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Student(Person):
    __slots__ = ['gpa'] # EXTEND with new attributes
    def __init__(self, name, email, gpa):
        Person.__init__(self, name, email)
        self.gpa = gpa

st = Student('mostafa', 'm@g', 3.7)
#print(st.__dict__)   # Now error!

# Note: Although we can respecify __slots__ as
# __slots__ = ['name', 'email', 'gpa']
# but this hides parent ones! Overall, highly discouraged
# Note: Probably this will be prevented in the future
