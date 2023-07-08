# Write your solution here
def add_student(dictionary: dict, name: str):
    if(name not in dictionary):
        dictionary[name] = []

def print_student(dictionary, name):
    if(name in dictionary and dictionary[name] == []):
        print(f"{name}:")
        print(" no completed courses")
    elif(name in dictionary):
        print(f"{name}:")
        sum = 0
        courses = []
        for course in dictionary[name]:
            if(course[1] > 0):
                sum += course[1]
                courses.append(course)
        if(sum > 0):
            print(f" {len(dictionary[name])} completed courses:")
            for course in courses:
                print(f"  {course[0]} {course[1]}")
            print(f" average grade {sum/len(dictionary[name])}")
        else:
            print(" no completed courses")
    else:
        print(f"{name}: no such person in the database")

def add_course(dictionary: dict, name: list, tuple):
    if(name in dictionary):
        if(dictionary[name] == []):
            dictionary[name].append(tuple)
        if(tuple[1] > 0):
            for course in dictionary[name]:
                if(course[0] != tuple[0] and tuple not in dictionary[name]):
                    dictionary[name].append(tuple)
                if(course[0] == tuple[0] and tuple[1] > course[1]):
                    dictionary[name].remove(course)
                    dictionary[name].append(tuple)
    
    #print(dictionary[name])

def summary(dictionary: dict):
    print(f"students {len(dictionary)}")
    most = 0
    name = ""
    best_grade = 0
    grade_name = ""
    for person, courses in dictionary.items():
        sum = 0
        #print(person, courses)
        if(len(courses) > most):
            most = len(courses)
            name = person
        for course in courses:
            sum += course[1]
        if(len(courses) > 0 and (sum/len(courses)) > best_grade):
            best_grade = sum/len(courses)
            grade_name = person
    print(f"most courses completed {most} {name}")
    print(f"best average grade {best_grade} {grade_name}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
    #add_student(students, "Peter")
    #add_student(students, "Eliza")
    #add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    #add_course(students, "Peter", ("Introduction to Programming", 1))
    #add_course(students, "Peter", ("Advanced Course in Programming", 1))
    #add_course(students, "Eliza", ("Introduction to Programming", 5))
    #add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    #summary(students)


### Example solution
def add_student(students: dict, name: str):
    students[name] = {}
 
def print_student(students: dict, name: str):
    if not name in students:
        print(f"{name}: no such person in the database")
        return
 
    students_completed_courses = students[name]
 
    print(f"{name}:")
    if len(students_completed_courses) == 0:
        print(" no completed courses")
    else:
        print(f" {len(students_completed_courses):} completed courses:")
        sum = 0
        for course, grade in students_completed_courses.items():
            course_grade = grade[1]
            print(f"  {course} {course_grade}")
            sum += course_grade
 
        print(f" average grade {sum/len(students_completed_courses):.1f}")
 
def add_course(students: dict, name: str, completion: tuple):
    students_completed_courses = students[name]
    course_name = completion[0]
    course_grade = completion[1]
 
    # failed course is not recorded in the database
    if course_grade==0:
        return
 
    # if previous grade is higher, new grade is not recorded in the database
    if course_name in students_completed_courses:
        if students_completed_courses[course_name][1] > course_grade:
            return
 
    students_completed_courses[course_name] = completion
 
def summary(students: dict):
    print(f"students {len(students)}")
    most_courses_count = 0
    best_avg_grade = 0
    for name, completions in students.items():
        if len(completions) > most_courses_count:
            most_courses = name
            most_courses_count = len(students[most_courses])
 
        sum = 0
        for course, grade in completions.items():
            sum += grade[1]
 
        if len(completions)==0:
            avg = 0
        else:
            avg = sum/len(completions)
 
        if avg>best_avg_grade:
            best_avg_grade = avg
            best = name
 
    print(f"most courses completed {most_courses_count} {most_courses}")
    print(f"best average grade {best_avg_grade:.1f} {best}")