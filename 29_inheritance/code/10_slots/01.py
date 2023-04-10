

class Employee:
    employees_cnt = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = Employee('most', 12)
print(dir(emp)) # 'employees_cnt', 'name', 'salary'
print(emp.name) # most

print(Employee.__dict__)    # {'employees_cnt': 0, '__doc__': None, etc}
print(emp.__dict__)  # {'name': 'mostafa'}
print(vars(emp))     # {'name': 'mostafa'}


