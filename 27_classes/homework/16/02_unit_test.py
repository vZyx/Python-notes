statistics_total_prints = 0


class StudentGradesInfo_OLD:
    def __init__(self, id):
        self.id = id
        self.grades = []
        self.courses_names = []

    def adjust_grade(self, grade):
        if grade < 0:
            return grade
        if grade > 100:
            return 100
        return grade

    """
    This function adds a new course IFF the course 
    is not already added
    If added, course old value is not overwritten!
    """

    def add_grade(self, grade, course_name):
        self.grades.append(self.adjust_grade(grade))

        if course_name in self.courses_names:
            return False

        self.courses_names.append(course_name)
        return True

    def print(self):
        global statistics_total_prints
        statistics_total_prints += 1

        print(f'Grades info for Student ID {self.id}')
        for idx in range(len(self.grades)):
            print(f'Course: {self.courses_names[idx]} - Grade: {self.grades[idx]}')

    def get_total_grades_sum(self):
        return (sum(self.grades), 100 * len(self.grades))


class StudentGradesInfo_FIXED:
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
        - Define a const MAX_COURSE_GRADE on class level
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


# switch between old and new to test
# StudentGradesInfo = StudentGradesInfo_OLD
StudentGradesInfo = StudentGradesInfo_FIXED


class StudentGradesInfoTester:

    @classmethod
    def test_total_courses_cnt(cls):
        student = StudentGradesInfo('ID1234')

        assert len(student.grades) == len(student.courses_names) == 0

        student.add_grade(70, "Math")
        assert len(student.grades) == len(student.courses_names) == 1
        student.add_grade(70, "programming 1")
        assert len(student.grades) == len(student.courses_names) == 2
        student.add_grade(85, "programming 2")
        assert len(student.grades) == len(student.courses_names) == 3
        student.add_grade(10, "programming 2")
        student.add_grade(20, "programming 2")
        student.add_grade(30, "programming 2")
        assert len(student.grades) == len(student.courses_names) == 3

    @classmethod
    def test_grades_sum(cls):
        student = StudentGradesInfo('ID1234')

        assert student.get_total_grades_sum() == (0, 0)

        f = 100
        input = [(5, "Math"), (-2, "programming 1"), (3, "programming 2"), (4, "programming 2")]
        output = [(5, 1 * f), (5, 2 * f), (8, 3 * f), (8, 3 * f)]

        for idx, args in enumerate(input):
            student.add_grade(*args)
            assert student.get_total_grades_sum() == output[idx], idx

    @classmethod
    def test_printing(cls):
        """
        This function is writing to console! How to test?
        1) redirect print output to a text file: https://www.kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python#:~:text=Use%20sys.,or%20more%20times%2C%20use%20file.
        2) read file content
        3) compare to what you expect!
        """
        pass

    @classmethod
    def test_all(cls):
        calls = [cls.test_grades_sum, cls.test_grades_sum]

        for call in calls:
            call()


if __name__ == '__main__':
    StudentGradesInfoTester.test_all()








