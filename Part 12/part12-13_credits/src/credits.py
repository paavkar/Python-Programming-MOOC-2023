from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(courses: list):
    return reduce(lambda credits, course: credits + course.credits, courses, 0)

def sum_of_passed_credits(courses: list):
    passed = filter(lambda a: a.grade >= 1, courses)
    return reduce(lambda credits, course: credits + course.credits, passed, 0)

def average(courses: list):
    passed = list(filter(lambda a: a.grade >= 1, courses))
    grades = reduce(lambda grades, course: grades + course.grade, passed, 0)
    return grades/len(passed)