
class Person:
    __slots__ = ['name', 'email']
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Student(Person):
    __slots__ = ['gpa', '__dict__']
    def __init__(self, name, email, gpa):
        Person.__init__(self, name, email)
        self.gpa = gpa

st = Student('mostafa', 'm@g', 3.7)
st.temp = '111'
print(st.__dict__)  # {'temp': '111'}

# By adding __dict__ as slot
# we can have both slot and dynamic attributes!
