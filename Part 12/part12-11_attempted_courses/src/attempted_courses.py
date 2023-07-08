class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here
def names_of_students(attempts: list):
    return map(lambda c: c.student_name, attempts)

def course_names(attempts: list):
    names = map(lambda k: k.course_name, attempts)
    # remove duplicates by using a set
    return sorted(list(set(names)))