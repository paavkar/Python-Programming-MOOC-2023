class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list):
    return filter(lambda a: a.grade >= 1, attempts)

def attempts_with_grade(attempts: list, grade: int):
    return filter(lambda a: a.grade == grade, attempts)

def passed_students(attempts: list, course: str):
    filtered = filter(lambda a: a.course_name == course and a.grade >= 1, attempts)
    return sorted(map(lambda a: a.student_name, filtered))