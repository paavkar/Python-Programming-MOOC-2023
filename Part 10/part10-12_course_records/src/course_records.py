# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name
    
    def grade(self):
        return self.__grade
    
    def credits(self):
        return self.__credits
    
    def change_grade(self, grade: int):
        self.__grade = grade

class CourseRecords:

    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if not name in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        if(self.__courses[name].grade() < grade):
            self.__courses[name].change_grade(grade)

    def get_course(self, name: str):
        if not name in self.__courses:
            return None
        return self.__courses[name]
    
    def statistics(self):
        count = len(self.__courses)
        credit_amount = 0
        grades = {}
        grade_total = 0
        for i in range(5, 0, -1):
            grades[i] = 0
        for name, course in self.__courses.items():
            credit_amount += course.credits()
            grade_total += course.grade()
            grades[course.grade()] += 1
        print(f"{count} completed courses, a total of {credit_amount} credits")
        mean = grade_total/count
        print(f"mean {mean:.1f}")
        print(f"grade distribution")
        for grade, amount in grades.items():
            print(f"{grade}:", "x"*amount)

class CourseRecordsApplication:

    def __init__(self):
        self.__course_records = CourseRecords()

    def help(self):
        print("commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__course_records.add_course(course, grade, credits)

    def search(self):
        course = input("course: ")
        course = self.__course_records.get_course(course)
        if(course == None):
            print("no entry for this course")
            return
        print(f"{course.name()} ({course.credits()} cr) grade {course.grade()}")

    def statistics(self):
        self.__course_records.statistics()

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.search()
            elif command == "3":
                self.statistics()
            else:
                self.help()

application = CourseRecordsApplication()
application.execute()