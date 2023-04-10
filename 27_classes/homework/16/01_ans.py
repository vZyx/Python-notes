class StudentGradesInfo:

    """
    It seems developer wants to keep track of how many times this function is called
    Proper way to maintain a static counter inside the class
    Side note: in real life, we applications keep track of what users do and analyze it
    This allows discovering what users do/don't so that we improve their experience
    """
    statistics_total_prints = 0
    MAX_COURSE_GRADE = 100

    def __init__(self, id):
        self.id = id
        self.grades = []
        self.courses_names = []

    """    
    Several mistakes:
    - It uses a magic number: numeric literal (for example, 8080 , 2048 ) that is used in the middle of a block of code without explanation
        - Define a const MAXS_COURSE_GRADE on class level
            - Imagine what happens of 100 changed? In old code, you make a lot of changes
    - This method has nothing to do with the object attributes
        - As it needs the course grade, we can make it class method

    - Bug in first if condition: it should return 0
    """

    @classmethod
    def adjust_grade(cls, grade):
        if grade < 0:
            return 0
        if grade > cls.MAX_COURSE_GRADE:
            return cls.MAX_COURSE_GRADE
        return grade

    def add_grade(self, grade, course_name):
        """
        This function adds a new course IFF the course is not already added
        If added, course old value is not overwritten!
        """
        # Docs should be AFTER not before the method/class

        if course_name in self.courses_names:
            return False

        # Critical bugL append the grades before the condition!
        self.grades.append(self.adjust_grade(grade))
        self.courses_names.append(course_name)
        return True

    def print(self):
        self.__class__.statistics_total_prints += 1

        print(f'Grades info for Student ID {self.id}')
        for idx in range(len(self.grades)):
            print(f'Course: {self.courses_names[idx]} - Grade: {self.grades[idx]}')

    def get_total_grades_sum(self):
        # Don't use magic number. Don't use class name explicitly (avoid future code changes)
        return (sum(self.grades), self.__class__.MAX_COURSE_GRADE * len(self.grades))


if __name__ == '__main__':
    student = StudentGradesInfo('ID1234')

    student.add_grade(70, "Math")
    student.add_grade(70, "programming 1")
    student.add_grade(85, "programming 2")

    student.print()







