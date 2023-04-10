

statistics_total_prints = 0

class StudentGradesInfo:
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

if __name__ == '__main__':
    student = StudentGradesInfo('ID1234')

    student.add_grade(70, "Math")
    student.add_grade(70, "programming 1")
    student.add_grade(85, "programming 2")

    student.print()
    print(student.get_total_grades_sum())







