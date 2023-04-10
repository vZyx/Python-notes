

class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def __repr__(self):
        return f'({self.name}, {self.salary}, {self.age})'

    def __lt__(self, other):
        # Observe: we use other.name in the first tuple
        return (other.name, self.salary, self.age) < (self.name, other.salary, other.age)


lst = [Employee('mostafa', 10, 18),
       Employee('Ziad', 100, 19),
       Employee('mostafa', 7, 35),
       Employee('mostafa', 7, 26),
       Employee('warda', 9, 18)]
lst.sort()
print(lst)
# [(warda, 9, 18), (mostafa, 7, 26), (mostafa, 7, 35),
#   (mostafa, 10, 18), (Ziad, 100, 19)]

# Use lambda to pass a key based on age, then name, then salary (smaller first)
lst.sort(key=lambda emp : (emp.age, emp.name, emp.salary))
print(lst)
# [(mostafa, 10, 18), (warda, 9, 18), (Ziad, 100, 19), (mostafa, 7, 26), (mostafa, 7, 35)]

# sort is in-place. We can do several sort commands to achieve one complex criteria
# but u must do it in opposite direction: we want sort on name, salary(decreasing), age
# then opposite: sort age, salary(decreasing), name
lst.sort(key=lambda emp : emp.age)
lst.sort(key=lambda emp : emp.salary, reverse=True)
lst.sort(key=lambda emp : emp.name)
# [(Ziad, 100, 19), (mostafa, 10, 18), (mostafa, 7, 26), (mostafa, 7, 35), (warda, 9, 18)]

# Same as above. Mathematically: sorting int x increasing is same sorting -x decreasing
lst.sort(key=lambda emp : (emp.name, -emp.salary, emp.age))
print(lst)