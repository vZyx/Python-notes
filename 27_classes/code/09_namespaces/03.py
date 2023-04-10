
class Employee:
    lst = [2, 5]    # mutable
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    obj1 = Employee('obj1')
    obj2 = Employee('obj2')

    print(Employee.lst) # [2, 5]
    print(obj1.lst)     # [2, 5]
    print(obj2.lst)     # [2, 5]

    obj1.lst = [10, 20]
    print(Employee.lst)  # [2, 5]
    print(obj1.lst)      # [10, 20]
    print(obj2.lst)      # [2, 5]

    obj2.lst += [3]
    print(Employee.lst)  # [2, 5, 3]
    print(obj1.lst)      # 10, 20]
    print(obj2.lst)      # [2, 5, 3]



