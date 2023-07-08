# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

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

for student_id, name in students.items():
    print(f"{name} {sum(exercises[student_id])}")