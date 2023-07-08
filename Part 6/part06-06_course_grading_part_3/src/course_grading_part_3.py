# tee ratkaisu tänne
# wwite your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"

students = {}

with open(student_info) as file:
    for line in file:
        parts = line.split(";")
        if(parts[0] == "id"):
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"

exercises = {}

with open(exercise_data) as file:
    for line in file:
        parts = line.split(";")
        if(parts[0] == "id"):
            continue
        exercises[parts[0]] = []
        for i in range (1, len(parts)):
            exercises[parts[0]].append(int(parts[i]))

exams = {}

with open(exam_points) as file:
    for line in file:
        parts = line.split(";")
        if(parts[0] == "id"):
            continue
        exams[parts[0]] = 0
        for i in range(1, len(parts)):
            exams[parts[0]] += int(parts[i].strip())


name_column = "name"
exercise_column = "exec_nbr"
points_column = "exec_pts."
exam_column = "exm_pts."
total_column = "tot_pts."
grade_column = "grade"
print(f"{name_column:<30}{exercise_column:<10}{points_column:<10}{exam_column:<10}{total_column:<10}{grade_column:<10}")

for student_id, name in students.items():
    exercise_sum = sum(exercises[student_id])
    course_points = exercise_sum*10//40 + exams[student_id]
    grade = 0
    if(course_points > 14 and course_points < 18):
        grade = 1
    elif(course_points > 17 and course_points < 21):
        grade = 2
    elif(course_points > 20 and course_points < 24):
        grade = 3
    elif(course_points > 23 and course_points < 28):
        grade = 4
    elif(course_points >= 28):
        grade = 5
    print(f"{name:<30}{sum(exercises[student_id]):<10}{exercise_sum*10//40:<10}{exams[student_id]:<10}{course_points:<10}{grade:<10}")