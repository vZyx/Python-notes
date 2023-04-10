

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f'({self.name}, {self.salary})'

    def __lt__(self, other): # More pythonic style
        return (self.name, self.salary) < (other.name, other.salary)

    def __lt__V2(self, other):  # on name first, if tie on salary
        # More of Old C++ Culture
        if self.name != other.name:
            return self.name < other.name

        return self.salary < other.salary


lst = [Employee('mostafa', 10),
       Employee('Ziad', 100), Employee('mostafa', 7)]
lst.sort()
print(lst)  # [(Ziad, 100), (mostafa, 7), (mostafa, 10)]



