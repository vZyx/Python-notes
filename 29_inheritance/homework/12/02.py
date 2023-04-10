

class CommunityMember:
    pass



class Student(CommunityMember):
    pass

class Alumnus(CommunityMember):
    pass

class Employee(CommunityMember):
    pass





class Staff(Employee):
    pass

class Faculty(Employee):
    pass





class Teacher(Faculty):
    pass

class Administrator(Faculty):
    pass



class AdministratorTeacher(Teacher, Administrator):
    pass
