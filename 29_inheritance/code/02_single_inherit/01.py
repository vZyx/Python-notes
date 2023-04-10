
class Person:
    def __init__(self):
        self.name = 'Mostafa'
        self.email = 'Mostafa@gmail.com'

    def is_valid_email(self):
        return  self.email.endswith('@gmail.com')

    def print_info(self):
        print(self.name, self.email)


class Student(Person):
    def __init__(self):
        Person.__init__(self)   # Call parent init
        self.GPA = .5
        self.studied_courses = ['C++', 'Python']

    def print_info(self):
        print(self.name, self.GPA)


if __name__ == '__main__':
    st = Student()
    st.print_info() # Mostafa 0.5
    print(st.email) # Mostafa@gmail.com
    print(st.is_valid_email())  # True

    p = Person()
    p.name, p.email = 'Noha', 'Noha@hotmail.com'
    p.print_info()  # Noha Noha@hotmail.com
    print(p.is_valid_email())   # False

    print(type(st))     # <class '__main__.Student'>
    print(isinstance(st, Student))          # True
    print(isinstance(st, Person))           # True

    print(type(st) is Student)              # True
    print(type(st) is Person)               # False
    print(type(st) in [Student, Person])    # True

    print(issubclass(Student, Person))      # True
    print(issubclass(Student, Student))     # True
    print(issubclass(Student, list))        # False
    #print(issubclass(st, Person))          # Error: class NOT object
    print(issubclass(type(st), Person))     # True

    # Be careful from type vs isinstance
    # isinstance considers inheritance, type don't



    print(issubclass(Person, object))      # True
    print(issubclass(Student, object))     # True
    print(issubclass(list, object))        # True
    print(issubclass(int, object))         # True: int is object
    print(issubclass(BaseException, object))  # True

    import math
    print(isinstance(math, object))         # True: module is object
    print(isinstance(math.sqrt, object))    # True

    # we actually inherit its attributes & methods
    obj = object()
    print(dir(obj)) # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    print(obj.__init__)
    print(obj.__repr__())    # 0x7ff2b4169b90 default print memory address
    print(object.__name__)   # on class level



