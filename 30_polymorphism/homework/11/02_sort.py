

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

