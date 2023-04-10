

class Person:
    def __init__(self, full_name):
        self.first_name, self.last_name = full_name.lower().split()

# After some time, We found it is a wrong design
# more flexible, we has explicit first name and last name
# we can use same arguments for init, but the attribute is gone!

# Now all of the hundreds of dependency fail!
def f1():
    # AttributeError: No full_name'
    person = Person('Mostafa Saad')
    print(person.full_name)


def f2():
    person = Person('Ziad Mostafa')


if __name__ == '__main__':
    f1()