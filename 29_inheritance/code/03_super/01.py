

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print(f'name: {self.name} ', end=' ')

class Student(Person):
    def __init__(self, name, email, gpa):
        super().__init__(name, email)  # make it first line
        self.gpa = gpa

    def print_info(self):
        super().print_info()    # Delegate to parent
        print(f'GPA: {self.gpa}')

if __name__ == '__main__':
    st = Student('Mostafa', 'Mostafa@gmail.com', 3.82)
    st.print_info()     # name: Mostafa  GPA: 3.82

