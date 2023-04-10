
class Student:
    def __init__(self):
        self.name = None
        self.email = None
        self.address = None
        self.national_id = None
        self.starting_study_year = None
        self.gpa = None
        self.studied_courses = []

    def is_valid_email(self, email):
        pass
    def add_course_grade(self, course_id, grade):
        pass
    def print_grades(self):
        pass


class Teacher:
    def __init__(self):
        self.name = None
        self.email = None
        self.address = None
        self.national_id = None
        self.starting_employement_year = None
        self.current_salary = None
        self.teaching_courses = []

    def is_valid_email(self, email):
        pass

    def add_course(self, course_id):
        pass
