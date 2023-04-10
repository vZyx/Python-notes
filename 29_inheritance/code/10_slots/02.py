

class Employee:
    employees_cnt = 0
    __slots__ = "name", "salary"    # tuple/iterable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        #self.age = 1   # u can't

print(Employee.__dict__)    # {'employees_cnt': 0, '__doc__': None, etc}
emp = Employee('most', 12)
print(dir(emp)) # 'employees_cnt': 0, '__slots__': ['name', 'salary']
                # 'name': <member 'name' of 'Employee' objects>, 'salary':
print(emp.name) # most
#print(emp.__dict__)  # AttributeError no attribute '__dict__'
#print(vars(emp))      # TypeError: vars() argument must have __dict__ attribute
del emp.name

# For us: Almost similar usage
# For python: Different implementation: More memory and time efficient!
# BUT: you lose flexibility of adding attributes! Trade off




