
class Employee:
    def __init__(self):
        self.id = 0

def inc_id(emp):
    print(id(emp))  # 0x111 SAME
    emp.id += 1

obj1 = Employee()
obj2 = obj1
print(id(obj1))     # 0x111
print(id(obj2))     # 0x111

print(obj1.id)     # 0

inc_id(obj1)
print(obj1.id)     # 1

inc_id(obj2)
print(obj1.id)     # 2
print(obj2.id)     # 2



